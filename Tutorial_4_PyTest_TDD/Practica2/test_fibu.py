import pytest
from fibu import fibus

def test_fibu():
    num = 10
    assert fibus(num) == [ "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]

