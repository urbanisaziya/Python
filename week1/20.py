N = int(input())
M = int(input())
a = M // N
if (M % N) > 0:
    print(a+1)
else:
    print(a)
