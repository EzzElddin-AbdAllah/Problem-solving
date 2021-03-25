n, m, x = map(int, input().split())
k = [[chr(0) for i in range(m)] for y in range(n)]
shift = list()
for i in range(n):
    s = input()
    for j in range(m):
        k[i][j] = s[j]
        if s[j] == 'S':
            shift.append((i, j))
q = int(input())
t = input()
c = 0
mn = 0
f = 0
for i in range(q):
    if f == 1:
        break
    for j in range(n):
        if f == 1:
            break
        for v in range(m):
            if t[i].lower() == k[j][v]:
                f = 1
                break
if f == 0:
    print('-1')
    exit()
for i in range(q):
    if t.islower():
        continue
    else:
        inx = k.index("a")
        print(inx)