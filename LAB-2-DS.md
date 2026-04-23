# Lab 2: Train, Register & Batch-Score (Data Science Track)

**Duration:** 80 minutes
**Goal:** Train a forecasting model, register it cleanly in Unity Catalog, and produce a batch predictions artifact you can demo
**Team Size:** Pairs (two-person teams)

> Complete `LAB-0-GETTING-STARTED.md` and `LAB-1-DS.md` first.

---

## Pair Programming

Same pattern as Lab 1.

- **Driver:** types prompts, runs tests, commits.
- **Navigator:** reads outputs, verifies in the MLflow UI / Unity Catalog Model Registry, challenges at the **V** step of R.V.P.I.
- **Swap every 15 min** — set a timer.
- **Escalation rule:** if a task doesn't fit R.V.P.I. in 15 min, split it.

Before you start, re-read your CLAUDE.md. Is it still current after Lab 1?

---

## The Mission

Your feature table is ready. Train a model to predict retail turnover, register it to **Unity Catalog** under a three-level name with a `@champion` alias, then **batch-score** a sample of features so you have a concrete predictions artifact to demo.

> **No Model Serving endpoint today.** Provisioning a serving endpoint is a 10–20 minute ops task (permissions, warm-up, auth). That's Monday-morning work. Today we stay in notebooks + pipelines where the feedback loop is seconds, not minutes.

> **Airgap-safe reference — read before any MLflow work:**
> **[`starter-kit/references/mlflow-uc.md`](starter-kit/references/mlflow-uc.md)** has copy-pasteable patterns for every phase below — training (§2), UC registration (§3), Tier 1 notebook scoring (§4), Tier 2 Lakeflow stretch (§5), plus troubleshooting (§6) and a guaranteed-works fallback. MLflow's online docs aren't reachable from this environment; this file is the single source of truth. When the agent generates MLflow code, Navigator's V-step is to cross-check against this file.

---

> **The Small Steps Principle (continued from Lab 1)**
>
> Keep each prompt to **1–3 min of agent work**. Split "train + register + score" into separate prompts. See `LAB-1-DE.md` Phases 2–3 for the canonical pattern.
>
> **Heuristic:** *"After this prompt finishes, will I KNOW whether it worked?"* If no → split it.

---

## Phase 1: Train Model + Write Tests (20 min)

> **Pair Tasks**
> - **Driver:** Run the test prompt first (1.1), then the training prompt (1.2).
> - **Navigator:** Read the generated tests — do they actually capture "predictions positive" and "R² > 0.5"? Flag if not. While the agent trains, open the MLflow UI and verify runs are landing in the right experiment.

> **UC volume prerequisite (run once per pair schema, BEFORE the training prompt):**
> ```sql
> CREATE VOLUME IF NOT EXISTS workshop_vibe_coding.<pair_schema>.mlflow_artifacts;
> ```
> Experiments in UC-enforced workspaces need `artifact_location` pointing at a UC volume — without it, `log_model` fails. See `@starter-kit/references/mlflow-uc.md §1` Rule 7.

### 1.1 Write model tests

```
Write pytest tests for model training in tests/test_model.py:

1. test_model_predictions_positive: all predictions are positive (turnover can't be negative)
2. test_model_r2_score: R² > 0.5 on test set
3. test_model_logged_to_mlflow: run has model artifact, R², MAE, RMSE metrics

Write ONLY tests. Do NOT implement yet.
```

### 1.2 Train the model

```
Train a retail turnover forecasting model:

1. Set mlflow.set_registry_uri("databricks-uc") at the top of the script
2. Read feature table: workshop_vibe_coding.TEAM_SCHEMA.retail_features
3. Target: turnover_millions
4. Features: all lag, seasonal, and growth columns
5. Split: 80% train / 20% test (split by date, not random)
6. Try both RandomForestRegressor and XGBRegressor
7. Use mlflow.sklearn.autolog() or mlflow.xgboost.autolog()
8. Log both models, compare R², MAE, RMSE
9. Print which model performed better and the MLflow run URL

Run tests after training.
```

> **Navigator V-step:** Open the MLflow experiment UI. Do you see two runs (RF + XGB)? Is the model artifact present on the best run? Can you click through to the `input_example`?

> **Starter Kit:** Copy-paste prompt in `starter-kit/prompts/ds/04-train-model.md`

---

## Phase 2: Register in Unity Catalog (25 min)

> **Pair Tasks**
> - **Swap Driver/Navigator** if the timer has fired.
> - **Driver:** Run 2.1 (register to UC), then 2.2 (verify + set alias).
> - **Navigator:** This phase is your moment. Accidental writes to the **workspace** registry (instead of **Unity Catalog**) are the #1 silent failure in MLflow. Your job: demand proof it landed in UC.

### 2.1 Register the model to Unity Catalog

