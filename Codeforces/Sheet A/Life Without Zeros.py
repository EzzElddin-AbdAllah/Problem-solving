a = input()
b = input()
c = int(''.join(str(int(a) + int(b)).split('0')))
z = int(''.join(a.split('0'))) + int(''.join(b.split('0')))
if c == z:
    print('YES')
else:
    print('NO')
