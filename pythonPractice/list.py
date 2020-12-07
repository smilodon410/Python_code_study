# 평균 구하기 1
# sum = 0
# count = 0
# while True:
#     x = input('Enter a number: ')
#     if x == 'done':
#         break
#     y = float(x)
#     sum = sum + y
#     count = count + 1
#
# average = sum / count
# print(average)

# 평균 구하기 2
# numlist = list()
# while True:
#     x = input('Enter Number: ')
#     if x == 'done':
#         break
#     y = float(x)
#     numlist.append(y)
#
# average = sum(numlist) / len(numlist)
# print(average)

# Exercise - Guardian Pattern
x = open('mbox-short.txt')
for li in x:
    li = li.rstrip()
    y = li.split()
    # guardian in a compound statement
    if len(y) < 3 or y[0] != 'From':
        continue
    print(y[2])