```
Register the best model from our experiment to Unity Catalog:

1. Ensure mlflow.set_registry_uri("databricks-uc") is set
2. Find the best run (highest R²) from our MLflow experiment
3. Register with the THREE-LEVEL UC name:
   workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster
4. Use mlflow.register_model(
       model_uri=f"runs:/{run_id}/model",
       name="workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster"
   )
5. Add description: "Retail turnover forecasting model for Australian states"
6. Set the alias "champion" on the newly-registered version using
   MlflowClient().set_registered_model_alias(name, "champion", version)

Print the registered model name, version, and the UC URL.
```

### 2.2 Verify it actually landed in Unity Catalog

```
Prove the model is in Unity Catalog, not the workspace registry:

1. Run this SQL and show me the output:
   DESCRIBE MODEL workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster

2. List aliases using MlflowClient().get_registered_model(name).aliases
   — confirm "champion" points to the version we just registered

3. Construct the UC UI URL:
   https://<workspace-host>/explore/data/models/workshop_vibe_coding/TEAM_SCHEMA/grocery_forecaster
   Print it so the Navigator can click through.
```

> **Navigator V-step:** *"Did it register to UC, not workspace? Show me proof."* Click the UC UI link. Does the model card show the right input signature (lag features, seasonal, growth)? If you see it under `/mlflow/models` (workspace registry) instead of `/explore/data/models` (UC), you registered to the wrong place — fix it before Phase 3.

> **Escape hatch — registration failed?** Use the pre-built checkpoint model:
> `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`
> You can load it exactly the same way in Phase 3. Note it in CLAUDE.md so the agent stops trying to re-register.

> **Starter Kit:** Copy-paste prompt in `starter-kit/prompts/ds/05-register-model.md`

---

## Phase 3: Batch Inference (25 min)

**Everyone does Path A.** Only move to Path B if you finish Path A with 20+ minutes remaining.

> **Why batch, not serving?** Serving endpoints are a legitimate production need, but they cost 10–20 min to provision plus another 5 min of permissions debugging per team. For a forecasting model scored monthly, batch is the right answer anyway. Don't let the shiny endpoint distract you from shipping predictions.

### Path A (Tier 1 default): Interactive notebook inference

> **Pair Tasks**
> - **Swap Driver/Navigator** if the timer has fired.
> - **Driver:** Create a new notebook, load the model via alias, score 1,000 rows, plot results.
> - **Navigator:** Sanity-check the predictions. Are they positive? Are they in the right order of magnitude (hundreds to thousands of $M)? Compare to actual `turnover_millions` on the same rows.

#### 3.1 Score a sample in a notebook

```
Create a Databricks notebook at notebooks/batch_inference.py (or .ipynb)
that scores a sample from our feature table:

1. Load the model via ALIAS (not version number):
   import mlflow
   mlflow.set_registry_uri("databricks-uc")
   model = mlflow.pyfunc.load_model(
       "models:/workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster@champion"
   )

2. Load 1,000 rows of features:
   features = spark.table("workshop_vibe_coding.TEAM_SCHEMA.retail_features") \
       .orderBy("month").limit(1000).toPandas()

3. Separate feature columns from target/key columns:
   feature_cols = [c for c in features.columns if c.startswith("turnover_lag_")
                   or c in ("month_of_year", "quarter", "is_december", "is_q4",
                            "turnover_mom_growth", "turnover_yoy_growth")]
   X = features[feature_cols]

4. Predict and attach:
   features["predicted_turnover"] = model.predict(X)

5. Plot predicted vs actual inline:
   - Pick the top-3 state/industry combos by row count
   - Line chart per combo: actual vs predicted over time
   - Use matplotlib; display inline with plt.show()

6. Print summary stats:
   - Mean absolute error
   - Count of negative predictions (should be 0)
   - First 10 rows of (month, state, industry, turnover_millions, predicted_turnover)
```

> **Navigator V-step:** *"Does this look sane for forecasting retail turnover?"* Check:
> - Zero negative predictions
> - Predicted values within ~30% of actuals on the sample
> - Chart tracks the actual curve (not a flat line)
> If any of those fail, the model loaded wrong — re-check the alias and the feature columns.

**Demo artifact:** The notebook output — predicted-vs-actual chart + summary stats. Export cell output to HTML or screenshot the chart before moving on.

> **Starter Kit:** Copy-paste prompt in `starter-kit/prompts/ds/06-batch-inference.md`

---

### Path B (Tier 2 stretch): Scheduled Lakeflow batch job

**Only start Path B if you have 20+ minutes left after Path A.** Skipping to B without a working A leaves you with nothing to demo.

> **Pair Tasks**
> - **Driver:** Add a `@dp.materialized_view` to the existing Lakeflow pipeline that loads the model via `mlflow.spark_udf` and writes `gold_forecast`.
> - **Navigator:** Verify the materialized view builds in the pipeline UI, check row counts match `silver_features`, and open a Genie conversation on the schema to query the forecast.

