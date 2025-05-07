from um import count

def main():
    test_word_with_um()
    test_um_surrounded_by_space()
    test_case_insensitive_check()

def test_word_with_um():
    assert count("yummy")==0
    assert count("Plum")==0

def test_case_insensitive_check():
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2

def test_um_surrounded_by_space():
    assert count('Hello um world')==1
    assert count('um?')==1

if __name__=="__main__":
    main()
