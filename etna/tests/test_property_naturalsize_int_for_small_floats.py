from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_naturalsize_int_for_small_floats
from etna_runner.strategies import strategy_naturalsize_int_for_small_floats


@given(strategy_naturalsize_int_for_small_floats())
@settings(max_examples=100, deadline=None)
def test_property_naturalsize_int_for_small_floats(value: float) -> None:
    r = property_naturalsize_int_for_small_floats(value)
    assert r.kind != "fail", r.message
