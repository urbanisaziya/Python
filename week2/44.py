a = int(input())
b = int(input())
c = int(input())
d = int(input())
D = (a*d + b*c)*2 - 4*a*c*b*d
if D < 0:
	print("NO")
elif D == 0:
	print("1")
else:
	print("2")