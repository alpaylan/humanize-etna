from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_intword_preserves_sign
from etna_runner.strategies import strategy_intword_preserves_sign


@given(strategy_intword_preserves_sign())
@settings(max_examples=100, deadline=None)
def test_property_intword_preserves_sign(value: int) -> None:
    r = property_intword_preserves_sign(value)
    assert r.kind != "fail", r.message
