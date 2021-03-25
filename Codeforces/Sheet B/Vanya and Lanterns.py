n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
z = list()
if 0 not in s:
    z.append(s[0])
if l not in s:
    z.append(l - s[n-1])
for i in range(n-1):
    z.append((s[i+1]-s[i])/2)
print(max(z))
