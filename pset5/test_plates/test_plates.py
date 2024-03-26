from plates import is_valid

def test_letters():
    assert is_valid("993") == False
    assert is_valid("AAB34") == True

def test_minmax():
    assert is_valid("A") == False
    assert is_valid("AA12345") == False
    assert is_valid("AA1234") == True
    assert is_valid("AA") == True

def test_alnum():
    assert is_valid("AA123!") == False
    assert is_valid("AA1234") == True
    assert is_valid("AA12a") == False
    assert is_valid("AA12a!") == False

def test_num():
    assert is_valid("AA0123") == False
    assert is_valid("AA1234") == True
    assert is_valid("AA123a") == False


