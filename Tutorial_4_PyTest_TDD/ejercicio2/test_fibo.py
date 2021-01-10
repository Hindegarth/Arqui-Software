import pytest
from fibo import fibonacci

def test_fibonacci():
    num = 10
    assert fibonacci(num) == 55
