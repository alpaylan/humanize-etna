# humanize — Injected Bugs

Pure-Python human-readable conversions for numbers, file sizes and dates (python-humanize/humanize). Bug fixes mined from upstream history; modern HEAD is the base, each patch reverse-applies a fix to install the original bug.

Total mutations: 7

## Bug Index

| # | Variant | Name | Location | Injection | Fix Commit |
|---|---------|------|----------|-----------|------------|
| 1 | `apnumber_zero_off_by_one_2f179b6_1` | `apnumber_zero_off_by_one` | `src/humanize/number.py:305` | `patch` | `2f179b6b5c1e2eb88240e3ec42ff9edeb946ea65` |
| 2 | `intcomma_ndigits_zero_03863fe_1` | `intcomma_ndigits_zero` | `src/humanize/number.py:164` | `patch` | `03863fed6c2ba02cfd13d5b1e0b161f680c7b966` |
| 3 | `intword_negative_no_sign_520aac1_1` | `intword_negative_no_sign` | `src/humanize/number.py:239` | `patch` | `520aac16c448f3cfd72f7c5812b04a3238e77bb4` |
| 4 | `metric_zero_crash_b1ee687_1` | `metric_zero_crash` | `src/humanize/number.py:570` | `patch` | `b1ee6875820839a59f1b6f4a5fedc7cad8883834` |
| 5 | `naturaldelta_negative_components_b939b2e_1` | `naturaldelta_negative_components` | `src/humanize/time.py:157` | `patch` | `b939b2e50ca7449f89b69d29a057886942e27b36` |
| 6 | `naturaldelta_subsecond_872d733_1` | `naturaldelta_subsecond` | `src/humanize/time.py:150` | `patch` | `872d7331fe3e307d3cc682d422f51f2de13c0fa7` |
| 7 | `naturalsize_float_int_cast_11e62ee_1` | `naturalsize_float_int_cast` | `src/humanize/filesize.py:97` | `patch` | `11e62eeedb8990298c3612af82376dc2344d24f8` |

## Property Mapping

| Variant | Property | Witness(es) |
|---------|----------|-------------|
| `apnumber_zero_off_by_one_2f179b6_1` | `ApnumberZeroIsZero` | `witness_apnumber_zero_is_zero_case_zero` |
| `intcomma_ndigits_zero_03863fe_1` | `IntcommaNdigitsZeroRounds` | `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` |
| `intword_negative_no_sign_520aac1_1` | `IntwordPreservesSign` | `witness_intword_preserves_sign_case_minus_million` |
| `metric_zero_crash_b1ee687_1` | `MetricFiniteOnZero` | `witness_metric_finite_on_zero_case_zero` |
| `naturaldelta_negative_components_b939b2e_1` | `NaturaldeltaNegativeIsAbsolute` | `witness_naturaldelta_negative_is_absolute_case_five_hours` |
| `naturaldelta_subsecond_872d733_1` | `NaturaldeltaSubsecondsAreMilliseconds` | `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` |
| `naturalsize_float_int_cast_11e62ee_1` | `NaturalsizeIntForSmallFloats` | `witness_naturalsize_int_for_small_floats_case_500_float` |

## Framework Coverage

| Property | proptest | quickcheck | crabcheck | hegel |
|----------|---------:|-----------:|----------:|------:|
| `ApnumberZeroIsZero` | ✓ | ✓ | ✓ | ✓ |
| `IntcommaNdigitsZeroRounds` | ✓ | ✓ | ✓ | ✓ |
| `IntwordPreservesSign` | ✓ | ✓ | ✓ | ✓ |
| `MetricFiniteOnZero` | ✓ | ✓ | ✓ | ✓ |
| `NaturaldeltaNegativeIsAbsolute` | ✓ | ✓ | ✓ | ✓ |
| `NaturaldeltaSubsecondsAreMilliseconds` | ✓ | ✓ | ✓ | ✓ |
| `NaturalsizeIntForSmallFloats` | ✓ | ✓ | ✓ | ✓ |

