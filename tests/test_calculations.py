# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import pytest
from app.calculation import Calculation

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 1, 2, 3),
    ("sub", 3, 1, 2),
    ("mul", 2, 4, 8),
])
def test_calc_execute(op, a, b, expected):
    assert Calculation(op, a, b).execute() == expected
