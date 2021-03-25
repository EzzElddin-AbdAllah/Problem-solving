a = [[j for j in input()] for i in range(4)]
for j in range(3):
    for k in range(3):
        if a[j][k] == a[j][k+1]:
            if (a[j+1][k] != a[j+1][k+1]) | (a[j+1][k] == a[j+1][k+1] == a[j][k] == a[j][k+1]):
                print('YES')
                exit()
        else:
            if a[j+1][k] == a[j+1][k+1]:
                print('YES')
                exit()
print('NO')