# n = int(input())
# s = list(map(int, input().split()))
# a = list()
# z = sorted(s)
# #c = 0
# q1 = q3 = -1
# for i in range(n):
#     if s[i] != z[i]:
#         q1 = i
#         break
# if q1 == -1:
#     print('yes')
#     print('1', '1')
#     exit()
# for i in range(n-1, q1, -1):
#     if s[i] != z[i]:
#         q3 = i
#         break
# a = list(reversed(s[q1:q3+1]))
# d = (z[q1:q3+1])
# if a == d:
#     print('yes')
#     print(q1+1, q3+1)
# else:
#     print('no')


n = int(input())
b = list(map(int, input().split()))
a = sorted(b)
if a == b:
    print('yes')
    print('1', '1')
    exit()
for i in range(len(b)):
    if b[i] != a[i]:
        f = i
        break
for i in reversed(range(len(b))):
    if b[i] != a[i]:
        e = i
        break
b[f:e+1] = reversed(b[f:e+1])
if b == a:
    print('yes')
    print(f+1, e+1)
else:
    print('no')
