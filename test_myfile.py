import pytest
from myfile import calculator


def test_addition():
    x = 1
    y = 2
    assert calculator(x,y,'+') == 3

def test_division():
    assert calculator(10,5,'/') == 2

def test_zero_division():
    with pytest.raises(ZeroDivisionError, match= "cannot divide by zero"):
        calculator(2,0,'/')         
