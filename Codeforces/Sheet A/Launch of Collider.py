n = int(input())
s = list(input())
z = list(map(int, input().split()))
a = list()
c = 0
for i in range(n-1):
    if (s[i] == 'R') & (s[i+1] == 'L'):
        c += 1
        break
if (c == 0) | (n == 1):
    print('-1')
    exit()
for i in range(n-1):
    if (s[i] == 'R') & (s[i+1] == 'L'):
            a.append(z[i+1] - ((z[i] + z[i+1])//2))
print(min(a))
exit()
while 1:
    for i in range(n):
        if s[i] == 'R':
            z[i] += 1
        else:
            z[i] -= 1
        if i == n-1:
            break
        if s[i+1] == 'R':
            z[i+1] += 1
        else:
            z[i+1] -= 1
        c += 1
        if z[i] == z[i+1]:
            print(c)
            exit()
