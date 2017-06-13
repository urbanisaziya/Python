import math
A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
V1 = A1 * B1 * C1
V2 = A2 * B2 * C2
min1 = min(A1, B1, C1)
min2 = min(A2, B2, C2)
max1 = max(A1, B1, C1)
max2 = max(A2, B2, C2)
mid1 = (A1 + B1 + C1 - min1 - max1)
mid2 = (A2 + B2 + C2 - min2 - max2)
if (V1 == V2):
    if ((min1 == min2) and (max1 == max2)):
        print("Boxes are equal")
    else:
        print("Boxes are incomparable")
elif (V1 > V2):
    if ((max1 >= max2) and (min1 >= min2) and (mid1 >= mid2)):
        print("The first box is larger than the second one")
    else:
        print("Boxes are incomparable")
elif (V1 < V2):
    if ((max1 <= max2) and (min1 <= min2) and (mid1 <= mid2)):
        print("The first box is smaller than the second one")
    else:
        print("Boxes are incomparable")
else:
    print("Boxes are incomparable")
