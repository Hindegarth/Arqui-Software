def minimun(num):
    ans = num[0]
    for i in range(len(num)-1):
        if (ans > num[i]):
             ans = num[i]
    return ans
