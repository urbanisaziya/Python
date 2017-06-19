N = int(input())
M = 0
n = N
if N < 10:
    print(N)
while N // 10 != 0:
    n = N % 10
    M = M * 10 + n
    N = N // 10
    if N // 10 == 0:
        print(M, N, sep='')
