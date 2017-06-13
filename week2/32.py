n = int(input())
if (n <= 20 and n == 1) or (n > 20 and (n % 10) == 1):
    print(n, 'korova')
elif (n > 20) and ((n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4):
    print(n, 'korovy')
elif (n < 10) and (n == 2 or n == 3 or n == 4):
    print(n, 'korovy')
else:
    print(n, 'korov')
