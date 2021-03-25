n = int(input())
s = list(map(int, input().split()))
d1 = list()
d2 = list()
d3 = list()
x1 = x2 = x3 = 0
for i in s:
    if i == 1:
        x1 += 1
    elif i == 2:
        x2 += 1
    elif i == 3:
        x3 += 1
for i in range(len(s)):
    if s[i] == 1:
        d1.append(i+1)
    elif s[i] == 2:
        d2.append(i+1)
    elif s[i] == 3:
        d3.append(i+1)
print(min(x1, x2, x3))
for i in range(min(x1,x2,x3)):
    print(d1[i], d2[i], d3[i])