n = int(input())
oneList = list(map(int, input().split()))
k = int(input())
twoList = list(map(int, input().split()))
key = [0] * k
for now in twoList:
    key[now] += 1
key.pop(0)
for x in range(n):
    if oneList[x] < key[x]:
        print('YES')
    else:
        print('NO')
