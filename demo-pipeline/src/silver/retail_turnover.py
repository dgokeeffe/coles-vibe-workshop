# Databricks notebook source
"""Silver: Retail Turnover — decode regions/industries, cast dates."""

try:
    import databricks.declarative_pipelines as dp
except ModuleNotFoundError:
    import dlt as dp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, year, quarter

from grocery_intelligence import REGION_DECODE, INDUSTRY_DECODE, decode_column


@dp.expect_or_fail("valid_date", "date IS NOT NULL")
@dp.expect(
    "valid_state",
    "state IN ('New South Wales','Victoria','Queensland','South Australia',"
    "'Western Australia','Tasmania','Northern Territory','Australian Capital Territory')",
)
@dp.expect("positive_turnover", "turnover_millions > 0")
@dp.table(comment="Cleaned retail turnover with decoded regions and industries")
def silver_retail_turnover():
    spark = SparkSession.getActiveSession()
    df = spark.read.table("LIVE.bronze_abs_retail_trade")

    return (
        df.withColumn("state", decode_column("REGION", REGION_DECODE))
        .withColumn("industry", decode_column("INDUSTRY", INDUSTRY_DECODE))
        .withColumn("date", col("TIME_PERIOD").cast("date"))
        .withColumn("year", year("date"))
        .withColumn("month", month("date"))
        .withColumn("quarter", quarter("date"))
        .withColumnRenamed("OBS_VALUE", "turnover_millions")
        .select("state", "industry", "date", "year", "month", "quarter", "turnover_millions")
        .filter(col("date").isNotNull())
        .filter(col("turnover_millions").isNotNull())
        .filter(col("turnover_millions") > 0)
    )
