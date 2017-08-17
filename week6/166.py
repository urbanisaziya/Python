fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf-8')
spisok = []
for line in fin:
    a = line.split()
    a.pop(2)
    spisok.append(a)
spisok.sort()
for i in range(len(spisok)):
    a = spisok[i]
    print(*a, file=fout)
fin.close()
fout.close()
