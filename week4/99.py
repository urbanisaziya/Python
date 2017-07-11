def IsPointInCircle(x, y, xc, yc, r):
    a = x - xc
    b = y - yc
    if (a ** 2 + b ** 2) ** (1/2) <= r:
        return True
    return False
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
