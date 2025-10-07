# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import pytest
from app.operations import operation_factory, OperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 1, 2, 3),
    ("sub", 3, 1, 2),
    ("mul", 2, 4, 8),
    ("div", 8, 2, 4),
    ("pow", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_operations(op, a, b, expected):
    strat = operation_factory(op)
    assert strat.execute(a, b) == expected

def test_division_by_zero():
    with pytest.raises(OperationError):
        operation_factory("div").execute(1, 0)

def test_unknown_operation():
    with pytest.raises(OperationError):
        operation_factory("nope")

def test_root_zero_degree_and_negative_base():
    from app.operations import Root, OperationError
    with pytest.raises(OperationError):
        Root().execute(4, 0)
    # negative number fractional root triggers error
    with pytest.raises(OperationError):
        Root().execute(-9, 2)

def test_pow_and_root_validations():
    from app.operations import Pow, Root, OperationError
    assert Pow().execute(2, 3) == 8
    with pytest.raises(OperationError):
        Root().execute(9, 0)


def test_root_negative_odd_degree_and_pow():
    """Covers Root negative odd degree and Pow edge."""
    from app.operations import Root, Pow, OperationError

    # negative odd degree root should work fine
    assert round(Root().execute(-8, 3), 5) == -2.0

    # zero degree still raises error
    with pytest.raises(OperationError):
        Root().execute(9, 0)

    # pow still returns valid value
    assert Pow().execute(2, 3) == 8
