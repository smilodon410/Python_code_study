# 내장 함수 복슴
# a = 10
# print(id(a))
# print(type(a))
#
# print(abs(-10))

# a = [10, 20, 30]
# for i in a:
#     print(i, end=' ')
# print()

# for k, v in enumerate(a):   # k = index(key), v = value
#     print(k, v)

# eval() 함수 : '' 안을 코드로 취급함
# a = 'print(10 + 20)'
# eval(a)

# Min(), Max() 함수
# a = [3, 5, 7]
# print(min(a))
# print(max(a))
# print(min([1, 2, 3, 4, 5]))
# print(max([1, 2, 3, 4, 5]))

# 진수 변환
# print(bin(100))     # 2진수 변환 : bin() => 0b~~
# print(oct(100))     # 8진수 변환 : oct() => 0o~~
# print(hex(100))     # 16진수 변환 : hex() => 0x~~
# 2진수에서 16진수로 변환할 때 4자리씩 끊어서 계산을 하게 되면 바로 나오게 된다.
# ex) bin(100) = 0b1100100 => 0110/0100 => 6/4 => 0x64 => hex(100)

# Type Casting :
# a = int('123')
# print(type(a))
# b = str(123)
# print(type(b))
#
# a = list('Apple')
# print(type(a))
# print(a)

# divmod(a, b) 함수 : 몫과 나머지를 구해주는 함수
# a = divmod(10, 3)
# print(a)

# 논리 연산
# print(True & True)
# print(all([True, True, True]))  # all = and 의 개념
#
# print(False or False or True)
# print(any([False, False, True]))    # any = or 의 개념

# a = [9, 6, 3, 7, 2]
# b = sorted(a)   # index 를 역순으로 바꿔준다.
# print(a)        # 원본은 그래도 두고 원본을 가지고 정렬된 결과를 저장
# print(b)

# a.sort()      # 원본을 수정한다
# print(a)
# a.sort(reverse=True)
# print(a)

# 외부 함수
# time
import time
# a = time.localtime(time.time())
# print(a)
# print(a.tm_year)
# print(a.tm_mon)
# print(a.tm_mday)
#
# b = ['월', '화', '수', '목', '금', '토', '일']
# print(b[a.tm_wday])

import datetime
# print(datetime.datetime.now())
#
# for i in range(5):
#     print(i)
#     time.sleep(1)    # time.sleep() : 출력 시간 지연

# Python Lambda
# def f1():
#     print(1)
# f1()
#
# f2 = lambda: print(2)
# f2()
# print(type(f2))
#
# f3 = lambda x : print(x*x)
# f3(9)
#
# f4 = lambda x, y: print(x+y)
# f4(10,20)
#
# f5 = lambda : 99
# print(f5())
#
# f6 = lambda x,y : x+y
# print(f6(3,4))
#
# def f1(ff):
#     ff()
#
# def f2():
#     print('호랑이')
#
# f1(f2)
# f1(lambda : print('코끼리'))
#
# def f3(ff):
#     ff(10,20)
# f3(lambda x,y : print(x+y))

# Lambda 예제
# def f04(a):
#     return a > 0
#
# a = filter(f04,[-2, -1, 0, 1, 2])
# print(list(a))
#
# a = filter(lambda a : a > 0 ,[-2, -1, 0, 1, 2])
# print(list(a))

