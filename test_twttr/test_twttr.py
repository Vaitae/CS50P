from twttr import shorten
import pytest

def test_error():
    with pytest.raises(TypeError):
        shorten()

def test_uppercase_vowels():
    assert shorten("ADIEU")=="D"

def test_lowercase_vowels():
    assert shorten("adieu")=="d"

def test_str():
    assert shorten("Hello")=="Hll"
    assert shorten("Hello there")=="Hll thr"

def test_numbers():
    assert shorten("1234")=="1234"
    assert shorten("12.34")=="12.34"

def test_symbols():
    assert shorten("/!.-")=="/!.-"
