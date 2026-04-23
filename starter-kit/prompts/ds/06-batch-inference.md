## Step 6: Batch Inference

Load the UC-registered model and produce a batch of predictions. Two tiers — start with Tier 1.

> **Airgap reference:** MLflow's online docs aren't reachable. The full
> API surface for both tiers (with signatures, common errors, and the
> "everything is on fire" fallback) lives in
> `@starter-kit/references/mlflow-uc.md` — §4 for Tier 1, §5 for Tier 2,
> §6 for troubleshooting.

---

### Tier 1 (default): Notebook batch inference

Every pair does this. Demo artifact = the notebook output.

#### Prompt

```
Read @starter-kit/references/mlflow-uc.md §4. Then create a Databricks
notebook at notebooks/batch_inference.py that scores a sample from our
feature table with the UC-registered model.

1. Configure MLflow to use Unity Catalog:
   import mlflow
   mlflow.set_registry_uri("databricks-uc")

2. Load the model by ALIAS (not version number):
   model = mlflow.pyfunc.load_model(
       "models:/workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster@champion"
   )

3. Load 1,000 rows of features ordered by month:
   features = spark.table("workshop_vibe_coding.TEAM_SCHEMA.retail_features") \
       .orderBy("month").limit(1000).toPandas()

4. Select the feature columns the model expects (lag, seasonal, growth).

5. Predict:
   features["predicted_turnover"] = model.predict(features[feature_cols])

6. Plot predicted vs actual inline with matplotlib:
   - Top-3 state/industry combos by row count
   - One line chart per combo, actual vs predicted over time

7. Print summary:
   - Mean absolute error
   - Count of negative predictions (should be 0)
   - First 10 rows of (month, state, industry, turnover_millions, predicted_turnover)

Do not create a serving endpoint. Do not use ai_query.
```

#### Expected Result

A notebook cell output with the predicted-vs-actual chart and a summary table. Zero negative predictions.

#### Navigator V-step

Ask the Driver: *"Does this look sane for forecasting retail turnover?"*
- Are predicted values within roughly 30% of actuals on the sample?
- Does the chart track the actual curve, or is it a flat line (broken features)?
- Are there zero negative predictions?
If any of those fail, the model loaded wrong or the feature columns were mis-mapped — fix before moving on.

#### If It Doesn't Work

- **`RESOURCE_DOES_NOT_EXIST`** — Missing `mlflow.set_registry_uri("databricks-uc")`. Add it at the top.
- **Alias not found** — Phase 2 didn't set `@champion`. Run `MlflowClient().set_registered_model_alias(name, "champion", version)`.
- **Feature column mismatch** — Model signature and notebook columns diverged. Check `model.metadata.get_input_schema()`.
- **Registration failed entirely** — Load the fallback: `models:/workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`.

---

### Tier 2 (stretch): Lakeflow batch job with `mlflow.spark_udf`

Only start Tier 2 if Tier 1 is done with **20+ minutes remaining**. Otherwise you'll have nothing to demo.

> ⚠️ **Do NOT use `ai_query` here.** `ai_query` requires a Model Serving endpoint, which we explicitly do not have today. The correct primitive is `mlflow.pyfunc.spark_udf` — it loads the UC-registered model directly into the pipeline's executors. No endpoint, no auth token, no warm-up. If the agent proposes `ai_query`, stop and re-prompt.

#### Prompt

```
Read @starter-kit/references/mlflow-uc.md §5 (includes the ai_query
anti-pattern warning). Then add a new materialized view to our Lakeflow
pipeline that batch-scores silver_features using the UC-registered model.

1. Create src/gold/gold_forecast.py.

2. Imports:
   import databricks.declarative_pipelines as dp
   import mlflow

3. Configure UC registry at module load:
   mlflow.set_registry_uri("databricks-uc")

4. Create the Spark UDF once at module scope (NOT inside the function):
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
       features = dp.read("silver_features")
       feature_cols = [<same columns as the training script>]
       return features.withColumn(
           "predicted_turnover",
           predict_udf(*[features[c] for c in feature_cols]),
       )

6. DO NOT import or call ai_query anywhere.
7. DO NOT add any serving-endpoint reference.

Run the pipeline and wait for gold_forecast to build.
```

#### Expected Result

`workshop_vibe_coding.TEAM_SCHEMA.gold_forecast` materializes with a row count matching `silver_features` and a `predicted_turnover` column.

#### Navigator V-step

*"Does any line in this pipeline reference `ai_query`, `serving-endpoints`, or an endpoint URL?"*
- If yes → wrong path. The agent went down the serving rabbit hole. Stop, re-read the CLAUDE.md rule, re-prompt with `mlflow.pyfunc.spark_udf`.
- If no → open the Lakeflow pipeline UI. Did `gold_forecast` appear as a node and complete without errors? Open Genie and query: *"What's the average predicted turnover by state for 2025?"* Does it return?

#### If It Doesn't Work

- **`ai_query` used by accident** — Rip it out. You need `mlflow.pyfunc.spark_udf` instead. Update CLAUDE.md if the agent keeps reverting.
- **`spark_udf` raises `RESOURCE_DOES_NOT_EXIST`** — `mlflow.set_registry_uri("databricks-uc")` must be called before `spark_udf` is created.
- **Pipeline hangs on `gold_forecast`** — Model file is large; let it run. If >5 min, check driver logs for serialization errors.
- **Column type mismatch** — `spark_udf` expects double/float inputs. Cast categorical or boolean columns explicitly.
