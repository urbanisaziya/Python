s = input()
s1 = s.find('f')
s2 = s.rfind('f')
if s1 != -1 and s2 != -1:
    if s1 == s2:
        print(s1)
    else:
        print(s1, s2)
