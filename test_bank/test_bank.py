from bank import value
import pytest

def test_error():
    with pytest.raises(TypeError):
        value()

def test_starts_with_hello():
    assert value("Hello")==0
    assert value("hello there")==0

def test_starts_with_h():
    assert value("hey there")==20
    assert value("Hey")==20

def test_other_Str():
    assert value("What's up?")==100
    assert value("1234")==100
    assert value("./-!")==100
