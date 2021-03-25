n, x = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
c = 0
for i in range(n):
    c += (s[i] * x)
    if x > 1:
        x -= 1
print(c)