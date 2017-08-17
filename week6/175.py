oneList = list(map(int, input().split()))
twoList = list(map(int, input().split()))
oneList.sort()
twoList.sort(reverse=True)
sumTax = 0
for i in range(len(oneList)):
    b = oneList[i] * twoList[i]
    sumTax += b
print(sumTax)
