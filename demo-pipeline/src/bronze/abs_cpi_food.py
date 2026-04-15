# Databricks notebook source
"""Bronze layer: ABS Consumer Price Index (Food) ingestion.

Ingests raw CSV data from the ABS SDMX API for quarterly CPI food
indices by state. No transformations — raw columns preserved.
"""

try:
    import databricks.declarative_pipelines as dp
except ModuleNotFoundError:
    import dlt as dp
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp


@dp.expect("valid_time_period", "TIME_PERIOD IS NOT NULL")
@dp.expect("valid_obs_value", "OBS_VALUE IS NOT NULL")
@dp.table(
    comment="Raw ABS CPI Food data from SDMX API",
)
def bronze_abs_cpi_food():
    """Ingest ABS CPI Food CSV from UC volume.

    Reads quarterly food price indices by state since 2010
    from pre-staged CSV in the raw_data volume.
    """
    spark = SparkSession.getActiveSession()

    return (
        spark.read.csv(
            "/Volumes/workshop_vibe_coding/demo/raw_data/abs_cpi_food.csv",
            header=True,
            inferSchema=True,
        )
        .withColumn("_ingested_at", current_timestamp())
    )
