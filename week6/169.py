fin = open('input.txt', 'r', encoding='utf8')
max9 = 0
max10 = 0
max11 = 0
for line in fin:
    a = line.split()
    b = int(a[-1])
    if a[-2] == '9':
        if b > max9:
            max9 = b
    elif a[-2] == '10':
        if b > max10:
            max10 = b
    elif a[-2] == '11':
        if b > max11:
            max11 = b
print(max9, end=' ')
print(max10, end=' ')
print(max11, end='')
