import random

a, b, jump = map(int, input().split())

ar =[]
ar1 = []
t = 0
sum = 0
for i in range(a):
    for j in range(b):
        t = random.randint(-100, 100)
        print(t, end=' ')
        ar.append(t)
    print()

for i in range(len(ar)):
    c = abs(int(ar[i]))
    ar1.append(c)

ar1.sort(reverse=True)
print(ar1)

for i in range(jump + 1):
    d = int(ar1[i])
    st = t * d
    t = d
    sum = sum + st
print(sum)

