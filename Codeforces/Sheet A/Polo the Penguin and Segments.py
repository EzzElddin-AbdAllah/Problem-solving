n, k = map(int, input().split())
c = 0
s = list()
for i in range(n):
    x, y = map(int, input().split())
    s.append(y-x+1)
z = sum(s)
while 1:
    if z % k == 0:
        print(c)
        exit()
    else:
        z += 1
        c += 1