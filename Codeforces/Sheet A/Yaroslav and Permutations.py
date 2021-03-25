n = int(input())
s = list(map(int, input().split()))
z = list()
if n == 1:
    print('YES')
    exit()
if n == 2:
    if s[0] == s[1]:
        print('NO')
        exit()
    else:
        print('YES')
        exit()
for i in range(n):
    if s[i] in s[0:i]:
        continue
    z.append(s.count(s[i]))


if len(z) == 1:
    print('NO')
    exit()
if max(z) <= sum(z) - max(z) + 1:
    print('YES')
else:
    print('NO')
