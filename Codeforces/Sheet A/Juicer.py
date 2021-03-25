n, b, d = map(int, input().split())
s = list(map(int, input().split()))
c = 0
z = 0
for i in s:
    if i <= b:
        z += i
    if z > d:
        c += 1
        z = 0
print(c)