> **⚠️ Critical warning — do NOT use `ai_query` here**
>
> `ai_query(endpoint_name, request)` requires a **Model Serving endpoint**, which we explicitly do not have today. If your agent reaches for `ai_query`, it's gone down the wrong path.
>
> The correct primitive is `mlflow.spark_udf` — it loads the UC-registered model directly into the pipeline's executors as a Spark UDF. No endpoint, no auth token, no warm-up.
>
> **Navigator check:** *Does any line in this pipeline reference a serving endpoint URL, `ai_query`, or `serving-endpoints`? If yes, you're on the wrong path — stop and re-prompt.*

#### 3.2 Add a forecast materialized view

```
Add a new materialized view to our Lakeflow pipeline that batch-scores
every row of silver_features using the registered model.

1. File: src/gold/gold_forecast.py
2. Import:
   import databricks.declarative_pipelines as dp
   import mlflow
3. At module load, configure the UC registry:
   mlflow.set_registry_uri("databricks-uc")
4. Define the UDF once at module scope:
   predict_udf = mlflow.pyfunc.spark_udf(
       spark,
       "models:/workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster@champion",
       result_type="double",
   )
5. Define the materialized view:
   @dp.materialized_view(
       name="gold_forecast",
       comment="Batch forecast of retail turnover using the @champion model",
   )
   def gold_forecast():
       features = dp.read("silver_features")  # or spark.read.table
       feature_cols = [...]  # same columns as the training script
       return features.withColumn(
           "predicted_turnover",
           predict_udf(*[features[c] for c in feature_cols]),
       )
6. Do NOT add ai_query or any serving-endpoint reference anywhere.
7. Run the pipeline and wait for gold_forecast to complete.
```

> **Navigator V-step:** Open the Lakeflow pipeline UI. Did `gold_forecast` appear as a node? Did it materialize without errors? Run:
> `SELECT COUNT(*) FROM workshop_vibe_coding.TEAM_SCHEMA.gold_forecast` — does it match the `silver_features` row count? Open Genie on the schema and ask: *"What's the average predicted turnover by state for 2025?"*

**Demo artifact:** The `gold_forecast` table queried through Genie.

> **Starter Kit:** Tier 2 prompt in `starter-kit/prompts/ds/06-batch-inference.md`

---

## Phase 4: Demo Prep (10 min)

You have **3 minutes** in the demo slot.

**Path A pairs (most teams):**
1. Show the MLflow experiment UI — the two runs you compared
2. Show the model in Unity Catalog — the `@champion` alias
3. Show the notebook output — predicted-vs-actual chart + summary stats
4. 60-second explanation: what you built, what surprised you, what you'd do next

**Path B pairs (stretch):**
1. Show the MLflow experiment + UC registration (same as above)
2. Show the Lakeflow pipeline DAG with the new `gold_forecast` node
3. Open Genie and run a live query against `gold_forecast`
4. 60-second explanation: why batch + `mlflow.spark_udf` instead of a serving endpoint

> **Navigator V-step:** Run the demo end-to-end once as a dry-run before the Show & Tell. Caught something broken? You have 5 min to fix it.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Model training OOM** | Reduce feature count or sample size. Collect to pandas for small datasets. |
| **`register_model` 404 / NO_SUCH_CATALOG** | Forgot `mlflow.set_registry_uri("databricks-uc")`. Set it and re-register. |
| **Model in workspace registry, not UC** | Same fix. Re-register under the three-level name. Check `DESCRIBE MODEL`. |
| **Registration permission error** | Need `CREATE MODEL ON SCHEMA workshop_vibe_coding.TEAM_SCHEMA`. Ask facilitator. |
| **Low R² score** | Try XGBoost instead of RandomForest, or add more features. |
| **Model load fails in notebook** | Check the alias exists: `MlflowClient().get_model_version_by_alias(name, "champion")` |
| **Agent reaches for `ai_query`** | Say: "No. We have no serving endpoint. Use `mlflow.pyfunc.load_model` (notebook) or `mlflow.spark_udf` (pipeline)." Update CLAUDE.md. |
| **Spark UDF can't find model** | Ensure `mlflow.set_registry_uri("databricks-uc")` is called BEFORE `spark_udf` is created. |
| **Training failed entirely** | Use the checkpoint: `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`. Skip to Phase 3 Path A. |

---

## Success Criteria

- [ ] Model trained with R² > 0.5
- [ ] Model registered in **Unity Catalog** under `workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster`
- [ ] `@champion` alias set and verified via `DESCRIBE MODEL`
- [ ] Batch inference executed (Path A notebook output OR Path B `gold_forecast` table)
- [ ] Predicted-vs-actual chart (Path A) or Genie query result (Path B) ready to demo
- [ ] All tests passing
- [ ] Ready for 3-minute demo

---

## Reflection Questions (for Demo)

1. How accurate were your model's predictions? Where does it fail?
2. Why batch inference instead of a serving endpoint for this use case? When would you flip the answer?
3. What does the `@champion` alias buy you over version numbers?
4. How does UC registration differ from the workspace registry, and why does it matter for governance?
