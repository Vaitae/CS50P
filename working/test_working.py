from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_hr()
    test_min()

def test_format():
    with pytest.raises(ValueError):
        convert('12 AM - 12 PM')

def test_time():
    assert convert('9 AM to 5 PM')=='09:00 to 17:00'
    assert convert('10 AM to 8:50 PM')=='10:00 to 20:50'
    assert convert('10:30 PM to 8 AM')=='22:30 to 08:00'

def test_hr():
    with pytest.raises(ValueError):
        convert('13 PM to 16 PM')

def test_min():
    with pytest.raises(ValueError):
        convert('5:60 AM to 9:60 PM')

if __name__=="__main__":
    main()
