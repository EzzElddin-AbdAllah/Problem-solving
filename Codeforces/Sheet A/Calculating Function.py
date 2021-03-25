n = int(input())
if n % 2 == 0:
    print(n//2)
    exit()
else:
    print(((n-1)//2)-n)