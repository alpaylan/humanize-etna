from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_apnumber_zero_is_zero
from etna_runner.strategies import strategy_apnumber_zero_is_zero


@given(strategy_apnumber_zero_is_zero())
@settings(max_examples=100, deadline=None)
def test_property_apnumber_zero_is_zero(value: int) -> None:
    r = property_apnumber_zero_is_zero(value)
    assert r.kind != "fail", r.message
