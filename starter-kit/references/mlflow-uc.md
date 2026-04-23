# MLflow + Unity Catalog — DS Track Reference

> **Why this file exists:** the workshop runs in an airgapped environment.
> MLflow's online docs aren't reachable; no existing AI Dev Kit skill
> covers classic ML model training + UC-scoped registration
> (`databricks-mlflow-evaluation` is for GenAI agents; `databricks-model-serving`
> is what we're avoiding). This file is the airgap-safe single source of
> truth for DS pairs in Lab 2.
>
> **Now also available as a skill:** the content here is ALSO bundled as a
> proper Claude Code skill at `starter-kit/skills/databricks-mlflow-ml/`
> — install it by copying into your Claude Code environment, and it
> auto-triggers whenever you're working on MLflow + UC training code. The
> skill was contributed upstream to
> [databricks-solutions/ai-dev-kit](https://github.com/databricks-solutions/ai-dev-kit)
> (PR pending review). Until the PR lands, the bundled copy in this repo
> is the canonical source.
>
> **How to use (either way):**
> - As a reference file: `@reference` it in prompts for exact API surface
> - As an installed skill: Claude Code auto-loads it when relevant
> - Every pattern is copy-pasteable and verified against MLflow 3.11 on
>   Lakeflow SDP serverless compute version 5 (same runtime the workshop
>   pipelines use). Patterns also work on MLflow 2.16+ for pairs on older
>   classic DBRs — where 3.x behaviour diverges (e.g., `artifact_path` →
>   `name=`) it's called out in §6 / GOTCHAS.md
>
> **R.V.P.I. note:** when the agent generates MLflow code, Navigator should
> Validate against this file — especially the UC-specific rules in §1,
> which the agent's training data may contradict.

---

## §1. The Seven UC Rules (Pin These)

1. **`mlflow.set_registry_uri("databricks-uc")`** at session start. Without
   this, `register_model` silently writes to the workspace registry — you
   won't know until Lab 2 Phase 3 when the load fails.

2. **Three-level names always.** `workshop_vibe_coding.<pair_schema>.grocery_forecaster`
   — never two-level. Two-level names route to workspace registry.

3. **Aliases (`@champion`, `@challenger`) not version numbers** when loading.
   Aliases decouple the loading code from the model version — you can
   promote a new version to `@champion` without touching any loader.

4. **Never `ai_query` on custom UC models** in Lab 2. `ai_query` requires a
   serving endpoint, which requires permissions + provisioning time we
   don't have. Use `mlflow.pyfunc.load_model` (notebook) or
   `mlflow.pyfunc.spark_udf` (Lakeflow) instead.

5. **Verify registration, don't trust the code.** After `register_model`,
   run `DESCRIBE MODEL workshop_vibe_coding.<pair_schema>.grocery_forecaster`
   or open Catalog Explorer. If you see "workspace registry" in the URL,
   you're wrong — see Rule 1.

6. **If training or registration breaks, load the fallback checkpoint:**
   `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`. It's
   pre-registered. It works. Keep moving.

7. **Experiments need a UC volume `artifact_location`.** In UC-enforced
   workspaces, the default (DBFS root) is rejected — every `log_model`
   call will fail with opaque storage errors. When you create the
   experiment, pin it to a UC volume:
   ```python
   mlflow.set_experiment(
       experiment_name="/Users/{email}/grocery_forecaster",
       artifact_location="dbfs:/Volumes/workshop_vibe_coding/<pair_schema>/mlflow_artifacts/forecaster",
   )
   ```
   Prerequisite: `CREATE VOLUME IF NOT EXISTS workshop_vibe_coding.<pair_schema>.mlflow_artifacts;`
   The checkpoint schema already has a volume you can fall back to if your
   own is missing.

---

## §2. Training + Logging (Lab 2 Phase 1)

### Classic sklearn workflow

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from mlflow.models import infer_signature

# Rule 1: set registry URI before anything else
mlflow.set_registry_uri("databricks-uc")

# Rule 7: experiment needs a UC volume artifact_location
# Prereq (run once per pair schema):
#   CREATE VOLUME IF NOT EXISTS workshop_vibe_coding.<pair_schema>.mlflow_artifacts;
mlflow.set_experiment(
    experiment_name=f"/Users/{user_email}/grocery_forecaster",
    artifact_location=f"dbfs:/Volumes/workshop_vibe_coding/<pair_schema>/mlflow_artifacts/forecaster",
)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

with mlflow.start_run(run_name="gbr_v1"):
    model = GradientBoostingRegressor(n_estimators=100, max_depth=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Signature + input_example are both LOAD-bearing — they're what
    # makes pyfunc.load_model work downstream. Don't skip.
    signature = infer_signature(X_train, model.predict(X_train[:5]))

    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",          # path within the run
        signature=signature,
        input_example=X_train.iloc[:5],
        # Do NOT pass registered_model_name here unless you've already
        # done Rule 1. We register in Phase 2 as a separate explicit step.
    )

    # Metrics the Navigator will ask about during V-step
    mlflow.log_metric("rmse", root_mean_squared_error(y_test, predictions))
    mlflow.log_metric("mae", mean_absolute_error(y_test, predictions))
    mlflow.log_param("n_estimators", 100)
```

**Navigator V-step:**
- Open the MLflow experiment UI. Is there a run? Is there a model artifact
  on the run (not just metrics)?
- Click the `input_example` — does it show 5 rows of your training features?
- Is the signature schema present (input columns + output type)?
- If any of these are missing, the registration step in Phase 2 will
  either fail or produce a model that can't be loaded.

### Why the signature + input_example matter

`mlflow.pyfunc.load_model(...)` calls at load time wrap the model in a
`PythonModel` interface that uses the signature to coerce inputs. Without
a signature, the loaded model accepts `dict`, `DataFrame`, or `ndarray`
ambiguously — leading to silent prediction corruption when Lakeflow's
columnar Spark DataFrame gets passed in. Always log a signature.

---

## §3. Registering to Unity Catalog (Lab 2 Phase 2)

### The explicit-register pattern (recommended for Lab 2)

```python
import mlflow
from mlflow import MlflowClient

mlflow.set_registry_uri("databricks-uc")   # Rule 1 (idempotent to repeat)

# Three-level name — Rule 2
MODEL_NAME = "workshop_vibe_coding.<pair_schema>.grocery_forecaster"

# Find the run (adjust run_id from Phase 1)
run_id = "<your_run_id_from_phase_1>"
model_uri = f"runs:/{run_id}/model"

# Register. This creates MODEL_NAME in UC if missing, and creates a new
# version linked to the run's model artifact.
result = mlflow.register_model(
    model_uri=model_uri,
    name=MODEL_NAME,
)
print(f"Registered {MODEL_NAME} version {result.version}")

# Set @champion alias — Rule 3
client = MlflowClient()
client.set_registered_model_alias(
    name=MODEL_NAME,
    alias="champion",
    version=result.version,
)
```

### The log-and-register-in-one-call pattern (shortcut)

Only use this if you've already set the registry URI (Rule 1) AND you
already know which model should become `@champion`:

```python
mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="model",
    signature=signature,
    input_example=X_train.iloc[:5],
    registered_model_name="workshop_vibe_coding.<pair_schema>.grocery_forecaster",
)
# Still need to set the alias separately — log_model doesn't do that.
```

### Verify — Navigator V-step (Rule 5)

```sql
-- Run in a SQL cell
DESCRIBE MODEL workshop_vibe_coding.<pair_schema>.grocery_forecaster;

-- Check the Aliases section shows @champion pointing at the right version
SHOW TBLPROPERTIES workshop_vibe_coding.<pair_schema>.grocery_forecaster;
```

Or visually:
1. Open Catalog Explorer.
2. Navigate to `workshop_vibe_coding > <pair_schema> > Models`.
3. You should see `grocery_forecaster` with an `@champion` alias badge.
4. **Wrong path check:** if the model is under "Workspace" (left sidebar,
   not Catalog) — you forgot Rule 1. Delete, set `registry_uri`, re-register.

### Common registration errors

| Error | Cause | Fix |
|-------|-------|-----|
| `RestException: PERMISSION_DENIED ... CREATE MODEL` | Pair missing `CREATE MODEL ON SCHEMA` grant | Raise with facilitator — pre-workshop grant was missed |
| Registered but not visible in Catalog Explorer | `set_registry_uri` not called — in workspace registry | Re-set URI, re-register. Old one is orphaned, that's fine. |
| `Invalid model name: must be three-level namespaced` | Two-level name used | Change to `catalog.schema.name` |
| `Alias 'champion' already exists on version N` | Alias was set on a previous run | Either move the alias (`set_registered_model_alias` again) or use `@challenger` for the new version |

---

## §4. Batch Inference — Tier 1 (Interactive Notebook)

This is the default path for Lab 2 Phase 3.

```python
import mlflow

mlflow.set_registry_uri("databricks-uc")   # Rule 1

# Load by alias — Rule 3
model = mlflow.pyfunc.load_model(
    "models:/workshop_vibe_coding.<pair_schema>.grocery_forecaster@champion"
)

# Score a sample of silver features (don't score the whole table in a notebook
# — that's what Tier 2 is for). `.toPandas()` is fine for up to ~10k rows.
features = (
    spark.table("workshop_vibe_coding.<pair_schema>.silver_features")
    .limit(1000)
    .toPandas()
)

predictions = model.predict(features)

# Attach predictions back to the features DataFrame for display
features["prediction"] = predictions

# Display inline — Databricks notebooks render this as a chart
display(spark.createDataFrame(features))
```

### Turning the output into a demo artifact

Add a predicted-vs-actual chart:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(features["month_date"], features["turnover_millions"], label="Actual", alpha=0.7)
ax.plot(features["month_date"], features["prediction"], label="Predicted", linestyle="--")
ax.set_title("Grocery Forecast — Predicted vs Actual")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
display(fig)
```

### Fallback — use the checkpoint if your model won't load

```python
model = mlflow.pyfunc.load_model(
    "models:/workshop_vibe_coding.checkpoints.grocery_forecaster@fallback"
)
# Same .predict() API. You lose "I trained this" story but keep
# "I scored predictions in a notebook from a UC-registered model".
```

---

## §5. Batch Inference — Tier 2 Stretch (Lakeflow Batch Job)

Only attempt if Tier 1 is done with 20+ min remaining.

### The pattern — `mlflow.pyfunc.spark_udf` inside `@dp.materialized_view`

Add a new file to the pipeline:

```python
# src/gold/gold_forecast.py
import databricks.declarative_pipelines as dp
import mlflow
from pyspark.sql import functions as F

@dp.materialized_view(
    comment="Grocery turnover forecast using @champion model from UC.",
)
def gold_forecast():
    # Load model as a Spark UDF — scales across executors, no per-row Python loop
    mlflow.set_registry_uri("databricks-uc")
    forecast_udf = mlflow.pyfunc.spark_udf(
        spark,
        model_uri="models:/workshop_vibe_coding.<pair_schema>.grocery_forecaster@champion",
        result_type="double",
    )

    features = spark.read.table("workshop_vibe_coding.<pair_schema>.silver_features")

    # Apply UDF — pass all input columns the model's signature declares
    return features.withColumn(
        "forecast_turnover_millions",
        forecast_udf(
            "turnover_lag_1",
            "turnover_lag_12",
            "rolling_3m_avg",
            "state_share_of_national",
            # ... all signature input columns
        ),
    )
```

### ⚠️ DO NOT use `ai_query`

`ai_query('<model_name>', <input>)` requires a Model Serving endpoint
to be provisioned and running. That is exactly what we're avoiding in
this lab. Symptoms of the wrong path:

- Code references `ai_query` or a URL like `/serving-endpoints/...`
- Errors mention `serving endpoint` or `endpoint_status`
- You're asked to wait for an endpoint to "become ready"

If you see any of these: stop. You're on the wrong path. Use
`mlflow.pyfunc.spark_udf` above instead.

### Navigator V-step for Tier 2

- *"Does any line in this pipeline reference `ai_query`, `serving-endpoints`,
  or an endpoint URL?"* → If yes, wrong path.
- Run the pipeline once. Does `gold_forecast` materialize? (Catalog
  Explorer → pair_schema → Tables)
- Query it from Genie: *"what's the forecast for each state next month?"*
  The table should answer.

---

## §5b. Install note for local training

If you're training locally (laptop, CI, not a Databricks cluster), the
default `pip install mlflow` leaves out the cloud-storage SDKs MLflow
needs to stage artifacts into UC-managed storage. `log_model` works
(tracking server receives it), but `register_model` fails with:

```
MlflowException: Unable to import necessary dependencies to access
model version files in Unity Catalog
  → ModuleNotFoundError: No module named 'azure' (or 'boto3' / 'google.cloud')
```

**Fix:** install the databricks extras.

```bash
pip install 'mlflow[databricks]'
# or, lighter:
pip install 'mlflow-skinny[databricks]'
```

Databricks clusters ship these extras pre-installed — this only bites
outside-cluster workflows.

---

## §6. Troubleshooting Cheat Sheet

### `mlflow.exceptions.MlflowException: Could not find registered model`

- Check Rule 1: `mlflow.get_registry_uri()` should return `"databricks-uc"`,
  not a workspace URI.
- Check Rule 2: the name in your load call is the exact three-level name
  you registered.
- Check Rule 3: the alias exists. Run `DESCRIBE MODEL ...` — does it show
  `aliases: {champion: 3}` or similar?

### `PERMISSION_DENIED: User does not have EXECUTE on MODEL`

- You can register but not load someone else's model. Either load the
  fallback (§3) or ask the facilitator to grant `EXECUTE ON MODEL`.

### Predictions look wrong (all same value, or NaN)

- Check the signature: did `input_example` get logged? Run
  `mlflow.models.get_model_info(model_uri).signature`.
- Column order matters for `spark_udf` — pass columns in the order the
  signature declares, not alphabetically.
- If using pandas: the feature DataFrame's dtypes should match the
  `input_example`'s dtypes. Integer vs float mismatches silently cast.

### Lakeflow pipeline errors on `spark_udf` load

- The cluster needs MLflow installed. On serverless SDP, it's there by
  default. On classic, confirm `mlflow>=2.16` in the pipeline's library
  settings.
- The model URI must use `models:/` (UC registry), not `runs:/` (experiment
  artifact). Only registered models work as Spark UDFs.

### "Everything is on fire, I just need to demo"

Use the fallback. In a notebook cell:

```python
import mlflow
mlflow.set_registry_uri("databricks-uc")
model = mlflow.pyfunc.load_model(
    "models:/workshop_vibe_coding.checkpoints.grocery_forecaster@fallback"
)

features = (
    spark.table("workshop_vibe_coding.checkpoints.retail_features")
    .limit(500).toPandas()
)
features["prediction"] = model.predict(features)
display(spark.createDataFrame(features))
```

Every DS pair can reach this point regardless of what broke upstream.

---

## §7. Where This Fits in R.V.P.I.

- **Research**: this file + the experiment you ran in Phase 1 + your CLAUDE.md
- **Validate**: §3 verification steps, §6 troubleshooting checks. Navigator owns.
- **Plan**: pick the path (Tier 1 notebook or Tier 2 Lakeflow) before writing
  code. Write the §4 or §5 pattern into your prompt as a spec.
- **Implement**: small steps. Log model → run fails → verify → register →
  alias → load → predict. Each step has its own V-step in §3–§6.

---

## §8. Future Work (Not for This Workshop)

If/when someone creates a `databricks-mlflow-ml` skill in AI Dev Kit,
this file's §1–§5 content maps 1:1 to the skill's SKILL.md + references.
The gap this file fills is real: AI Dev Kit's current skills are
`databricks-mlflow-evaluation` (GenAI evaluation — different audience)
and `databricks-model-serving` (the thing we're deliberately skipping).
A classic-ML / UC-registration skill would be a valuable contribution.
