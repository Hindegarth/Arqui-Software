import math

def is_prime(num):
    # Prime numbers must be greater than 1
    if num < 2:
        return False
    #Prime numbers mu
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

def suma(num):
    ans = 0
    for n in range(len(num)-1):
         if True == is_prime(num[n]):
               ans += num[n]
    return ans
