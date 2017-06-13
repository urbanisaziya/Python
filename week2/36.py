import math
a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == max(a, b, c):
        if a**2 == (b**2 + c**2):
            print("rectangular")
        elif a**2 < (b**2 + c**2):
            print("acute")
        else:
            print("obtuse")
    elif b == max(a, b, c):
        if b**2 == (a**2 + c**2):
            print("rectangular")
        elif b**2 < (a**2 + c**2):
            print("acute")
        else:
            print("obtuse")
    elif c == max(a, b, c):
        if c**2 == (b**2 + a**2):
            print("rectangular")
        elif c**2 < (b**2 + a**2):
            print("acute")
        else:
            print("obtuse")
else:
    print("impossible")
