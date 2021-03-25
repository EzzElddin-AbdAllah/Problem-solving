n = int(input())
s = list(input())
if n % 2 != 0:
    for i in range(n - 2, 0, -2):
        print(s[i], end='')
    for i in range(0, n, 2):
        print(s[i], end='')
else:
    for i in range(n - 2, -1, -2):
        print(s[i], end='')
    for i in range(1, n, 2):
        print(s[i], end='')
