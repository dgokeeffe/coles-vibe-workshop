# Databricks notebook source
"""Silver layer: Food Price Index transformation.

Decodes series codes, parses quarterly dates, and standardizes column names
from the bronze ABS CPI Food table.
"""

try:
    import databricks.declarative_pipelines as dp
except ModuleNotFoundError:
    import dlt as dp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, to_date, concat, year, quarter as quarter_fn


REGION_DECODE = {
    1: "New South Wales",
    2: "Victoria",
    3: "Queensland",
    4: "South Australia",
    5: "Western Australia",
    6: "Tasmania",
    7: "Northern Territory",
    8: "Australian Capital Territory",
}

INDEX_DECODE = {
    10001: "All groups CPI",
    20001: "Food and non-alcoholic beverages",
}


@dp.expect_or_fail("valid_date", "date IS NOT NULL")
@dp.expect(
    "valid_state",
    "state IN ('New South Wales','Victoria','Queensland','South Australia',"
    "'Western Australia','Tasmania','Northern Territory','Australian Capital Territory')",
)
@dp.expect("positive_index", "cpi_index > 0")
@dp.table(
    comment="Cleaned CPI food price index with decoded regions and categories",
)
def silver_food_price_index():
    """Transform bronze CPI food data into analytics-ready silver table."""
    spark = SparkSession.getActiveSession()
    df = spark.read.table("LIVE.bronze_abs_cpi_food")

    # Build region decode (REGION is INT)
    region_expr = lit("Unknown")
    for code, name in REGION_DECODE.items():
        region_expr = when(col("REGION") == code, lit(name)).otherwise(region_expr)

    # Build index decode (INDEX is INT)
    index_expr = lit("Unknown")
    for code, name in INDEX_DECODE.items():
        index_expr = when(col("INDEX") == code, lit(name)).otherwise(index_expr)

    # TIME_PERIOD is STRING like "2010-Q1" — parse to first day of quarter
    return (
        df.withColumn("state", region_expr)
        .withColumn("category", index_expr)
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
        # 20001 (food-specific) unavailable in this API version — use All groups CPI
    )
