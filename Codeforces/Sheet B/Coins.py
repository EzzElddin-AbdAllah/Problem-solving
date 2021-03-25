s1 = input()
s2 = input()
s3 = input()
z = list()
if s1[1] == '>':
    z.append(s1[0])
else:
    z.append(s1[2])
if s2[1] == '>':
    z.append(s2[0])
else:
    z.append(s2[2])
if s3[1] == '>':
    z.append(s3[0])
else:
    z.append(s3[2])
if ('A' in z) & ('B' in z) & ('C' in z):
    print('Impossible')
    exit()
else:
    if (z.count('A') > z.count('B')) & (z.count('A') > z.count('C')):
        if z.count('B') > z.count('C'):
            print('CBA')
        else:
            print('BCA')
    else:
        if z.count('B') > z.count('C'):
            if z.count('A') > z.count('C'):
                print('CAB')
            else:
                print('ACB')
        else:
            if z.count('A') > z.count('B'):
                print('BAC')
            else:
                print('ABC')
