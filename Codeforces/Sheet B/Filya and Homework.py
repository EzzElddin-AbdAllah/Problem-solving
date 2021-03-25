n = int(input())
a = sorted(list(set(map(int, input().split()))))
if len(a) > 3:
    print('NO')
elif len(a) == 2 or len(a) == 1:
    print('YES')
else:
    if a[1] - a[0] == a[2] - a[1]:
        print('YES')
    else:
        print('NO')
