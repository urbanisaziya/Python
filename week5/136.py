A = list(map(int, input().split()))
for i in range(1, len(A)):
    if A[i - 1] > 0 and A[i] > 0:
        a = A[i - 1]
        b = A[i]
        print(a, b, end=' ')
        break
    if A[i - 1] < 0 and A[i] < 0:
        c = A[i - 1]
        d = A[i]
        print(c, d, end=' ')
        break
