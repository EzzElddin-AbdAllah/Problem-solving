n = int(input())
c = 0
lap = {}
for i in range(n):
    x, y = map(int, input().split())
    lap[x] = y
d = dict(sorted(lap.items()))
for v in d.values():
    if v < c:
        print("Happy Alex")
        exit()
    c = v
print("Poor Alex")













exit()
for i in range(n):
    p, q = map(int, input().split())
    #if p < q:
    s.append(p)
    z.append(q)
    #elif p == q:
        #c += 1
z.sort()
for i in range(len(z)-1):
    if z[i] > z[i+1]:
        print("Poor Alex")
        exit()
print("Happy Alex")

exit()
if (len(s) == 0) | (c == n):
    print("Poor Alex")
    exit()
if len(s) == 1:
    if z[0] > s[0]:
        print("Happy Alex")
        exit()
mn = min(s)
mx = max(s)
for i in range(len(s)):
    if s[i] == mn:
        qn = z[i]
    if s[i] == mx:
        qm = z[i]
if qn < qm:
    print("Happy Alex")
else:
    print("Poor Alex")