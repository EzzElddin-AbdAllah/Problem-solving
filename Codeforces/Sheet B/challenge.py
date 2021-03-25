n, k = map(int, input().split())
n += 1
while n % k != 0:
    n += 1
print(n)
