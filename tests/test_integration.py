from roman.converter import (
    add_roman,
    from_roman,
    is_valid_roman,
    subtract_roman,
)


def test_add_roman_returns_canonical_and_valid_result():
    result = add_roman("II", "II")

    assert result == "IV"
    assert from_roman(result) == 4
    assert is_valid_roman(result) is True


def test_subtract_roman_returns_canonical_and_valid_result():
    result = subtract_roman("X", "I")

    assert result == "IX"
    assert from_roman(result) == 9
    assert is_valid_roman(result) is True