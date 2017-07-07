import math
n = int(input())
Sum = n
Sqr = n ** 2
i = 0
while n != 0:
    n = int(input())
    Sum = Sum + n
    Sqr = Sqr + n ** 2
    i += 1
st = math.sqrt((Sqr - (Sum ** 2 / i)) / (i - 1))
print(st)
