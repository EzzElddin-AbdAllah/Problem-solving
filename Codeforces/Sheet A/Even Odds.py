n, k = map(int, input().split())
if k <= int(round(n/2+.1)):
    print(1+2*(k-1))
else:
    if n % 2 == 0:
        print(int(2 * (k - (n / 2))))
    else:
        print(int(2 * (k - (n / 2))-1))