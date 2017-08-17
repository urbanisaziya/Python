def merge(X, Y):
    C = []
    i = 0
    j = 0
    lA = len(A)
    lB = len(B)
    while i < lA or j < lB:
        if i >= lA:
            C.append(B[j])
            j += 1
        elif j >= lB:
            C.append(A[i])
            i += 1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    print(*C)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
merge(A, B)
