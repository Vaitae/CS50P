import pytest
from plates import is_valid

def test_error():
    with pytest.raises(TypeError):
        is_valid()

def test_two_letters():
    assert is_valid("0A")==False
    assert is_valid("A0")==False
    assert is_valid("AA")==True
    assert is_valid("00")==False

def test_min_max_len():
    assert is_valid("flower")==True
    assert is_valid("h")==False
    assert is_valid("flowers")==False

def test_num_in_middle():
    assert is_valid("AA3AA")==False
    assert is_valid("AAA22A")==False
    assert is_valid("abcdef")==True
    assert is_valid("AAA222")==True

def test_startswith_zero():
    assert is_valid("0")==False
    assert is_valid("0hello")==False

def test_punctuation():
    assert is_valid("to you")==False
    assert is_valid("Hello!")==False
    assert is_valid("PI3.14")==False
    assert is_valid("you-")==False

def test_zero_place():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False

def test_begins_without_letters():
    assert is_valid("5")==False
    assert is_valid("22")==False
