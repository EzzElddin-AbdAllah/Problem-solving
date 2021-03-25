n = int(input())
z = list(str(n))
for i in range(len(z)):
    if i == 0:
        if z[0] == '9':
            print(z[0], end='')
            continue
    if int(z[i]) > (9 - int(z[i])):
        z[i] = 9 - int(z[i])
    print(z[i], end='')