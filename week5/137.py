A = list(map(int, input().split()))
b = 0
for i in range(2, len(A)):
    if A[i - 2] < A[i - 1] and A[i] < A[i - 1]:
        b += 1
print(b)
