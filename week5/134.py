A = list(map(int, input().split()))
for i in range(1, len(A)):
    if A[i - 1] < A[i]:
        print(A[i], end=' ')
