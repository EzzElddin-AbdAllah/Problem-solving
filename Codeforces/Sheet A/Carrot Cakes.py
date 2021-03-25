n, t, k, d = map(int, input().split())
z1 = z2 = z3 = 0
x = c = y = 0
while 1:
    x += k
    z1 += t
    if x >= n:
        break
c = int(d/t)
z2 = c*t
x = c*k
while 1:
    if x >= n:
        break
    else:
        x += 2*k
        z2 += t
x = y = 0
z3 = d
while 1:
    x += 2*k
    z3 += t
    if x >= n:
        break
if (z2<z1) | (z3<z1):
    print('YES')
else:
    print('NO')