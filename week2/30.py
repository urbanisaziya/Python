import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if (math.fabs(A - C) + math.fabs(B - D)) % 2 == 0:
    print("YES")
else:
    print("NO")