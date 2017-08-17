fin = open('input.txt', 'r', encoding='utf8')
class9 = []
class10 = []
class11 = []
for line in fin:
    a = line.split()
    b = int(a[-1])
    if a[-2] == '9':
        class9.append(int(a[-1]))
    elif a[-2] == '10':
        class10.append(int(a[-1]))
    elif a[-2] == '11':
        class11.append(int(a[-1]))
class9.sort()
class10.sort()
class11.sort()
a, b, c = max(class9), max(class10), max(class11)
x, y, z = len(class9), len(class10), len(class11)
while x > 0:
    if class9[x - 1] == a:
        x -= 1
    else:
        print(class9[x - 1], end=' ')
        break
while y > 0:
    if class10[y - 1] == b:
        y -= 1
    else:
        print(class10[y - 1], end=' ')
        break
while z > 0:
    if class11[z - 1] == c:
        z -= 1
    else:
        print(class11[z - 1])
        break
