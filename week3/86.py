s = input()
pos = 0
d = 0
l = len(s)
if s.find('f') == -1:
    print(-2)
else:
    while s.find('f', pos) != -1:
        if s.find('f', pos) != -1:
            pos = s.find('f', pos) + 1
            d += 1
            if d == 2:
                print(pos - 1)
    if d == 1:
        print(-1)
