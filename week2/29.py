x = int(input())
y = int(input())
N = y - x + 1
M = x - 1
if M % N == 0:
    print("YES")
else:
    print("NO")
