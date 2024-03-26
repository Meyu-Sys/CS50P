from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    pytest.raises(ZeroDivisionError, convert, "1/0")
    pytest.raises(ValueError, convert, "2/1")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(49) == "49%"
    assert gauge(50) == "50%"
    assert gauge(51) == "51%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
