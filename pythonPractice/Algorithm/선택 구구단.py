n, m = map(int, input('숫자를 입력하세요: ').split())
a = [n, m]
if n > m:
    r = range(n, m - 1, -1)
else :
    r = range(n, m + 1)

for i in r:
    for j in range(1, 10):
        x = i * j
        print("%d * %d = %2d" % (i, j, x), end='   ')
        if j % 3 == 0:
            print('')
    print('')