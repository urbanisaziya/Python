intList = list(map(int, input().split()))
count = 0
for i in range(len(intList)):
    if intList[i] > 0:
        count += 1
print(count)
