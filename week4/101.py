def xor(x, y):
    if x == 1 and y == 1:
        return False
    elif x == 1 or y == 1:
        return True
    return False
x = float(input())
y = float(input())
if xor(x, y):
    print('1')
else:
    print('0')
