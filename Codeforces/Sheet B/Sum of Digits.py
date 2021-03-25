n = input()
n = list(n)
c = z = 0
while len(n) > 1:
    for i in n:
        z += int(i)
    n = list(str(z))
    z = 0
    c += 1
print(c)