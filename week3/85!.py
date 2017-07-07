s = input()
s1 = s.find('h')
s2 = s.rfind('h')
s3 = s[s1+1:s2]
h = (s.replace(s[s2:], s3))
print(h, s[s2:], sep='')
#not work?