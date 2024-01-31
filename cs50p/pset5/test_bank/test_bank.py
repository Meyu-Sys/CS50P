from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello!") == 0
    assert value("Hello, world!") == 0

def test_h():
    assert value("H") == 20
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("Howdy") == 20

def test_other():
    assert (value("Welcome") == 100)
    assert (value("What's Up") == 100)
    assert (value("Good Morning") == 100)