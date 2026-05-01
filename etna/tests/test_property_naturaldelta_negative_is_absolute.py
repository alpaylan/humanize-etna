from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_naturaldelta_negative_is_absolute
from etna_runner.strategies import strategy_naturaldelta_negative_is_absolute


@given(strategy_naturaldelta_negative_is_absolute())
@settings(max_examples=100, deadline=None)
def test_property_naturaldelta_negative_is_absolute(value: int) -> None:
    r = property_naturaldelta_negative_is_absolute(value)
    assert r.kind != "fail", r.message
