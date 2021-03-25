n = input()
s = input()
op = list()
z1 =('qwertyuiop')
z2 = ('asdfghjkl;')
z3 = ('zxcvbnm,./')
if n == 'R':
    for i in range(len(s)):
        if s[i] in z1:
            for j in range(len(z1)):
                if s[i] == z1[j]:
                    op.append(z1[j-1])
        elif s[i] in z2:
            for j in range(len(z2)):
                if s[i] == z2[j]:
                    op.append(z2[j-1])
        else:
            for j in range(len(z3)):
                if s[i] == z3[j]:
                    op.append(z3[j-1])
        print(op[i], end='')
elif n == 'L':
    for i in range(len(s)):
        if s[i] in z1:
            for j in range(len(z1)):
                if s[i] == z1[j]:
                    op.append(z1[j+1])
        elif s[i] in z2:
            for j in range(len(z2)):
                if s[i] == z2[j]:
                    op.append(z2[j+1])
        else:
            for j in range(len(z3)):
                if s[i] == z3[j]:
                    op.append(z3[j+1])
        print(op[i], end='')