import sys


def Count(X):
    return(-X[0], X[1])
text = sys.stdin.read().split()
Letters = dict()
Answer = []
for word in text:
    Letters[word] = Letters.get(word, 0) + 1
for c in sorted(Letters):
    Answer.append((Letters[c], c))
Answer.sort(key=Count)
for i in Answer:
    print(i[1])
