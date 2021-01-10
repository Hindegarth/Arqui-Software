def fibus(num):
    ans = []
    for i in range(1, num+1):
        fb = ""
        if not (i % 3):
            fb += "Fizz"
        if not (i % 5):
            fb += "Buzz"
        if not fb:
            ans.append(str(i))
        else:
            ans.append(fb)
    return ans
