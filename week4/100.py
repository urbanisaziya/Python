def IsPointInArea(x, y):
    xc = -1
    yc = 1
    r = 2
    y1 = -1 * x
    y2 = 2 * x + 2
    dist = ((x - xc) ** 2 + (y - yc) ** 2) ** (1 / 2)
    if (y >= y1 and y >= y2 and dist <= r):
        return True
    elif (y <= y1 and y <= y2 and dist >= r):
        return True
    return False
x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
