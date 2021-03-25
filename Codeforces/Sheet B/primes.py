n = int(input())
n -= 2
if n < 3:
    print(-1)
elif n % 2 == 0:
    print(-1)
else:
    flag = True
    for i in range(3, n, 2):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(2, n)
    else:
        print(-1)
