"""Plain-Python witness functions.

Each witness calls a single property with frozen inputs. On the base tree
every witness must return PASS; with the corresponding patch reverse-applied
every witness for that variant must return fail(...).
"""

from __future__ import annotations

from ._result import PropertyResult
from . import properties as P


def witness_metric_finite_on_zero_case_zero() -> PropertyResult:
    return P.property_metric_finite_on_zero(0.0)


def witness_intword_preserves_sign_case_minus_million() -> PropertyResult:
    return P.property_intword_preserves_sign(1_000_000)


def witness_intcomma_ndigits_zero_rounds_case_thousand_decimal() -> PropertyResult:
    return P.property_intcomma_ndigits_zero_rounds(1234.5454545)


def witness_apnumber_zero_is_zero_case_zero() -> PropertyResult:
    return P.property_apnumber_zero_is_zero(0)


def witness_naturalsize_int_for_small_floats_case_500_float() -> PropertyResult:
    return P.property_naturalsize_int_for_small_floats(500.0)


def witness_naturaldelta_negative_is_absolute_case_five_hours() -> PropertyResult:
    return P.property_naturaldelta_negative_is_absolute(5 * 3600)


def witness_naturaldelta_subseconds_are_milliseconds_case_half_second() -> PropertyResult:
    return P.property_naturaldelta_subseconds_are_milliseconds(500_000)
