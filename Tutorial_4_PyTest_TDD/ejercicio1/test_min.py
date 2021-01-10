import pytest
from min import minimun

def test_numberToRoman():
    num = [1,2,3,4,5,6,7,8,9,10]
    assert minimun(num) == 1
