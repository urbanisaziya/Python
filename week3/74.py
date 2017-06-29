P = float(input())
X = float(input())
Y = float(input())
summa = X + Y / 100
percent = ((P / 100) * summa)
vklad = round((summa + percent), 2)
rub = round(vklad // 1)
kop = round((vklad % 1) * 100)
print(rub, kop)
#not work