k = int(input())
a = k - 3*2
b = k - 5*2
if (k % 3 == 0) or (k % 5 == 0):
    print("YES")
elif (a > 0 and a % 5 == 0) or (b > 0 and b % 3 == 0):
    print("YES")
else:
    print("NO")
