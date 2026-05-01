"""Hypothesis strategies for the humanize workload.

Strategies stick to the CrossHair-friendly subset: integers, floats, plain
arithmetic. No @composite, no st.data, no opaque object-from-type.
"""

from __future__ import annotations

from hypothesis import strategies as st


def strategy_metric_finite_on_zero():
    return st.floats(
        min_value=-1e30,
        max_value=1e30,
        allow_nan=False,
        allow_infinity=False,
    )


def strategy_intword_preserves_sign():
    return st.integers(min_value=1_000, max_value=10**32)


def strategy_intcomma_ndigits_zero_rounds():
    return st.floats(
        min_value=-1e12,
        max_value=1e12,
        allow_nan=False,
        allow_infinity=False,
    )


def strategy_apnumber_zero_is_zero():
    return st.integers(min_value=-100, max_value=100)


def strategy_naturalsize_int_for_small_floats():
    # Floats whose fractional part is zero, in (1, 1000), so we exercise the
    # `abs_bytes < base` branch that the bug regressed.
    return st.integers(min_value=2, max_value=999).map(float)


def strategy_naturaldelta_negative_is_absolute():
    # Cover seconds, minutes, hours, days, weeks, months, years.
    return st.integers(min_value=1, max_value=60 * 60 * 24 * 365 * 5)


def strategy_naturaldelta_subseconds_are_milliseconds():
    return st.integers(min_value=10_000, max_value=999_999)
