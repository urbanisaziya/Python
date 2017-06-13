N = int(input())
k = 0
while 2**k < N:
    k = k + 1
if 2**k >= N:
    print(k)
