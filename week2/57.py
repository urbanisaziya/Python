n = int(input())
d = 0
seqSum = 0
while n != 0:
    seqSum += n
    d = d + 1
    n = int(input())
print(seqSum/d)
