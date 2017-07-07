a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and b == 0 and c == 0 and d == 0:
    if e == 0 and f == 0:
        print(5)
    else:
        print(0)
elif a == 0 and b == 0:
    print(0)
elif c == 0 and d == 0:
    print(0)
elif a == 0 and c == 0:
    y = e / b
    print(4, y)
elif a == 0 and d == 0:
    x = f / c
    y = e / b
    print(2, x, y)
elif a == 0:
    y = e / b
    x = (f - d * y) / c
    print(2, x, y)
elif b == 0 and c == 0:
    x = e / a
    y = f / d
    print(2, x, y)
elif b == 0 and d == 0:
    x = e / a
    print(3, x)
elif b == 0:
    x = e / a
    y = (f - c * x) / d
    print(2, x, y)
elif c == 0:
    y = f / d
    x = (e - b * y) / a
    print(2, x, y)
elif d == 0:
    x = f / c
    y = (e - a * x) / b
    print(2, x, y)
elif a * d - c * b == 0:
    p = -a / b
    q = e / b
    print(1, p, q)
elif e == 0:
    x = - b
    y = a
    print(2, x, y)
elif f == 0:
    x = - d
    y = c
    print(2, x, y)
else:
    y = (f * a - c * e)/(a * d - c * b)
    x = (e - b * y) / a
    print(2, x, y)
#not work