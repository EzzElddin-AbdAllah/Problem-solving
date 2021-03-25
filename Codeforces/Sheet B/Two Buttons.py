n, m = map(int, input().split())
x = 0
if n >= m:
    if n > m:
        print(n-m)
    else:
        print(0)
else:
    while n < m:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        x += 1
    print(x+n-m)
