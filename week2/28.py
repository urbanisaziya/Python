import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if math.fabs(A - C) <= 1 and math.fabs(B - D) <= 1:
    print("YES")
else:
    print("NO")
