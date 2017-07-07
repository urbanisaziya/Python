s = input()
s1 = s.find('h')
s2 = s.rfind('h')
s3 = s[s1:s2+1]
print(s.replace(s3, ''))
