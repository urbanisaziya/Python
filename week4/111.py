def C(n, k):
    if n < k:
        return
    if k == 0:
        return 1
    if n == k or k == 1:
        return n - k + 1
    return C((n-1), k) + C((n-1), (k-1))
n = int(input())
k = int(input())
print(C(n, k))
