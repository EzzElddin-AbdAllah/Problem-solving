n = int(input())
#clr = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
c = 0
print('ROYGBIV', end='')
n -= 7
cr = ['G', 'B', 'I', 'V']
for i in range(n):
    print(cr[c], end='')
    c += 1
    if c == 4:
        c = 0
exit()
# for i in range(n):
#     print(clr[c], end='')
#     c += 1
#     if c == 7:
#         c = 0
#         x = clr[0]
#         y = clr[1]
#         del clr[0]
#         del clr[1]
#         clr.append(x)
#         clr.append(y)
#         #z += 1
# exit()
if (n - 1) % 7 == 0:
    #print('G', end='')
    for i in range(1, n+1):
        if i % 8 == 0:
            print('G', end='')
            continue
        print(clr[c], end='')
        c += 1
        if c == 7:
            c = 0
else:
    for i in range(1, n+1):
        if i % 8 == 0:
            print('G', end='')
            continue
        print(clr[c], end='')
        c += 1
        if c == 7:
            c = 0
