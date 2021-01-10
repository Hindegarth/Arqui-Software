import pytest
from primes import is_prime, suma

@pytest.mark.parametrize(
    "n, result",
    [([1,2,3,4,5,6,7,8,9,10], 17), ([1,2,5,8,3], 7 ), ([1,2,3,4,5,6,7,8,9,10,11,12,200,203], 28)]
)
def test_primes(n,result):

    
    assert suma(n) == result
    
