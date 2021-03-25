n = int(input())
s = list()
a = b = z = 0
for i in range(n):
    s.append(input())
for i in range(n):
    if s[0] != s[i]:
        a = s.count(s[0])
        b = s.count(s[i])
        z = i
        break
if a > b:
    print(s[0])
else:
    print(s[z])
