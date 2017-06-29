import math
a = float(input())
b = float(input())
c = float(input())
p = 0.5 * (a + b + c)
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)
