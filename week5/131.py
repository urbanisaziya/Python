intList = list(map(int, input().split()))
for i in range(len(intList)):
    if intList[i] % 2 == 0:
        print(intList[i], end=' ')
