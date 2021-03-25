n, k = map(int, input().split())
s = list()
for i in range(k):
    s.append(chr(i+97))
for i in range(n - k):
    s.append(s[i])
for i in range(len(s)):
    print(s[i],end='')