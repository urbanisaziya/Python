def Count(X):
    return(-X[0], X[1])
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
Letters = dict()
Answer = []
for line in fin:
    line = line.strip()
    Letters[line] = Letters.get(line, 0) + 1
a = sum(Letters.values())
for c in sorted(Letters):
    Answer.append((Letters[c], c))
Answer.sort(key=Count)
if Answer[0][0] / a > 0.5:
    print(Answer[0][1], file=fout)
else:
    for i in Answer[:2]:
        print(i[1], file=fout)
