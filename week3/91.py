s = input()
s1 = s.find('h')
s2 = s.rfind('h')
s3 = s[s1+1:s2]
s4 = s3.replace('h', 'H')
print(s[:s1+1], s4, s[s2:], sep='')
