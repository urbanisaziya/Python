import math
N = int(input())
A = list(map(int, input().split()))
x = int(input())
i = 0
a = A[i]
b = math.fabs(A[i] - x)
while i < len(A):
    if math.fabs(A[i] - x) < b:
        a = A[i]
        b = math.fabs(A[i] - x)
    i += 1
print(a)
