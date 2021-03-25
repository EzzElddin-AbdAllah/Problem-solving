n = int(input())
d1 = dict()
x = list(map(int, input().split()))
for i in range(n):
    d1[x[i]] = i
m = int(input())
y = list(map(int, input().split()))
c1 = c2 = m
for i in range(m):
    c1 += d1.get(y[i])
    c2 += n - 1 - d1.get(y[i])
print(c1, c2)
exit()










# n = int(input())
# a1 = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# #a2 = a1[::-1]
# c1 = c2 = m
# for i in range(m):
#     for j in range(n):
#         if b[i] == a1[j]:
#             c1 += j
#             break
#     for k in range(n-1, -1, -1):
#         if b[i] == a1[k]:
#             c2 += n - 1 - k
#             break
#     #c1 += a1.index(b[i])
#     #c2 += a2.index(b[i])
# print(c1, c2)
