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
    ("AA99 9AC", False),
    ("AA99 9CI", False),
    ("AA99 9KA", False),
    ("AA99 9MA", False),
    ("AA99 9AV", False),
    ("A 9AA", False),
    ("A9I 9AA", False),
    ("A9L 9AA", False),
    ("A9M 9AA", False),
    ("A9N 9AA", False),
    ("A9O 9AA", False),
    ("A9Q 9AA", False),
    ("A9R 9AA", False),
    ("A9V 9AA", False),
    ("A9X 9AA", False),
    ("A9Y 9AA", False),
    ("A9Y 9AA", False),
    ("A9Y9AA", False),
    ("AA9C 9AA", False),
    ("AA9D 9AA", False),
    ("AA9F 9AA", False),
    ("AA9G 9AA", False),
    ("AA9I 9AA", False),
    ("AA9J 9AA", False),
    ("AA9K 9AA", False),
    ("AA9L 9AA", False),
    ("AA9O 9AA", False),
    ("AA9Q 9AA", False),
    ("AA9S 9AA", False),
    ("AA9T 9AA", False),
    ("AA9Z 9AA", False),
    ("QA9 9AA", False),
    ("VA9 9AA", False),
    ("XA9 9AA", False),
    ("AI9 9AA", False),
    ("AJ9 9AA", False),
    ("AZ9 9AA", False),
])
def test_postalcode_format(test_input, expected):
    """Tests the overall format of the codes"""
    assert validator.Uk.validate(test_input) == expected
