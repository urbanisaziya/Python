A = list(map(int, input().split()))
i = len(A) - 1
while i != 0:
    A[i], A[i - 1] = A[i - 1], A[i]
    i -= 1
print(*A)
