"""Backend tests for the Grocery Intelligence app.

Mocks the databricks-sql-connector so we can test endpoint shape and
parameterized-SQL wiring without a real warehouse.
"""
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("DATABRICKS_HOST", "fake.cloud.databricks.com")
os.environ.setdefault("DATABRICKS_HTTP_PATH", "/sql/1.0/warehouses/fake")
os.environ.setdefault("DATABRICKS_TOKEN", "fake-token")
os.environ.setdefault("CATALOG", "grocery_intel_demo_catalog")
os.environ.setdefault("SCHEMA", "grocery")

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
import app as app_module  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    def fake_run_query(sql, params=None):
        if "DISTINCT state" in sql:
            return [{"state": "NSW"}, {"state": "VIC"}, {"state": "QLD"}]
        if "gold_retail_summary" in sql:
            return [
                {"state": "NSW", "month": "2024-01-01", "total_turnover": 30000.0, "yoy_growth_pct": 3.2},
                {"state": "NSW", "month": "2024-02-01", "total_turnover": 31000.0, "yoy_growth_pct": 3.5},
            ]
        if "gold_food_inflation" in sql and "yoy" not in sql:
            return [
                {"category": "Bread & cereal", "quarter": "2024-Q1", "index_value": 128.4},
                {"category": "Bread & cereal", "quarter": "2024-Q2", "index_value": 129.1},
            ]
        if "SUM(total_turnover)" in sql:
            return [{"total_turnover": 1234567.0, "avg_yoy": 3.1, "avg_food_yoy": 4.7, "state_count": 8}]
        return []

    monkeypatch.setattr(app_module, "run_query", fake_run_query)
    return TestClient(app_module.app)


def test_states_endpoint_returns_list(client):
    r = client.get("/api/states")
    assert r.status_code == 200
    assert r.json() == ["NSW", "VIC", "QLD"]


def test_metrics_endpoint_passes_params(client, monkeypatch):
    captured = {}

    def capturing_run_query(sql, params=None):
        captured["sql"] = sql
        captured["params"] = params
        return [{"state": "NSW", "month": "2024-01-01", "total_turnover": 30000.0, "yoy_growth_pct": 3.2}]

    monkeypatch.setattr(app_module, "run_query", capturing_run_query)
    r = client.get("/api/metrics", params={"state": "NSW", "start": "2023-01-01", "end": "2024-12-31"})
    assert r.status_code == 200
    assert "%(state)s" in captured["sql"]
    assert captured["params"]["state"] == "NSW"
    assert captured["params"]["start"] == "2023-01-01"
    assert captured["params"]["end"] == "2024-12-31"
    assert r.json()[0]["state"] == "NSW"


def test_inflation_endpoint_filters_by_category(client, monkeypatch):
    captured = {}

    def capturing_run_query(sql, params=None):
        captured["sql"] = sql
        captured["params"] = params
        return [{"category": "Bread & cereal", "quarter": "2024-Q1", "index_value": 128.4}]

    monkeypatch.setattr(app_module, "run_query", capturing_run_query)
    r = client.get("/api/inflation", params={"category": "Bread & cereal"})
    assert r.status_code == 200
    assert "%(category)s" in captured["sql"]
    assert captured["params"]["category"] == "Bread & cereal"


def test_summary_endpoint_returns_cards(client):
    r = client.get("/api/summary")
    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) >= {"total_turnover", "avg_yoy", "avg_food_yoy", "state_count"}
    assert body["state_count"] == 8
