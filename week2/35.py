import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
M = C - A
N = D - B
if ((C + D) > (A + B)) and ((math.fabs(M) + math.fabs(N)) % 2 == 0):
    print("YES")
else:
    print("NO")
