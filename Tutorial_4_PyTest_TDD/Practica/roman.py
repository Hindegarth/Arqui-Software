def numRoman(num):
    dicc = {
        1000: "M" ,
        900 : "CM",
        500 : "D" ,
        400 : "CD",
        100 : "C" ,
        90  : "XC",
        50  : "L" ,
        40  : "XL",
        10  : "X" ,
        9   : "IX",
        5   : "V" ,
        4   : "IV",
        1   : "I"
    }
    decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""
    while num > 0:
        if num < decimal[0]:
            decimal = decimal[1:]
        else:
            num -= decimal[0]
            ans += dicc[decimal[0]]
    return ans

def romanNum(roman):
    dicc = {
        "M"  : 1000,
        "CM" : 900 ,
        "D"  : 500 ,
        "CD" : 400 ,
        "C"  : 100 ,
        "XC" : 90  ,
        "L"  : 50  ,
        "XL" : 40  ,
        "X"  : 10  ,
        "IX" : 9   ,
        "V"  : 5   ,
        "IV" : 4   ,
        "I"  : 1
    }
    sections = []
    temp = ""
    for i in range(len(roman)-1):
        a = dicc[roman[i]]
        b = dicc[roman[i+1]]
        temp += roman[i]
        if a >= b:
            sections.append(temp)
            temp = ""
    ans = 0
    for sec in sections:
        print(sec)
        ans += dicc[sec]
    if temp:
        ans += dicc[roman[-2:]]
    else:
        ans += dicc[roman[-1]]
    return ans
