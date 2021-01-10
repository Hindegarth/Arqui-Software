import pytest
from pali import inverse

def test_inverse():
    carac = "ruby"
    assert inverse(carac) == "ybur"
