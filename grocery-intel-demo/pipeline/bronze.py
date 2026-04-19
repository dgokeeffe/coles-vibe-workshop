"""Bronze layer — raw ABS SDMX-CSV ingest via HTTPS."""
from pyspark import pipelines as dp
import requests, pandas as pd, io

ABS_HEADERS = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}
ABS_TIMEOUT = 120


def _fetch_sdmx_csv(url: str, params: dict) -> pd.DataFrame:
    r = requests.get(url, headers=ABS_HEADERS, params=params, timeout=ABS_TIMEOUT)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), dtype=str)


@dp.table(name="bronze_retail_raw", comment="ABS Retail Trade (RT 1.0.0) seas-adj monthly turnover, all states x industries")
@dp.expect("has_obs_value", "OBS_VALUE IS NOT NULL")
def bronze_retail_raw():
    pdf = _fetch_sdmx_csv(
        "https://data.api.abs.gov.au/data/ABS,RT,1.0.0/M1..20..M",
        {"startPeriod": "2020-01"},
    )
    return spark.createDataFrame(pdf)


@dp.table(name="bronze_cpi_food_raw", comment="ABS CPI (2.0.0) food index, monthly, 8 capital cities, selected categories")
@dp.expect("has_obs_value", "OBS_VALUE IS NOT NULL")
def bronze_cpi_food_raw():
    # NB: capital-city CPI (REGION 1..8) is only published at monthly frequency on this endpoint.
    # We aggregate to quarterly in silver.
    pdf = _fetch_sdmx_csv(
        "https://data.api.abs.gov.au/data/ABS,CPI,2.0.0/1.20001+1144+30001+30002+30003+114120.10.1+2+3+4+5+6+7+8.M",
        {"startPeriod": "2020-01"},
    )
    return spark.createDataFrame(pdf)
