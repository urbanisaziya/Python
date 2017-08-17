def Intersection(X, Y):
    C = []
    i = 0
    j = 0
    lA = len(A)
    lB = len(B)
    while i < lA and j < lB:
        if A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
            j += 1
    print(*C)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Intersection(A, B)
