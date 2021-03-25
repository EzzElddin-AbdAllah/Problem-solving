with open('input.txt', 'r') as f:
    n = int(f.readline())
    c = list(map(int, f.readline().split()))
c1 = c.copy()
x = 0
y = 0
out = 5000
if max(c) <= min(c) * 2:
    out = 0
else:
    while max(c) >= min(c) * 2:
        c.remove(min(c))
        x += 1
    while max(c1) >= min(c1) * 2:
        c1.remove(max(c1))
        y += 1
    with open('output.txt', 'w') as f2:
        z = min(out, x, y)
        z = str(z)
        f2.write(z)

