import jar
import pytest

def test_init():
    j = jar.Jar(12)
    assert j.cap == 12
    with pytest.raises(ValueError):
        jar.Jar(-1)

def test_deposit():
    j = jar.Jar(12)
    j.deposit(3)
    assert j.num == 3
    with pytest.raises(ValueError):
        j.deposit(10)

def test_withdraw():
    j = jar.Jar(12)
    j.deposit(3)
    j.withdraw(2)
    assert j.num == 1
    with pytest.raises(ValueError):
        j.withdraw(2)

def test_str():
    j = jar.Jar(12)
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"
    j.deposit(2)
    assert str(j) == "🍪🍪🍪🍪🍪"

