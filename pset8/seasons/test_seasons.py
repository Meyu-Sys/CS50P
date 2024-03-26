from seasons import calc
from datetime import date

def test_calc():
    assert calc(date(2000, 1, 1), date(2000, 1, 2)) == 1440
    assert calc(date(2000, 1, 1), date(2000, 1, 1)) == 0
    assert calc(date(1999,8,2), date(2000,12,19)) == 727200