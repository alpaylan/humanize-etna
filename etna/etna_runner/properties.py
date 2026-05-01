"""Property functions for the humanize workload.

Each property is pure and deterministic: same input always produces the same
PropertyResult. They are referenced from etna.toml and exercised both by the
plain witness functions and by the Hypothesis-driven test suite.
"""

from __future__ import annotations

import datetime as dt
import math

import humanize

from ._result import DISCARD, PASS, PropertyResult, fail


def property_metric_finite_on_zero(value: float) -> PropertyResult:
    """metric(value) returns a string for any finite value, including 0.

    The buggy version reaches math.log10(abs(0)) and raises ValueError.
    """
    if not math.isfinite(value):
        return DISCARD
    try:
        out = humanize.metric(value)
    except Exception as e:
        return fail(f"metric({value!r}) raised {type(e).__name__}: {e}")
    if not isinstance(out, str):
        return fail(f"metric({value!r}) returned non-string {out!r}")
    return PASS


def property_intword_preserves_sign(value: int) -> PropertyResult:
    """For value > 0, intword(-value) == '-' + intword(value).

    The buggy version short-circuits negative numbers through `value < powers[0]`
    (true for any negative since powers[0]==1000), so it stringifies the raw
    integer instead of humanizing it. e.g. intword(-1_000_000) returns
    '-1000000' instead of '-1.0 million'.
    """
    if value <= 0:
        return DISCARD
    pos = humanize.intword(value)
    neg = humanize.intword(-value)
    if not (isinstance(pos, str) and isinstance(neg, str)):
        return fail(f"intword({value}) or intword({-value}) returned non-string")
    expected = "-" + pos
    if neg != expected:
        return fail(f"intword({-value}) = {neg!r}; expected {expected!r}")
    return PASS


def property_intcomma_ndigits_zero_rounds(value: float) -> PropertyResult:
    """intcomma(value, 0) is the integer rounding of value, with thousands separators.

    The buggy version treats ndigits=0 as falsy and returns the raw repr,
    which still contains a decimal point for floats.
    """
    if not math.isfinite(value):
        return DISCARD
    if abs(value) > 1e15:
        return DISCARD  # large floats lose integer precision

    out = humanize.intcomma(value, 0)
    if not isinstance(out, str):
        return fail(f"intcomma({value!r}, 0) returned non-string {out!r}")
    if "." in out:
        return fail(f"intcomma({value!r}, 0) = {out!r}; expected no decimal point")
    return PASS


def property_apnumber_zero_is_zero(value: int) -> PropertyResult:
    """apnumber(0) == 'zero'; for 1..9 it spells out the digit; otherwise str(value).

    The buggy version treats 0 as out-of-range and returns '0'.
    """
    out = humanize.apnumber(value)
    if value == 0:
        if out != "zero":
            return fail(f"apnumber(0) = {out!r}; expected 'zero'")
        return PASS
    if 1 <= value <= 9:
        words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if out != words[value - 1]:
            return fail(f"apnumber({value}) = {out!r}; expected {words[value - 1]!r}")
        return PASS
    if out != str(value):
        return fail(f"apnumber({value}) = {out!r}; expected {str(value)!r}")
    return PASS


def property_naturalsize_int_for_small_floats(value: float) -> PropertyResult:
    """naturalsize on a sub-base float renders as an integer (no decimal point).

    The buggy version emits 'f"{bytes_} Bytes"' which keeps the '.0' for floats
    (e.g. '500.0 Bytes' instead of '500 Bytes').
    """
    if not math.isfinite(value):
        return DISCARD
    # Keep the input out of the abs_bytes==1 special case to avoid coupling.
    if 1 < abs(value) < 1000 and value == int(value):
        out = humanize.naturalsize(value)
        if not isinstance(out, str):
            return fail(f"naturalsize({value!r}) returned non-string {out!r}")
        if "." in out:
            return fail(f"naturalsize({value!r}) = {out!r}; expected no decimal in 'X Bytes'")
        return PASS
    return DISCARD


def property_naturaldelta_negative_is_absolute(seconds: int) -> PropertyResult:
    """naturaldelta(timedelta(seconds=-s)) == naturaldelta(timedelta(seconds=s)).

    The buggy version uses |delta.days| and |delta.seconds| separately, which
    breaks for negative timedeltas because Python normalizes them as
    days=-1, seconds=86400-...; the absolute pieces no longer compose.
    """
    # Limit to a manageable range that exercises hours/days/months/years.
    if not (1 <= seconds <= 60 * 60 * 24 * 365 * 5):
        return DISCARD
    pos = humanize.naturaldelta(dt.timedelta(seconds=seconds))
    neg = humanize.naturaldelta(dt.timedelta(seconds=-seconds))
    if pos != neg:
        return fail(
            f"naturaldelta(+{seconds}s) = {pos!r} but naturaldelta(-{seconds}s) = {neg!r}"
        )
    return PASS


def property_naturaldelta_subseconds_are_milliseconds(microseconds: int) -> PropertyResult:
    """For us in [10_000, 999_999], naturaldelta(seconds=us/1e6, minimum_unit='milliseconds')
    must equal '<us//1000> milliseconds' — i.e. the millisecond count is preserved.

    The buggy version casts the float to int (so 0.5s becomes 0s) and the
    timedelta loses every sub-second microsecond, yielding '0 milliseconds'
    regardless of the actual fraction.
    """
    if not (10_000 <= microseconds < 1_000_000):
        return DISCARD
    seconds = microseconds / 1_000_000
    out = humanize.naturaldelta(seconds, minimum_unit="milliseconds")
    if not isinstance(out, str):
        return fail(f"naturaldelta({seconds!r}, ms) returned non-string {out!r}")
    expected_ms = microseconds // 1000  # 10..999
    expected = f"{expected_ms} milliseconds"
    if out != expected:
        return fail(f"naturaldelta({seconds!r}, ms) = {out!r}; expected {expected!r}")
    return PASS
