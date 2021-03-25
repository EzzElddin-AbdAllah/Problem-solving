n = int(input())
s = input()
counter = 0
for i in range(n):
    if i == n-1:
        break
    if s[i] == s[i+1]:
        counter = counter + 1
print(counter)