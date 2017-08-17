def CountSort(A):
    a = max(A) + 1
    B = [0] * a
    for now in A:
        B[now] += 1
    for i in range(len(B)):
        for x in range(B[i]):
            print(i, end=' ')
A = list(map(int, input().split()))
CountSort(A)
