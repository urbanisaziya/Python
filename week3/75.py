P = float(input())
X = float(input())
Y = float(input())
K = int(input())
i = 1
summa = X + Y / 100
percent = (P / 100) 
while i <= K:
    summa = (summa + percent*summa)
    i +=1
    print(summa)
print(summa)
rub = round(summa // 1)
kop = round((summa % 1) * 100)
print(rub, kop)
#not work