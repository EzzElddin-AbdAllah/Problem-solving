# x = 1
# for i in range(5):
#     a, b, c, d, e = map(int, input().split())
#     if a+b+c+d+e == 1:
#         r = i + 1
#         for i in (a, b, c, d, e):
#             if i == 1:
#                 break
#             else:
#                 x = x + 1
#                 continue
#     else:
#         continue
# if r >= 3:
#     h = r - 3
# else:h = 3 - r
# if x >= 3:
#     v = x - 3
# else: v = 3 - x
# print(h+v)


m = [[int(j) for j in input().split()] for i in range(5)]
for i in range(0, 5):
    for j in range(0, 5):
        if m[i][j] == 1:
            print(abs(i-2)+abs(j-2))
