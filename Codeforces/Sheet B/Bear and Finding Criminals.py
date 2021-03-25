n, a = map(int, input().split())
z = list(map(int, input().split()))
c = 0
if z[a-1] == 1:
    c += 1
if len(z[:a-1]) > len(z[a:]):
    x = len(z[:a-1]) - len(z[a:])
    c += z[:x].count(1)
    for i in range(1, len(z[a:])):
        if z[a-i-1] == z[a+i-1] == 1:
            c += 2
else:
    x = len(z[a:]) - len(z[:a-1])
    c += z[len(z)-x:].count(1)
    for i in range(1, len(z[:a])):
        if z[a-i-1] == z[a+i-1] == 1:
            c += 2
print(c)
