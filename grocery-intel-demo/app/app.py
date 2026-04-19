"""Grocery Intelligence Platform — FastAPI backend.

All SQL is parameterized via %(name)s. Connection uses databricks-sql-connector
and the env vars injected by Databricks Apps (or the dev shell).
"""
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

from databricks import sql
from databricks.sdk import WorkspaceClient
from databricks.sdk.core import Config, oauth_service_principal
from fastapi import Body, FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

CATALOG = os.environ.get("CATALOG", "grocery_intel_demo_catalog")
SCHEMA = os.environ.get("SCHEMA", "grocery")
HOST = os.environ.get("DATABRICKS_HOST", "").replace("https://", "").rstrip("/")
WAREHOUSE_ID = os.environ.get("DATABRICKS_WAREHOUSE_ID", "")
HTTP_PATH = os.environ.get("DATABRICKS_HTTP_PATH") or (
    f"/sql/1.0/warehouses/{WAREHOUSE_ID}" if WAREHOUSE_ID else ""
)
GENIE_SPACE_ID = os.environ.get("GENIE_SPACE_ID", "")

# Databricks Apps injects DATABRICKS_CLIENT_ID / DATABRICKS_CLIENT_SECRET; fall
# back to a personal access token for local dev.
_PAT = os.environ.get("DATABRICKS_TOKEN", "")
_cfg = Config(host=f"https://{HOST}") if HOST else None


def _credentials_provider():
    return oauth_service_principal(_cfg)


app = FastAPI(title="Grocery Intelligence Platform")
STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@contextmanager
def _cursor():
    kwargs = {"server_hostname": HOST, "http_path": HTTP_PATH}
    if _PAT:
        kwargs["access_token"] = _PAT
    else:
        kwargs["credentials_provider"] = _credentials_provider
    conn = sql.connect(**kwargs)
    try:
        with conn.cursor() as c:
            yield c
    finally:
        conn.close()


def run_query(query: str, params: Optional[dict] = None) -> list[dict]:
    with _cursor() as c:
        c.execute(query, params or {})
        cols = [d[0] for d in c.description]
        return [dict(zip(cols, row)) for row in c.fetchall()]


def _q(table: str) -> str:
    return f"`{CATALOG}`.`{SCHEMA}`.`{table}`"


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/states")
def states():
    rows = run_query(f"SELECT DISTINCT state FROM {_q('gold_retail_summary')} ORDER BY state")
    return [r["state"] for r in rows]


@app.get("/api/summary")
def summary():
    q = f"""
        SELECT
          SUM(total_turnover)      AS total_turnover,
          AVG(yoy_growth_pct)      AS avg_yoy,
          (SELECT AVG(yoy_change_pct) FROM {_q('gold_food_inflation_yoy')}
             WHERE quarter >= date_format(add_months(current_date(), -12), 'yyyy') || '-Q1'
          )                        AS avg_food_yoy,
          COUNT(DISTINCT state)    AS state_count
        FROM {_q('gold_retail_summary')}
        WHERE month >= add_months(current_date(), -12)
    """
    rows = run_query(q)
    return rows[0] if rows else {"total_turnover": 0, "avg_yoy": 0, "avg_food_yoy": 0, "state_count": 0}


@app.get("/api/metrics")
def metrics(
    state: Optional[str] = Query(None),
    start: Optional[str] = Query(None),
    end: Optional[str] = Query(None),
):
    filters = ["1=1"]
    params: dict = {}
    if state and state != "All":
        filters.append("state = %(state)s")
        params["state"] = state
    if start:
        filters.append("month >= %(start)s")
        params["start"] = start
    if end:
        filters.append("month <= %(end)s")
        params["end"] = end
    where = " AND ".join(filters)
    q = f"""
        SELECT state, CAST(month AS STRING) AS month, total_turnover, yoy_growth_pct
        FROM {_q('gold_retail_summary')}
        WHERE {where}
        ORDER BY month, state
    """
    return run_query(q, params)


@app.get("/api/inflation")
def inflation(category: Optional[str] = Query(None)):
    params: dict = {}
    where = "1=1"
    if category and category != "All":
        where = "category = %(category)s"
        params["category"] = category
    q = f"""
        SELECT category, quarter, index_value
        FROM {_q('gold_food_inflation')}
        WHERE {where}
        ORDER BY quarter, category
    """
    return run_query(q, params)


@app.post("/api/genie")
def ask_genie(payload: dict = Body(...)):
    question = (payload or {}).get("question", "").strip()
    if not question:
        return JSONResponse({"error": "question required"}, status_code=400)
    if not GENIE_SPACE_ID:
        return JSONResponse({"error": "GENIE_SPACE_ID not configured"}, status_code=503)

    w = WorkspaceClient(host=f"https://{HOST}") if _PAT else WorkspaceClient()
    msg = w.genie.start_conversation_and_wait(GENIE_SPACE_ID, question)

    text, query_sql, columns, rows = None, None, [], []
    for att in (msg.attachments or []):
        if att.text and att.text.content:
            text = att.text.content
        if att.query and att.query.query:
            query_sql = att.query.query
            try:
                result = w.genie.get_message_attachment_query_result(
                    GENIE_SPACE_ID, msg.conversation_id, msg.id, att.attachment_id
                )
                sr = result.statement_response
                if sr and sr.manifest and sr.manifest.schema:
                    columns = [c.name for c in sr.manifest.schema.columns]
                if sr and sr.result and sr.result.data_array:
                    rows = sr.result.data_array[:50]
            except Exception as e:
                text = (text or "") + f"\n\n(Result fetch failed: {e})"
    return {"text": text, "sql": query_sql, "columns": columns, "rows": rows}


@app.get("/healthz")
def healthz():
    return JSONResponse({"ok": True})
