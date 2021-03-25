n, m = map(int, input().split())
s = list()
s += (p for p in range(n+1, m+1) if 0 not in [p % d for d in range(2, p//2+1)])
f = bool
if m > 1:
    for i in range(2, m):
        if m % i == 0:
            f = False
            break
if f == False:
    print('NO')
else:
    if len(s) == 1:
        print('YES')
    else:
        print('NO')