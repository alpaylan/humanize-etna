from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_metric_finite_on_zero
from etna_runner.strategies import strategy_metric_finite_on_zero


@given(strategy_metric_finite_on_zero())
@settings(max_examples=100, deadline=None)
def test_property_metric_finite_on_zero(value: float) -> None:
    r = property_metric_finite_on_zero(value)
    assert r.kind != "fail", r.message
