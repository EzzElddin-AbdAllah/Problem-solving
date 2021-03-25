n = int(input())
if n < 6:
    if n == 1 or n == 2:
        print(n * 2)
    elif n == 3:
        print(7)
    elif n == 4:
        print(11)
    else:
        print(16)
else:
    print((n - 2) * 5)
