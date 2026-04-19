"""Smoke tests for the pipeline modules.

These assert the module structure and that the decorated functions exist.
We don't instantiate Spark here — Lakeflow runs the real thing. These tests
give us fast feedback if someone renames a gold table (breaking the app
contract) or forgets an @dp.expect.
"""
import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

PIPELINE_DIR = Path(__file__).resolve().parents[1] / "pipeline"


@pytest.fixture(autouse=True)
def stub_pyspark_pipelines(monkeypatch):
    """Provide a stub `pyspark.pipelines` module so imports work without a cluster."""
    import types

    stub = types.ModuleType("pyspark.pipelines")

    def decorator_factory(*_a, **_kw):
        def wrap(fn):
            fn._dp_registered = True
            return fn
        return wrap

    stub.table = decorator_factory
    stub.materialized_view = decorator_factory
    stub.expect = lambda *_a, **_kw: (lambda fn: fn)

    monkeypatch.setitem(sys.modules, "pyspark.pipelines", stub)
    # Also stub `spark` at module load time.
    monkeypatch.setitem(sys.modules, "__main__", types.SimpleNamespace(spark=MagicMock()))

    sys.path.insert(0, str(PIPELINE_DIR))
    yield
    sys.path.remove(str(PIPELINE_DIR))
    for m in ("bronze", "silver", "gold"):
        sys.modules.pop(m, None)


def test_bronze_exposes_both_raw_tables():
    import bronze  # noqa: E402

    assert hasattr(bronze, "bronze_retail_raw")
    assert hasattr(bronze, "bronze_cpi_food_raw")


def test_bronze_retail_url_targets_abs_rt():
    import inspect, bronze  # noqa: E402

    src = inspect.getsource(bronze.bronze_retail_raw)
    assert "ABS,RT,1.0.0" in src
    assert "startPeriod" in src


def test_silver_decode_maps_cover_all_states():
    # Silver imports spark at module load — stub it.
    import sys, types
    sys.modules["__main__"].spark = MagicMock()
    import silver  # noqa: E402
    import inspect

    src = inspect.getsource(silver)
    for state in ("NSW", "VIC", "QLD", "SA", "WA", "TAS", "NT", "ACT"):
        assert state in src, f"Silver missing state decode for {state}"


def test_silver_has_quality_expectations():
    sys_mod = __import__("sys")
    sys_mod.modules["__main__"].spark = MagicMock()
    import inspect, silver  # noqa: E402

    src = inspect.getsource(silver)
    assert "@dp.expect" in src


def test_gold_defines_four_contract_tables():
    sys_mod = __import__("sys")
    sys_mod.modules["__main__"].spark = MagicMock()
    import gold  # noqa: E402

    for tbl in (
        "gold_retail_summary",
        "gold_retail_turnover",
        "gold_food_inflation",
        "gold_food_inflation_yoy",
    ):
        assert hasattr(gold, tbl), f"Missing gold table function: {tbl}"


def test_gold_retail_summary_computes_yoy():
    sys_mod = __import__("sys")
    sys_mod.modules["__main__"].spark = MagicMock()
    import inspect, gold  # noqa: E402

    src = inspect.getsource(gold.gold_retail_summary)
    assert "lag" in src.lower()
    assert "12" in src  # 12-month window for YoY
    assert "yoy_growth_pct" in src
