s = input()
t = ''
pos = 0
while pos != len(s):
    if pos % 3 != 0:
        t = t + s[pos]
    pos += 1
print(t)
