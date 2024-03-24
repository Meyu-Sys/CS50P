from working import convert
import pytest

def test_convert():
    assert convert("1:30 PM to 2:00 PM") == "13:30 to 14:00"
    assert convert("1:30 PM to 2:00 AM") == "13:30 to 02:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    with pytest.raises(ValueError):
        convert("13:30 PM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("1:60 PM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("1:30 PM 2:60 PM")
    with pytest.raises(ValueError):
        convert("1:30 PM to 2:00")