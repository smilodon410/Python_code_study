#a = 0
# x = int(input('숫자를 입력하세요: '))
#
# while True :
#     if x % 2 == 0 :
#         a = int(x / 2)
#         print(a)
#         x = a
#     else :
#         a = x * 3 + 1
#         print(a)
#         x = a
#     if x == 1 :
#         break;
# print("탈출!")

# 우박수 삼항연산
# x = ( True if 조건 else False)
# x = int(input('숫자를 입력하세요: '))
# while True:
#     x = ( x / 2 if x % 2 == 0 else x * 3 + 1)
#     print(int(x))
#     if x == 1:
#         print('탈출!')
#         break

# range 함수
# list - range
# a = list(range(5, 10))
# print(a)
# print(list(range(3, 20, 2)))

# for문
# for i in [0, 1, 2, 3, 4] :
#     print(i)

# for i in ['월', '화', '수', '목', '금', '토', '일'] :
#     print(i, end = ' ')
# print(' ')
    
# for i in ['강아지', '고양이', '호랑이'] :
#     print(i, end = ' ')
# print(' ')

# for문의 기본형
# for i in range(0, 10) :
#     print(i, end = ' ')
# print(' ')

# 구구단
# x = int(input('몇 단? '))
# a = 0
# for i in range(0, 10) :
#     a = x * i
#     print( x, ' * ', i, ' = ', a)

# 숫자의 총합 구하기
# x = int(input('숫자를 입력하세요: '))
# sum = 0
# for i in range(1, x + 1) :
#     sum = sum + i
# print(sum)

# 다중 for문의 정석코드
# for i in range(0, 3) :
#     print(' ')
#     for j in range(0, 4) :
#         print('[', i, ' ', j, ']', end = ' ')

# k = 0
# for i in range(0, 3):
#     print(' ')
#     for j in range(0, 4):
#         print('{0:02d}'.format(k), end=' ')
#         k += 1

# 이중 for문(랜덤 인수와 각 row의 합 구하기)
# from random import *
#
# sum = 0
#
# for i in range(0, 3):
#     print('')
#     for j in range(0, 4):
#         x = randint(0, 10)
#         print('{0:02d}'.format(x), end=' ')
#         sum = sum + x
#     print(' 계: ', sum)
#     sum = 0