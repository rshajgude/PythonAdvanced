
import pytest

def multiply_2_num(a,b):
    return a*b

def multiply_3_num(a,b,c):
    return a*b**c

def division_2_num(a,b):
    if b==0:
        raise ValueError("Dinominator chan't be 0")
    return a/b

def test_multiply():
    assert multiply_2_num(3,7) == 21
    assert multiply_2_num(9, 12) == 108

def test_multiply_3_num():
    assert multiply_3_num(2,3,4) == 24

def test_division_2_num():
    assert division_2_num(4,2) == 2
    assert division_2_num(12,2) == 6
    with pytest.raises(Exception):
        division_2_num(12, 0)

