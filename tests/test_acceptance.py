import pytest

from roman.converter import (
    RomanError,
    from_roman,
    is_valid_roman,
)


def test_acceptance_trims_leading_and_trailing_whitespace():
    """
    Given a valid canonical Roman numeral with outer whitespace
    When the user converts it using from_roman
    Then the system returns the corresponding integer
    """
    assert from_roman("  IV  ") == 4


def test_acceptance_rejects_noncanonical_roman_numeral():
    """
    Given the noncanonical Roman numeral IIII
    When the user attempts to convert it using from_roman
    Then the system raises RomanError
    """
    with pytest.raises(RomanError):
        from_roman("IIII")


def test_acceptance_validation_returns_false_for_non_string():
    """
    Given a value that is not a string
    When the user validates it using is_valid_roman
    Then the system returns False without raising an exception
    """
    assert is_valid_roman(123) is False