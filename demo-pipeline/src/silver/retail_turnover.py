# Databricks notebook source
"""Silver layer: Retail Turnover transformation.

Decodes region and industry codes, extracts date components, and renames
columns from the bronze ABS Retail Trade table.
"""

try:
    import databricks.declarative_pipelines as dp
except ModuleNotFoundError:
    import dlt as dp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, year, quarter, when, lit


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

INDUSTRY_DECODE = {
    20: "Food retailing",
    41: "Clothing, footwear and personal accessories",
    42: "Department stores",
    43: "Other retailing",
    44: "Cafes, restaurants and takeaway",
    45: "Household goods retailing",
}


@dp.expect_or_fail("valid_date", "date IS NOT NULL")
@dp.expect(
    "valid_state",
    "state IN ('New South Wales','Victoria','Queensland','South Australia',"
    "'Western Australia','Tasmania','Northern Territory','Australian Capital Territory')",
)
@dp.expect("positive_turnover", "turnover_millions > 0")
@dp.table(
    comment="Cleaned retail turnover with decoded regions and industries",
)
def silver_retail_turnover():
    """Transform bronze retail trade into analytics-ready silver table."""
    spark = SparkSession.getActiveSession()
    df = spark.read.table("LIVE.bronze_abs_retail_trade")

    # Build region decode (REGION is INT from inferSchema)
    region_expr = lit("Unknown")
    for code, name in REGION_DECODE.items():
        region_expr = when(col("REGION") == code, lit(name)).otherwise(region_expr)

    # Build industry decode (INDUSTRY is INT)
    industry_expr = lit("Unknown")
    for code, name in INDUSTRY_DECODE.items():
        industry_expr = when(col("INDUSTRY") == code, lit(name)).otherwise(industry_expr)

    # TIME_PERIOD already parsed as DATE by inferSchema ("2010-01" → 2010-01-01)
    return (
        df.withColumn("state", region_expr)
        .withColumn("industry", industry_expr)
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
