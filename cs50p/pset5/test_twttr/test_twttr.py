from twttr import shorten
import pytest

def test_yolo():
    assert shorten("yolo") == "yl"
def test_twitter():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Alphabet") == "lphbt"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
