import pytest
from fuel import convert, gauge

def test_error():
    with pytest.raises(TypeError):
        convert()

def test_correct_output():
    assert convert("3/4")==75 and gauge(75)=="75%"
    assert convert("1/100")==1 and gauge(1)=="E"
    assert convert("99/100")==99 and gauge(99)=="F"

def test_ZeroDivError():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_value_str_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

