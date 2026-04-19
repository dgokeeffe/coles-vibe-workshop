"""Gold layer — business-ready tables the app consumes.

Contract (column names & types) is fixed — the app depends on it.
"""
from pyspark import pipelines as dp
from pyspark.sql import functions as F
from pyspark.sql.window import Window


@dp.materialized_view(
    name="gold_retail_summary",
    comment="Monthly total retail turnover by state, with YoY growth",
)
def gold_retail_summary():
    w = Window.partitionBy("state").orderBy("month")
    return (
        spark.read.table("silver_retail_turnover")
        .filter(F.col("industry") == "Total (all industries)")
        .filter(F.col("state") != "Australia")
        .groupBy("state", "month")
        .agg(F.sum("turnover").alias("total_turnover"))
        .withColumn("turnover_lag_12m", F.lag("total_turnover", 12).over(w))
        .withColumn(
            "yoy_growth_pct",
            F.when(
                F.col("turnover_lag_12m").isNotNull() & (F.col("turnover_lag_12m") != 0),
                ((F.col("total_turnover") - F.col("turnover_lag_12m")) / F.col("turnover_lag_12m")) * 100.0,
            ),
        )
        .select("state", "month", "total_turnover", "yoy_growth_pct")
    )


@dp.materialized_view(
    name="gold_retail_turnover",
    comment="Monthly retail turnover by state and industry",
)
def gold_retail_turnover():
    return (
        spark.read.table("silver_retail_turnover")
        .filter(F.col("industry") != "Total (all industries)")
        .filter(F.col("state") != "Australia")
        .groupBy("state", "industry", "month")
        .agg(F.sum("turnover").alias("turnover"))
        .select("state", "industry", "month", "turnover")
    )


@dp.materialized_view(
    name="gold_food_inflation",
    comment="Quarterly food CPI index by category (Australia-wide avg of capitals)",
)
def gold_food_inflation():
    return (
        spark.read.table("silver_food_cpi")
        .groupBy("category", "quarter")
        .agg(F.avg("index_value").alias("index_value"))
        .select("category", "quarter", "index_value")
    )


@dp.materialized_view(
    name="gold_food_inflation_yoy",
    comment="Quarterly YoY food CPI change by capital city and category",
)
def gold_food_inflation_yoy():
    w = Window.partitionBy("capital", "category").orderBy("quarter")
    return (
        spark.read.table("silver_food_cpi")
        .withColumn("index_lag_4q", F.lag("index_value", 4).over(w))
        .withColumn(
            "yoy_change_pct",
            F.when(
                F.col("index_lag_4q").isNotNull() & (F.col("index_lag_4q") != 0),
                ((F.col("index_value") - F.col("index_lag_4q")) / F.col("index_lag_4q")) * 100.0,
            ),
        )
        .withColumnRenamed("capital", "state")
        .select("state", "category", "quarter", "yoy_change_pct")
    )
