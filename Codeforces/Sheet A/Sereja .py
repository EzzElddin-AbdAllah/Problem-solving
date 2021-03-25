n = int(input())
s = list(map(int, input().split()))
a = b = y = 0
x = 1
for i in range(n):
    if i % 2 == 0:
        if s[n-x] > s[y]:
            a = a + s[n-x]
            x = x + 1
        else:
            a = a + s[y]
            y = y + 1
    else:
        if s[n-x] > s[y]:
            b = b + s[n-x]
            x = x + 1
        else:
            b = b + s[y]
            y = y + 1
print(a, b)