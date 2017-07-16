A = list(map(int, input().split()))
i = 0
while i < len(A) - 1:
    A[i], A[i + 1] = A[i + 1], A[i]
    i += 2
print(*A)
