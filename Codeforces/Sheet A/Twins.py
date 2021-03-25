n = int(input())
s = list(map(int, input().split()))
c = 1
s.sort(reverse=True)
if n == 1:
    print('1')
    exit()
elif n == 2:
    if max(s) == min(s):
        print('2')
    else:
        print('1')
    exit()
for i in range(n-1):
    if sum(s[0:i+1]) <= sum(s[i+1:n]):
       c += 1
    else:
        print(c)
        exit()