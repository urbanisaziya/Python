import sys
text = sys.stdin.read().split()
Letters = dict()
for word in text:
    Letters[word] = Letters.get(word, 0) + 1
max_count = max(Letters.values())
print(min(i[0] for i in Letters.items() if i[1] == max_count))
