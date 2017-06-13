N = int(input())
i = 0
while 2**i < N:
    i = i + 1
if 2**i == N:
    print("YES")
else:
    print("NO")
