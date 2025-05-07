from numb3rs import validate

def test1():
    assert validate("512.512.1000.1000") == False
    assert validate("1.2.3.4")==True
    assert validate("1.2.3")==False
    assert validate("1.2")==False
    assert validate("1")==False

def test2():
    assert validate("250.75.36.55") == True

def test3():
    assert validate("255.256.257.258") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
