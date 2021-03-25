n = int(input())
z = int((n % 4))
if n == 0:
    print('1')
    exit()
if z == 0:
    print('6')
elif z == 1:
    print('8')
elif z == 2:
    print('4')
else:
    print('2')