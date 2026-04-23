## Step 5: Register Model in Unity Catalog

> **Airgap reference:** `@starter-kit/references/mlflow-uc.md §3` has the full
> pattern with the exact API calls, verification SQL, and a troubleshooting
> table. Read it before prompting if you're fuzzy on any step below.

### Prompt

```
Read @starter-kit/references/mlflow-uc.md §3. Then register the best
model from our experiment to Unity Catalog:

1. Ensure mlflow.set_registry_uri("databricks-uc") is called before registering.

2. Find the best run (highest R²) from our MLflow experiment.

3. Register with the THREE-LEVEL UC name (never two-level):
   name = "workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster"
   mlflow.register_model(
       model_uri=f"runs:/{run_id}/model",
       name=name,
   )

4. Add description: "Retail turnover forecasting model for Australian states"

5. Set the alias "champion" (not "production") on the newly-registered version:
   from mlflow.tracking import MlflowClient
   MlflowClient().set_registered_model_alias(name, "champion", version)

6. Print the model name, version, and the UC UI URL
   (https://<host>/explore/data/models/workshop_vibe_coding/TEAM_SCHEMA/grocery_forecaster)
```

### Expected Result

Model registered under `workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster` with `@champion` alias.

### Navigator V-step

*"Did it register to UC, not workspace? Show me proof."*

Run this in a notebook or SQL editor:
```
DESCRIBE MODEL workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster
```
Then click the UC UI URL. If you land on `/mlflow/models/<name>` instead of `/explore/data/models/...`, the registration went to the workspace registry — re-register with the three-level name. Also confirm the alias with `MlflowClient().get_registered_model(name).aliases` — you should see `{"champion": <version>}`.

### If It Doesn't Work

- **Permission error** — Need `CREATE MODEL ON SCHEMA workshop_vibe_coding.TEAM_SCHEMA`. Ask facilitator.
- **`NO_SUCH_CATALOG` / `RESOURCE_DOES_NOT_EXIST`** — You forgot `mlflow.set_registry_uri("databricks-uc")`. Add it at the top of the script and re-run.
- **Registered to workspace by accident** — Same fix. Verify with `DESCRIBE MODEL`.
- **Run has no logged model artifact** — Training didn't use autolog or didn't call `mlflow.sklearn.log_model`. Fix training, not registration.
- **Registration fails entirely** — Fall back to the checkpoint: `workshop_vibe_coding.checkpoints.grocery_forecaster@fallback`. Note it in CLAUDE.md so the agent stops re-registering.
