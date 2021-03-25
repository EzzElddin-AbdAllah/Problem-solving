n = int(input())
s = list(map(int, input().split()))
c = 0
x = max(s)
y = min(s)
if n <= 2:
    print('0')
else:
    for i in range(n):
        if (s[i] < x) & (s[i] > y):
            c += 1
    print(c)