n, k = map(int, input().split())
z = c = 0
for i in range(n):
    s = input()
    for j in range(k+1):
        if str(j) in s:
            z += 1
        else:
            break
    if z == k+1:
        c += 1
    z = 0
print(c)