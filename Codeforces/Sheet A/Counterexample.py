# n, m = map(int, input().split())
# z = m - n
# a = n
# c = a*2
# b = c - 1
# if z <= 1:
#     print('-1')
# else:
#     print(a, b, c)
n, m = map(int, input().split())
if n % 2 == 0:
    a = n
else:
    a = n + 1
b = a + 1
c = b + 1
if (c > m) | (m - n <= 1):
    print('-1')
else:
    print(a, b, c)
