N = int(input())
H = N // 3600
M = (N - H * 3600) // 60
S = N - H * 3600 - M * 60
print(H % 24, ':', sep='', end='')
if int(M) < 10:
    print(0, M, ':', sep='', end='')
else:
    print(M, ':', sep='', end='')
if int(S) < 10:
    print(0, S, sep='', end='')
else:
    print(S)
