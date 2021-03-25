n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
c = 0
for x in range(n):
    for j in range(n):
        if a[x][0] == a[j][1]:
            c += 1
print(c)