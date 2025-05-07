from seasons import check_birthdate

def main():
    test_check_birthdate()

def test_check_birthdate():
    assert check_birthdate('2012-12-12')==('2012','12','12')
    assert check_birthdate('2000-1-1')==None
    assert check_birthdate('January 1, 2000')==None

if __name__=="__main__":
    main()
