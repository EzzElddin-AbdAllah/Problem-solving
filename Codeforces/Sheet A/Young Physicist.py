n = int(input())
s = list()
x = y = z = 0
for i in range(n):
    s = list(map(int, input().split()))
    x += s[0]
    y += s[1]
    z += s[2]
if x == y == z == 0:
    print('YES')
else:
    print('NO')