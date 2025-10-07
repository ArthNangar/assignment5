# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import pytest
from app.input_validators import parse_two_numbers
from app.exceptions import ValidationError

def test_parse_two_numbers_ok():
    assert parse_two_numbers(["add","1","2"]) == (1.0, 2.0)

@pytest.mark.parametrize("parts", [
    ["add","one","2"],
    ["add","1"],
    ["add"],
])
def test_parse_two_numbers_bad(parts):
    with pytest.raises(ValidationError):
        parse_two_numbers(parts)
