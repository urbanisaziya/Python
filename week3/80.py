a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
elif b == 0:
    x = e / a
    y = (f - c * x) / d
elif e == 0:
    x = - b
    y = a
elif c == 0:
    y = f / d
    x = (e - b * y) / a
elif d == 0:
    x = f / c
    y = (e - a * y) / b
elif f == 0:
    x = - d
    y = c
else:
    y = (f * a - c * e)/(a * d - c * b)
    x = (e - b * y) / a
print(x, y)
