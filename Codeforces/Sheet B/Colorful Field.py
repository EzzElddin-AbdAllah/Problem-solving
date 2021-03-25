n, m, k, t = map(int, input().split())
f = [[0 for x in range(m)] for y in range(n)]
x = ['Carrots', 'Kiwis', 'Grapes']
c = 0
for i in range(k):
    w1, w2 = map(int, input().split())
    f[w1-1][w2-1] = 'Waste'
for i in range(n):
    for j in range(m):
        if f[i][j] == 'Waste':
            continue
        f[i][j] = x[c]
        c += 1
        if c == 3:
            c = 0
for i in range(t):
    w1, w2 = map(int, input().split())
    print(f[w1-1][w2-1])
