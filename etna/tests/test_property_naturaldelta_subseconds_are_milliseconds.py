from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_naturaldelta_subseconds_are_milliseconds
from etna_runner.strategies import strategy_naturaldelta_subseconds_are_milliseconds


@given(strategy_naturaldelta_subseconds_are_milliseconds())
@settings(max_examples=100, deadline=None)
def test_property_naturaldelta_subseconds_are_milliseconds(value: int) -> None:
    r = property_naturaldelta_subseconds_are_milliseconds(value)
    assert r.kind != "fail", r.message
