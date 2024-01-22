from twttr import shorten

def test_yolo():
    assert shorten("yolo") == "yl"
    assert shorten("Twitter") == "twttr"