## Bug Details

### 1. apnumber_zero_off_by_one

- **Variant**: `apnumber_zero_off_by_one_2f179b6_1`
- **Location**: `src/humanize/number.py:305` (inside `apnumber`)
- **Property**: `ApnumberZeroIsZero`
- **Witness(es)**:
  - `witness_apnumber_zero_is_zero_case_zero` — apnumber(0) must be 'zero'
- **Source**: internal — Fix: AP style for 0 is 'zero'
  > apnumber() used to test `0 < value < 10`, treating 0 as out-of-range. The AP style guide spells 0 as 'zero', so the fix widens the range to `0 <= value < 10` and prepends 'zero' to the word tuple.
- **Fix commit**: `2f179b6b5c1e2eb88240e3ec42ff9edeb946ea65` — Fix: AP style for 0 is 'zero'
- **Invariant violated**: apnumber(0) == 'zero'; for 1..9 it spells the digit; otherwise it returns str(value).
- **How the mutation triggers**: Reverse-applying the patch tightens the guard back to `0 < value < 10` and removes 'zero' from the tuple. apnumber(0) then falls through to `return str(value)` and yields '0'.

### 2. intcomma_ndigits_zero

- **Variant**: `intcomma_ndigits_zero_03863fe_1`
- **Location**: `src/humanize/number.py:164` (inside `intcomma`)
- **Property**: `IntcommaNdigitsZeroRounds`
- **Witness(es)**:
  - `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` — intcomma(1234.5454545, 0) must round to '1,235'
- **Source**: internal — Fix intcomma with ndigits=0
  > intcomma(value, ndigits=0) used to skip the rounding branch (`if ndigits:` treats 0 as falsy) and emit the raw float repr. The fix uses `if ndigits is not None` so ndigits=0 rounds to integer.
- **Fix commit**: `03863fed6c2ba02cfd13d5b1e0b161f680c7b966` — Fix intcomma with ndigits=0
- **Invariant violated**: intcomma(value, 0) on a finite numeric value returns a string with no decimal separator: ndigits=0 means round-to-integer.
- **How the mutation triggers**: Reverse-applying the patch flips `if ndigits is not None:` back to `if ndigits:`, so 0 is treated as 'unspecified' and intcomma(1234.5454545, 0) returns '1,234.5454545' instead of '1,235'.

### 3. intword_negative_no_sign

- **Variant**: `intword_negative_no_sign_520aac1_1`
- **Location**: `src/humanize/number.py:239` (inside `intword`)
- **Property**: `IntwordPreservesSign`
- **Witness(es)**:
  - `witness_intword_preserves_sign_case_minus_million` — intword(-1_000_000) must start with '-'
- **Source**: internal — Fix intword for negative numbers
  > intword() used to ignore the sign on negative inputs above the thousand threshold; e.g. intword(-1_000_000) produced '1.0 million'. The fix records the sign before chopping and prepends a minus to the result.
- **Fix commit**: `520aac16c448f3cfd72f7c5812b04a3238e77bb4` — Fix intword for negative numbers
- **Invariant violated**: For any int value with value < 0 large enough to be humanized, intword(value) starts with '-'.
- **How the mutation triggers**: Reverse-applying the patch deletes the `if value < 0` block, so the negative_prefix is always '' and intword(-1_000_000) returns '1.0 million' instead of '-1.0 million'.

### 4. metric_zero_crash

- **Variant**: `metric_zero_crash_b1ee687_1`
- **Location**: `src/humanize/number.py:570` (inside `metric`)
- **Property**: `MetricFiniteOnZero`
- **Witness(es)**:
  - `witness_metric_finite_on_zero_case_zero` — metric(0) must not raise
- **Source**: internal — Fix metric(0) crash.
  > metric() used to call math.log10(abs(value)) directly, raising ValueError('math domain error') when value was 0. The fix short-circuits to exponent=0 in that branch.
