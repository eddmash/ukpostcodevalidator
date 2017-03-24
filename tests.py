import unittest

import pytest

from ukpostcodevalidator import validator

def test_input_is_string():
    with pytest.raises(ValueError):
        validator.Uk.validate([])

@pytest.mark.parametrize("test_input,expected", [
    ("A9 9AA", True),
    ("AA9 9AA", True),
    ("AA9A 9AA", True),
    ("A9 9AA", True),
    ("A99 9AA", True),
    ("AA99 9AA", True),
])
def test_outward(test_input, expected):
    assert validator.Uk.validate(test_input) == expected