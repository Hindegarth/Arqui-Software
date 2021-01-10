import pytest
from roman import numRoman, romanNum

def test_numberToRoman():
    num = 15
    assert numRoman(num) == "XV"

def test_romanToNumber():
    roman = "XV"
    assert romanNum(roman) == 15

