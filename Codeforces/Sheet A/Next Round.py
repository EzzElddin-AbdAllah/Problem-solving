n, k = map(int, input().split())
s = list(map(int, input().split()))
c = 0
for i in range(n):
    if (s[i] >= s[k-1]) & (s[i] > 0):
        c += 1
print(c)