from um import count

def test_count():
    assert count("um") == 1
    assert count("umum") == 0
    assert count("um um") == 2
    assert count("um, um") == 2
    assert count("Um, thanks, um...") == 2