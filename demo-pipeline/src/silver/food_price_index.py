# Databricks notebook source
"""Silver: Food Price Index — decode regions/indices, parse quarterly dates."""

try:
    import databricks.declarative_pipelines as dp
except ModuleNotFoundError:
    import dlt as dp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, to_date, concat, year, quarter as quarter_fn

from grocery_intelligence import REGION_DECODE, INDEX_DECODE, decode_column


@dp.expect_or_fail("valid_date", "date IS NOT NULL")
@dp.expect(
    "valid_state",
    "state IN ('New South Wales','Victoria','Queensland','South Australia',"
    "'Western Australia','Tasmania','Northern Territory','Australian Capital Territory')",
)
@dp.expect("positive_index", "cpi_index > 0")
@dp.table(comment="Cleaned CPI food price index with decoded regions and categories")
def silver_food_price_index():
    spark = SparkSession.getActiveSession()
    df = spark.read.table("LIVE.bronze_abs_cpi_food")

    return (
        df.withColumn("state", decode_column("REGION", REGION_DECODE))
        .withColumn("category", decode_column("INDEX", INDEX_DECODE))
        .withColumn(
            "date",
            to_date(
                concat(
                    col("TIME_PERIOD").substr(1, 4),
                    lit("-"),
                    when(col("TIME_PERIOD").contains("Q1"), lit("01"))
                    .when(col("TIME_PERIOD").contains("Q2"), lit("04"))
                    .when(col("TIME_PERIOD").contains("Q3"), lit("07"))
                    .when(col("TIME_PERIOD").contains("Q4"), lit("10")),
                    lit("-01"),
                ),
                "yyyy-MM-dd",
            ),
        )
        .withColumn("year", year("date"))
        .withColumn("quarter", quarter_fn("date"))
        .withColumnRenamed("OBS_VALUE", "cpi_index")
        .select("state", "category", "date", "year", "quarter", "cpi_index")
        .filter(col("date").isNotNull())
        .filter(col("cpi_index").isNotNull())
    )
