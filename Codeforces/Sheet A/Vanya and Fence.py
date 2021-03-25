n, h = map(int, input().split())
v = list(map(int, input().split()))
a = 0
for i in range(n):
    if v[i] <= h:
        a += 1
    else:
        a += 2
print(a)
