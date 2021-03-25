s = list(input())
z = list(input())
x = list()
for i in range(len(s)):
    if s[i] == '|':
        inx = i
x = s[0:inx]
for i in range(inx+1):
    del s[0]
for i in range(len(z)):
    if len(x) < len(s):
        x += z[i]
    else:
        s += z[i]
if len(x) != len(s):
    print("Impossible")
    exit()
for i in range(len(x)):
    print(x[i], end='')
print('|', end='')
for i in range(len(s)):
    print(s[i], end='')
# if (min(len(s), len(x)) + len(z)) == max(len(s), len(x)):
#     if len(s) > len(x):
#         for i in range(len(x)):
#             print(x[i], end='')
#         for i in range(len(z)):
#             print(z[i], end='')
#         print('|', end='')
#         for i in range(len(s)):
#             print(s[i], end='')
#     else:
#         for i in range(len(x)):
#             print(x[i], end='')
#         print('|', end='')
#         for i in range(len(s)):
#             print(s[i], end='')
#         for i in range(len(z)):
#             print(z[i], end='')
# else:
#     print("Impossible")