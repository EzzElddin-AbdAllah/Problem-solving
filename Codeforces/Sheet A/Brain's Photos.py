n, m = map(int, input().split())
c = 0
for i in range(n):
    s = list(input().split())
    if ('Y' not in s) & ('C' not in s) & ('M' not in s):
        c += 1
if c == n:
    print("#Black&White")
else:
    print("#Color")