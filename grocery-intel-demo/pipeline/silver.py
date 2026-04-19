"""Silver layer — decode ABS codes, parse time, apply units, type-cast."""
from pyspark import pipelines as dp
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType

RETAIL_STATE = F.create_map([F.lit(x) for pair in {
    "AUS": "Australia", "1": "NSW", "2": "VIC", "3": "QLD", "4": "SA",
    "5": "WA", "6": "TAS", "7": "NT", "8": "ACT",
}.items() for x in pair])

RETAIL_INDUSTRY = F.create_map([F.lit(x) for pair in {
    "20": "Total (all industries)",
    "41": "Food retailing",
    "42": "Household goods retailing",
    "43": "Clothing, footwear & personal accessory",
    "44": "Department stores",
    "45": "Other retailing",
    "46": "Cafes, restaurants & takeaway",
}.items() for x in pair])

CPI_CAPITAL = F.create_map([F.lit(x) for pair in {
    "1": "Sydney", "2": "Melbourne", "3": "Brisbane", "4": "Adelaide",
    "5": "Perth", "6": "Hobart", "7": "Darwin", "8": "Canberra", "50": "Australia",
}.items() for x in pair])

CPI_CATEGORY = F.create_map([F.lit(x) for pair in {
    "20001": "Food & non-alcoholic beverages",
    "1144":  "Food (aggregate)",
    "30001": "Dairy & related",
    "30002": "Bread & cereal",
    "30003": "Meat & seafood",
    "114120": "Fruit & vegetables",
}.items() for x in pair])


@dp.materialized_view(name="silver_retail_turnover", comment="Decoded, typed retail turnover by state x industry x month")
@dp.expect("turnover_positive", "turnover > 0")
@dp.expect("state_known", "state IS NOT NULL")
def silver_retail_turnover():
    return (
        spark.read.table("bronze_retail_raw")
        .filter(F.col("REGION").isNotNull() & F.col("INDUSTRY").isNotNull())
        .withColumn("state", RETAIL_STATE[F.col("REGION")])
        .withColumn("industry", RETAIL_INDUSTRY[F.col("INDUSTRY")])
        .withColumn("month", F.to_date(F.concat_ws("-", F.col("TIME_PERIOD"), F.lit("01"))))
        .withColumn(
            "turnover",
            (F.col("OBS_VALUE").cast(DoubleType()) * F.pow(F.lit(10.0), F.col("UNIT_MULT").cast("int"))),
        )
        .filter(F.col("state").isNotNull() & F.col("industry").isNotNull() & F.col("month").isNotNull())
        .select("state", "industry", "month", "turnover")
    )


@dp.materialized_view(name="silver_food_cpi", comment="Decoded food CPI index, aggregated monthly → quarterly, by capital x category")
@dp.expect("index_reasonable", "index_value BETWEEN 30 AND 400")
@dp.expect("capital_known", "capital IS NOT NULL")
def silver_food_cpi():
    monthly = (
        spark.read.table("bronze_cpi_food_raw")
        .filter(F.col("REGION").isNotNull() & F.col("INDEX").isNotNull())
        .withColumn("capital", CPI_CAPITAL[F.col("REGION")])
        .withColumn("category", CPI_CATEGORY[F.col("INDEX")])
        .withColumn("month_date", F.to_date(F.concat_ws("-", F.col("TIME_PERIOD"), F.lit("01"))))
        .withColumn("quarter", F.concat(F.year("month_date"), F.lit("-Q"), F.quarter("month_date")))
        .withColumn("index_value_m", F.col("OBS_VALUE").cast(DoubleType()))
        .filter(F.col("capital").isNotNull() & F.col("category").isNotNull() & F.col("index_value_m").isNotNull())
    )
    return (
        monthly.groupBy("capital", "category", "quarter")
        .agg(F.avg("index_value_m").alias("index_value"))
        .select("capital", "category", "quarter", "index_value")
    )
