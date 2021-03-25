n = int(input())
s = list(map(int, input().split()))
m = int(input())
if (n > 1) & (m != 0):
    for i in range(m):
        x, y = map(int, input().split())
        if x == 1:
            s[x] = s[x] + (s[x - 1] - y)
            s[x - 1] = 0
        elif x == n:
            s[x - 2] = s[x - 2] + y - 1
            s[x - 1] = 0
        else:
            s[x] = s[x] + (s[x - 1] - y)
            s[x - 2] = s[x - 2] + y - 1
            s[x - 1] = 0
elif m == 0:
    for i in range(m):
        print(s[i])
elif n == 1:
    x, y = map(int, input().split())
    print(0)
    exit()
for i in range(n):
    print(s[i])