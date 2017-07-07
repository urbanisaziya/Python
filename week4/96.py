def length(x1, y1, x2, y2):
    sqrSum = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return sqrSum ** (1 / 2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
A = length(x1, y1, x2, y2)
B = length(x2, y2, x3, y3)
C = length(x1, y1, x3, y3)
Sum = A + B + C
print(Sum)
