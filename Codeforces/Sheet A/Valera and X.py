n = int(input())
s = [[j for j in input()] for i in range(n)]
for i in range(((n-1)//2)+1):
    if (s[i][i] != s[i][n-1-i]) | (s[i][i] != s[0][0]):
        print('NO')
        exit()
for i in range(n-1, ((n-1)//2), -1):
    if (s[i][i] != s[i][n-i-1]) | (s[i][i] != s[0][0]):
        print('NO')
        exit()
if (s[0][0] != s[((n-1)//2)][((n-1)//2)]) | (s[0][0] == s[0][1]):
    print('NO')
    exit()
for i in range(1, n):
    if i == ((n-1)//2):
        continue
    if s[((n-1)//2)][0] != s[((n-1)//2)][i]:
        print('NO')
        exit()
for i in range(((n-1)//2)):
    for j in range(n):
        if (i == j) | (n - 1 - i == j):
            continue
        if s[i][j] != s[0][1]:
            print('NO')
            exit()
for i in range(n-1, ((n-1)//2), -1):
    for j in range(n):
        if (i == j) | (j == n - 1 - i):
            continue
        if s[i][j] != s[0][1]:
            print('NO')
            exit()
print('YES')