## Track: Data Science

### Airgap-safe MLflow reference (read BEFORE any MLflow work)

**Two equivalent ways to access the same content** — pairs can use either (or both):

**(a) As a Claude Code skill** — bundled at `starter-kit/skills/databricks-mlflow-ml/`.
Install into your Claude Code skills directory so it auto-triggers whenever the agent writes MLflow code. Ships `SKILL.md` + 7 reference files (GOTCHAS, CRITICAL-interfaces, patterns-experiment-setup, patterns-training, patterns-uc-registration, patterns-batch-inference, user-journeys).

**(b) As a reference file** — `@starter-kit/references/mlflow-uc.md` for in-prompt citation:
- §1 — seven non-negotiable UC rules (includes the UC-volume artifact_location requirement)
- §2–§3 — training + registration patterns (Lab 2 Phase 1/2)
- §4 — notebook batch inference (Lab 2 Phase 3, Tier 1 default)
- §5 — Lakeflow `mlflow.spark_udf` pattern (Tier 2 stretch; includes `ai_query` anti-pattern warning)
- §6 — troubleshooting cheat sheet, including "everything is on fire" fallback

The skill was contributed to AI Dev Kit as `databricks-mlflow-ml` (PR pending). Until it lands upstream, the workshop repo is the canonical source. MLflow's online docs are not reachable from this airgapped environment.

When the agent writes MLflow code, Navigator's V-step: cross-check the generated code against these patterns — agent training data may contradict UC-specific patterns that stabilised recently.

### Data Source
- Read from gold tables: `workshop_vibe_coding.TEAM_SCHEMA.retail_summary` and `food_inflation_yoy`
- These are pre-loaded in checkpoints — no need to build the pipeline

### Feature Engineering
- Use PySpark for all feature transformations
- Create lag features (1, 3, 6, 12 month lags) using Window functions
- Create seasonal indicators (month_of_year, quarter, is_december)
- Create growth rate features (MoM, YoY)
- Output a feature table in Unity Catalog

### MLflow
- Track experiments with `mlflow.start_run()`
- Log parameters, metrics, and artifacts
- Use `mlflow.sklearn` or `mlflow.xgboost` autologging where possible

### Unity Catalog + MLflow (non-negotiable)
- Always call `mlflow.set_registry_uri("databricks-uc")` at session start — before any `register_model` or `load_model` call
- Always register models with THREE-LEVEL UC names: `workshop_vibe_coding.TEAM_SCHEMA.<model_name>`. Never two-level (`<schema>.<model_name>`) — that lands in the workspace registry
- Use aliases (`@champion`, `@challenger`) when loading models, never version numbers. Loading path is `models:/workshop_vibe_coding.TEAM_SCHEMA.<model_name>@champion`
- Never use `ai_query` on custom-registered models — that requires a Model Serving endpoint. Use `mlflow.pyfunc.load_model` (notebook) or `mlflow.pyfunc.spark_udf` (Lakeflow pipeline) instead
- Verify registration via `DESCRIBE MODEL workshop_vibe_coding.TEAM_SCHEMA.<model_name>` or the UC UI (`/explore/data/models/...`). Never trust the agent's success message alone — check UC
- If training or registration fails, fall back to the pre-built checkpoint model: `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`

### Batch Inference (Lab 2 default)
- Default path: notebook-based batch scoring with `mlflow.pyfunc.load_model` + inline chart
- Stretch path: Lakeflow `@dp.materialized_view` using `mlflow.pyfunc.spark_udf` — writes a `gold_forecast` table
- No Model Serving endpoints in Lab 2. Serving is production ops work, out of scope today

### ML Libraries
- scikit-learn for baseline models
- XGBoost for boosted tree models
- pandas is OK for small feature DataFrames after collecting from Spark
- Always start with PySpark for data loading and feature engineering
