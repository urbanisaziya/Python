def IsPointInSquare(x, y):
    import math
    if x <= 1 and y <= 1 and x >= -1 and y >= -1:
        if math.fabs(x) + math.fabs(y) <= 1:
            return True
    return False
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
