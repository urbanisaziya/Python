A = int(input())
B = int(input())
C = int(input())
if A == B == C:
    print(3)
elif (A == B) or (B == C) or (C == A):
    print(2)
else:
    print(0)
