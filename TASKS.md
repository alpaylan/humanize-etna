# humanize — ETNA Tasks

Total tasks: 28

## Task Index

| Task | Variant | Framework | Property | Witness |
|------|---------|-----------|----------|---------|
| 001 | `apnumber_zero_off_by_one_2f179b6_1` | proptest | `ApnumberZeroIsZero` | `witness_apnumber_zero_is_zero_case_zero` |
| 002 | `apnumber_zero_off_by_one_2f179b6_1` | quickcheck | `ApnumberZeroIsZero` | `witness_apnumber_zero_is_zero_case_zero` |
| 003 | `apnumber_zero_off_by_one_2f179b6_1` | crabcheck | `ApnumberZeroIsZero` | `witness_apnumber_zero_is_zero_case_zero` |
| 004 | `apnumber_zero_off_by_one_2f179b6_1` | hegel | `ApnumberZeroIsZero` | `witness_apnumber_zero_is_zero_case_zero` |
| 005 | `intcomma_ndigits_zero_03863fe_1` | proptest | `IntcommaNdigitsZeroRounds` | `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` |
| 006 | `intcomma_ndigits_zero_03863fe_1` | quickcheck | `IntcommaNdigitsZeroRounds` | `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` |
| 007 | `intcomma_ndigits_zero_03863fe_1` | crabcheck | `IntcommaNdigitsZeroRounds` | `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` |
| 008 | `intcomma_ndigits_zero_03863fe_1` | hegel | `IntcommaNdigitsZeroRounds` | `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` |
| 009 | `intword_negative_no_sign_520aac1_1` | proptest | `IntwordPreservesSign` | `witness_intword_preserves_sign_case_minus_million` |
| 010 | `intword_negative_no_sign_520aac1_1` | quickcheck | `IntwordPreservesSign` | `witness_intword_preserves_sign_case_minus_million` |
| 011 | `intword_negative_no_sign_520aac1_1` | crabcheck | `IntwordPreservesSign` | `witness_intword_preserves_sign_case_minus_million` |
| 012 | `intword_negative_no_sign_520aac1_1` | hegel | `IntwordPreservesSign` | `witness_intword_preserves_sign_case_minus_million` |
| 013 | `metric_zero_crash_b1ee687_1` | proptest | `MetricFiniteOnZero` | `witness_metric_finite_on_zero_case_zero` |
| 014 | `metric_zero_crash_b1ee687_1` | quickcheck | `MetricFiniteOnZero` | `witness_metric_finite_on_zero_case_zero` |
| 015 | `metric_zero_crash_b1ee687_1` | crabcheck | `MetricFiniteOnZero` | `witness_metric_finite_on_zero_case_zero` |
| 016 | `metric_zero_crash_b1ee687_1` | hegel | `MetricFiniteOnZero` | `witness_metric_finite_on_zero_case_zero` |
| 017 | `naturaldelta_negative_components_b939b2e_1` | proptest | `NaturaldeltaNegativeIsAbsolute` | `witness_naturaldelta_negative_is_absolute_case_five_hours` |
| 018 | `naturaldelta_negative_components_b939b2e_1` | quickcheck | `NaturaldeltaNegativeIsAbsolute` | `witness_naturaldelta_negative_is_absolute_case_five_hours` |
| 019 | `naturaldelta_negative_components_b939b2e_1` | crabcheck | `NaturaldeltaNegativeIsAbsolute` | `witness_naturaldelta_negative_is_absolute_case_five_hours` |
| 020 | `naturaldelta_negative_components_b939b2e_1` | hegel | `NaturaldeltaNegativeIsAbsolute` | `witness_naturaldelta_negative_is_absolute_case_five_hours` |
| 021 | `naturaldelta_subsecond_872d733_1` | proptest | `NaturaldeltaSubsecondsAreMilliseconds` | `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` |
| 022 | `naturaldelta_subsecond_872d733_1` | quickcheck | `NaturaldeltaSubsecondsAreMilliseconds` | `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` |
| 023 | `naturaldelta_subsecond_872d733_1` | crabcheck | `NaturaldeltaSubsecondsAreMilliseconds` | `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` |
| 024 | `naturaldelta_subsecond_872d733_1` | hegel | `NaturaldeltaSubsecondsAreMilliseconds` | `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` |
| 025 | `naturalsize_float_int_cast_11e62ee_1` | proptest | `NaturalsizeIntForSmallFloats` | `witness_naturalsize_int_for_small_floats_case_500_float` |
| 026 | `naturalsize_float_int_cast_11e62ee_1` | quickcheck | `NaturalsizeIntForSmallFloats` | `witness_naturalsize_int_for_small_floats_case_500_float` |
| 027 | `naturalsize_float_int_cast_11e62ee_1` | crabcheck | `NaturalsizeIntForSmallFloats` | `witness_naturalsize_int_for_small_floats_case_500_float` |
| 028 | `naturalsize_float_int_cast_11e62ee_1` | hegel | `NaturalsizeIntForSmallFloats` | `witness_naturalsize_int_for_small_floats_case_500_float` |

## Witness Catalog

- `witness_apnumber_zero_is_zero_case_zero` — apnumber(0) must be 'zero'
- `witness_intcomma_ndigits_zero_rounds_case_thousand_decimal` — intcomma(1234.5454545, 0) must round to '1,235'
- `witness_intword_preserves_sign_case_minus_million` — intword(-1_000_000) must start with '-'
- `witness_metric_finite_on_zero_case_zero` — metric(0) must not raise
- `witness_naturaldelta_negative_is_absolute_case_five_hours` — naturaldelta(-5h) must equal naturaldelta(+5h)
- `witness_naturaldelta_subseconds_are_milliseconds_case_half_second` — naturaldelta(0.5, ms) must contain 'millisecond'
- `witness_naturalsize_int_for_small_floats_case_500_float` — naturalsize(500.0) must equal '500 Bytes'
