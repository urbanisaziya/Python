import math
H = int(input())
A = int(input())
B = int(input())
c = ((H - A) / (A - B)) + 1
print(math.ceil(c))
