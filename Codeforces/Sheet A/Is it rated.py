n = int(input())
s = list()
d = list()
c = 0
for i in range(n):
    s += (list(map(int, input().split())))
for i in range(0, n*2, 2):
    if s[i] == s[i+1]:
        c += 1
if c != n:
    print("rated")
else:
    for i in range(0, n*2, 2):
        d.append(s[i])
    if d == sorted(d, reverse=True):
        print("maybe")
    else:
        print("unrated")