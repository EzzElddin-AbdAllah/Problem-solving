n = int(input())
c = 1
while n != 1:
    if n % 2 != 0:
        c += 1
    n = n//2
print(c)