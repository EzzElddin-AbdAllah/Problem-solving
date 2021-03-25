a = input()
b = input()
if a == b:
    print('-1')
elif len(a) > len(b):
    print(len(a))
else:
    print(len(b))
# x = list()
# z = list()
# c = d = 1
# if a == b:
#     print('-1')
#     exit()
# else:
#     for i in range(len(a) - 1):
#         if (ord(a[i]) + 1 == ord(a[i + 1])) | (ord(a[i]) == ord(a[i + 1])):
#             c += 1
#         else:
#             z.append(c)
#             c = 1
#         if i == len(a) - 2:
#             z.append(c)
#     for i in range(len(b) - 1):
#         if ord(b[i]) + 1 == ord(b[i + 1]):
#             d += 1
#         else:
#             x.append(d)
#             d = 1
#         if i == len(b) - 2:
#             x.append(d)
#     print(max(max(z), max(x)))