- **Fix commit**: `b1ee6875820839a59f1b6f4a5fedc7cad8883834` — Fix metric(0) crash.
- **Invariant violated**: metric(value) returns a string for every finite value, including 0; it must not raise ValueError('math domain error').
- **How the mutation triggers**: Reverse-applying the patch removes the `if value != 0 else 0` guard; metric(0) then evaluates math.log10(0) and raises ValueError.

### 5. naturaldelta_negative_components

- **Variant**: `naturaldelta_negative_components_b939b2e_1`
- **Location**: `src/humanize/time.py:157` (inside `naturaldelta`)
- **Property**: `NaturaldeltaNegativeIsAbsolute`
- **Witness(es)**:
  - `witness_naturaldelta_negative_is_absolute_case_five_hours` — naturaldelta(-5h) must equal naturaldelta(+5h)
- **Source**: internal — Call abs on the whole datetime, not just parts
  > naturaldelta() used to call abs() on delta.days and delta.seconds independently. Python normalizes a negative timedelta to days=-1, seconds=86400-X — so the per-component absolute value yields '1 day' for what should be '5 hours'. The fix takes abs(delta) of the whole timedelta first.
- **Fix commit**: `b939b2e50ca7449f89b69d29a057886942e27b36` — Call abs on the whole datetime, not just parts
- **Invariant violated**: naturaldelta(td) == naturaldelta(-td) for any non-zero timedelta td.
- **How the mutation triggers**: Reverse-applying the patch swaps `delta = abs(delta)` for component-wise abs(delta.days), abs(delta.seconds). `naturaldelta(timedelta(hours=-5))` then returns '1 day, 19 hours' (or similar) rather than '5 hours'.

### 6. naturaldelta_subsecond

- **Variant**: `naturaldelta_subsecond_872d733_1`
- **Location**: `src/humanize/time.py:150` (inside `naturaldelta`)
- **Property**: `NaturaldeltaSubsecondsAreMilliseconds`
- **Witness(es)**:
  - `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` — naturaldelta(0.5, ms) must contain 'millisecond'
- **Source**: internal — Use float to support sub-second precision
  > naturaldelta(value) used to cast value to int before constructing the timedelta. Sub-second floats (e.g. 0.5) became 0, so naturaldelta(0.5, minimum_unit='milliseconds') returned 'a moment'. The fix casts to float so the timedelta keeps the microsecond component.
- **Fix commit**: `872d7331fe3e307d3cc682d422f51f2de13c0fa7` — Use float to support sub-second precision
- **Invariant violated**: For 0.001 <= seconds < 1, naturaldelta(seconds, minimum_unit='milliseconds') contains 'millisecond' (not 'a moment').
- **How the mutation triggers**: Reverse-applying the patch flips `value = float(value)` back to `value = int(value)`. naturaldelta(0.5, minimum_unit='milliseconds') then returns 'a moment' because the sub-second component is truncated to 0.

### 7. naturalsize_float_int_cast

- **Variant**: `naturalsize_float_int_cast_11e62ee_1`
- **Location**: `src/humanize/filesize.py:97` (inside `naturalsize`)
- **Property**: `NaturalsizeIntForSmallFloats`
- **Witness(es)**:
  - `witness_naturalsize_int_for_small_floats_case_500_float` — naturalsize(500.0) must equal '500 Bytes'
- **Source**: internal — Fix regression in naturalsize for float
  > naturalsize(value) on a sub-base float (e.g. 500.0) used to render as '500.0 Bytes' because the sub-base branch interpolated the raw float. The fix casts to int(bytes_) so the integer suffix matches integer inputs.
- **Fix commit**: `11e62eeedb8990298c3612af82376dc2344d24f8` — Fix regression in naturalsize for float
- **Invariant violated**: naturalsize(v) on a finite float v with 1 < |v| < base and v == int(v) does not contain a decimal separator.
- **How the mutation triggers**: Reverse-applying the patch drops the `int(bytes_)` cast in the sub-base branch and naturalsize(500.0) returns '500.0 Bytes' instead of '500 Bytes'.
