import itertools
def sum_sym(x):
    y = 0
    for i in x:
        if i == '+':
            y += 1
        else:
            y += -1
    return y


s = input()
r = input()
y = 0
ss = sum_sym(s)
qu_count = r.count('?')
pure = list()
if '?' not in r:
    sr = sum_sym(r)
    if ss == sr:
        print('1')
        exit()
for i in r:
    if not i == '?':
        pure += i
prob = list(itertools.combinations_with_replacement(['-', '+'], qu_count)) + list(itertools.combinations_with_replacement(['+', '-'], qu_count))
for i in range(len(prob)-2):
    if prob[i] in prob[i+1::]:
        prob.remove(prob[i])
#print(prob)
for i in range(len(prob)):
    prob[i] += tuple(pure)
    if sum_sym(prob[i]) == ss:
        y += 1
# prob_pure = list(sum_sym(i) for i in prob)
print(y/len(prob))
#print(prob)
