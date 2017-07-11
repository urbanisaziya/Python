n = int(input())
a, b, c = '+___ ', '|__\\ ', '|    '
print(a * n)
for i in range(n):
    print('|', i + 1, ' / ', sep='', end='')
print()
print(b * n)
print(c * n)
