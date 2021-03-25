# while 1:
#     n, m = map(int, input().split())
#     c = 0
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if (i + j) % 5 == 0:
#                 c += 1
#     print(c)
#     if n % 5 == 0:
#         print(m * (n // 5))
#     elif m % 5 == 0:
#         print(n * (m // 5))

print(3%5)
n, m = map(int, input().split())
c = 0
for i in range(1, n+1):
    c+=(i+m)//5-(i)//5
print(c)
