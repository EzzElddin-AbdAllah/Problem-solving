s = input().split('+')
s.sort()
d = list()
for i in range(len(s)):
    d.append(int(s[i]))
for i in range(len(d)):
    if i == len(d)-1:
        print(d[i])
    else:
        print(d[i], end='+')