n = int(input())
x = int(input())
for i in range(n):
    z1, z2 = map(int, input().split())
    s = [x, 7 - x, z1, z2, 7 - z1, 7 - z2]
    if (x==z1) | (x==7-z1) | (x-7==z1) | (x-7==7-z1) | (x==z2) | (x==7-z2) | (x-7==z2) | (x-7==7-z2):
        print('NO')
        exit()
print('YES')