N = input()
if int(N) == 0:
    print(1)
elif len(N) == 4 and N[0] == N[3] and N[1] == N[2]:
    print(1)
elif len(N) == 3 and N[0] == N[1] and int(N[2]) == 0:
    print(1)
else:
    print(2)
