"""
Model training test stubs for Data Science track Lab 2.
Copy to tests/test_model.py before starting.
"""


# ── Model Training ────────────────────────────────────────────────────


def test_model_predictions_positive(spark):
    """All predictions are positive numbers (turnover can't be negative)."""
    # TODO: Load model, run predictions on test set
    # TODO: Assert all predictions > 0
    pass


def test_model_r2_score(spark):
    """Model achieves R² > 0.5 on test set."""
    # TODO: Load model, predict on held-out test data
    # TODO: Calculate R² score
    # TODO: Assert R² > 0.5
    pass


def test_model_logged_to_mlflow():
    """Training run logged model artifact to MLflow."""
    # TODO: Query MLflow for latest run in our experiment
    # TODO: Assert run has a logged model artifact
    # TODO: Assert run has R², MAE, RMSE metrics logged
    pass


# ── Batch Inference (Unity Catalog model) ─────────────────────────────


def test_model_registered_in_uc():
    """Best run is registered under the three-level UC name with @champion alias."""
    # TODO: MlflowClient().get_registered_model("workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster")
    # TODO: Assert aliases dict contains "champion"
    pass


def test_batch_predictions_shape():
    """Batch inference on 1,000 rows returns 1,000 predictions with no negatives."""
    # TODO: Load model by alias: models:/workshop_vibe_coding.TEAM_SCHEMA.grocery_forecaster@champion
    # TODO: Score 1,000 rows from retail_features
    # TODO: Assert len(predictions) == 1000 and min(predictions) >= 0
    pass
