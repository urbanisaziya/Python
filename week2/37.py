A = int(input())
B = int(input())
C = int(input())
if (A + B + C) % 2 == 0:
    if (A % 2 == 0) and (B % 2 == 0) and (C % 2 == 0):
        print("NO")
    else:
        print("YES")
elif (A % 2 == 1) and (B % 2 == 1) and (C % 2 == 1):
    print("NO")
else:
    print("YES")
