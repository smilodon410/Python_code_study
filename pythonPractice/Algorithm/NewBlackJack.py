import random

# n, m 값 지정
n, m = map(int, input('n, m 값: ').split())

# 카드 후보군 선정
y = []
for i in range(n):
    while True:
        x = random.randint(0, 100000)
        if x > m:
            continue
        else:
            break
    y.append(x)
    print(x, end=' ')
print('')
print(y)

# m 에 근사한 값 만들기
while True:
    rd = random.sample(y, 3)
    sum = rd[0] + rd[1] + rd[2]
    if sum < m:
        print(sum)
    elif sum > m:
        rd = 0
    else:
        break

print(rd)

