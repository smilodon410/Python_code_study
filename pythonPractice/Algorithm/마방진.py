x = int(input())
ar = [[0] * x for i in range(x)]
a = 0
b = x // 2
y = 1


while True:
    ar[a][b] = y
    y += 1
    if y % x != 1:
        a = a - 1
        b = b - 1
    else:
        a = a + 1
    if a < 0:
        a = x - 1
    if b < 0:
        b = x - 1
    ar[a][b] = y

    if y == (x*x):
        break

# 출력
for i in ar:
    print()
    for j in i:
        print('%02d' % j, end=' ')



