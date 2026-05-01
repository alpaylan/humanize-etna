from __future__ import annotations

from hypothesis import given, settings

from etna_runner.properties import property_intcomma_ndigits_zero_rounds
from etna_runner.strategies import strategy_intcomma_ndigits_zero_rounds


@given(strategy_intcomma_ndigits_zero_rounds())
@settings(max_examples=100, deadline=None)
def test_property_intcomma_ndigits_zero_rounds(value: float) -> None:
    r = property_intcomma_ndigits_zero_rounds(value)
    assert r.kind != "fail", r.message
