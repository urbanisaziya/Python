s = input()
s1 = s[1:-1]
s2 = (s1.replace('', '*'))
if len(s) == 1:
    print(s)
else:
    print(s[0], s2, s[-1], sep='')
