A = list(map(int, input().split()))
a = min(A)
b = max(A)
k = A.index(a)
l = A.index(b)
A[k], A[l] = A[l], A[k]
print(*A)
