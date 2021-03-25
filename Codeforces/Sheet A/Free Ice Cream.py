n, x = map(int, input().split())
c = 0
for i in range(n):
    p, m = input().split()
    m = int(m)
    if p == '+':
        x += m
    else:
        if m > x:
            c +=1
        else:
            x -= m
print(x, c)
