m, n, a = map(int, input().split())
# z1 = z2 = a
# c1 = 1
# if m == n:
#     if m % a != 0:
#         c1 = (m // a) + 1
#     else:
#         c1 = (m // a)
#     print(c1*c1)
#     exit()
if m % a != 0:
    c1 = (m // a) + 1
else:
    c1 = (m // a)
if n <= a:
    c2 = 0
elif n % a != 0:
    c2 = (n // a) + 1
else:
    c2 = (n // a)
    # else:
    #     if n % a != 0:
    #         c1 = (n // a) + 1
    #     else:
    #         c1 = (n // a)
    #     if m <= a:
    #         c2 = 0
    #     else:
    #         c2 = (m // a)

# while 1:
#     if (m <= z1) & (n <= z2):
#         break
#     if m > z1:
#         c1 += 1
#         z1 += a
#     if n > z2:
#         c2 += 1
#         z2 += a
if c2 == 0:
    print(c1)
    exit()
print(c2*c1)