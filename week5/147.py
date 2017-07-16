A = list(map(int, input().split()))
i = 0
k = 1
while i < len(A):
    if A[i] > A[i - 1]:
        k += 1
    i += 1
print(k)
