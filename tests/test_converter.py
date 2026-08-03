# test suite
import pytest
from roman.converter import (
    RomanError,
    add_roman,
    from_roman,
    is_valid_roman,
    subtract_roman,
    to_roman,
)


def test_one():
    assert to_roman(1) == "I"


def test_two():
    assert to_roman(2) == "II"


def test_three():
    assert to_roman(3) == "III"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_five_hundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_from_one():
    assert from_roman("I") == 1


def test_from_five():
    assert from_roman("V") == 5


def test_from_two():
    assert from_roman("II") == 2


def test_roundtrip_small():
    assert from_roman(to_roman(7)) == 7


def test_roundtrip_medium():
    assert from_roman(to_roman(58)) == 58


def test_lowercase_input():
    assert from_roman("xi") == 11

def test_to_roman_rejects_non_integer():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman("10")


def test_to_roman_rejects_boolean():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman(True)


def test_to_roman_rejects_value_below_range():
    with pytest.raises(RomanError, match="value must be >= 1"):
        to_roman(0)


def test_to_roman_rejects_value_above_range():
    with pytest.raises(RomanError, match="value must be <= 3999"):
        to_roman(4000)


def test_to_roman_executes_multiple_loop_iterations():
    assert to_roman(3888) == "MMMDCCCLXXXVIII"


def test_from_roman_rejects_non_string():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(10)


def test_from_roman_rejects_empty_string():
    with pytest.raises(RomanError, match="empty string"):
        from_roman("")


def test_from_roman_rejects_invalid_character():
    with pytest.raises(RomanError, match="invalid roman character"):
        from_roman("A")


def test_from_roman_accepts_valid_subtractive_pair():
    assert from_roman("IX") == 9


def test_from_roman_rejects_invalid_subtractive_pair():
    with pytest.raises(RomanError, match="invalid subtractive pair"):
        from_roman("IL")


def test_from_roman_rejects_total_above_range():
    with pytest.raises(RomanError, match="value out of range"):
        from_roman("MMMM")


def test_is_valid_roman_true_and_false():
    assert is_valid_roman("X") is True
    assert is_valid_roman("A") is False


def test_add_roman_combines_conversion_functions():
    assert add_roman("I", "I") == "II"


def test_subtract_roman_combines_conversion_functions():
    assert subtract_roman("II", "I") == "I"