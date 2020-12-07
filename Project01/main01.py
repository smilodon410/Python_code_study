# 주석
# """전체 주석"""
#
# # 문자열 출력
# print('Hello world')
#
# # 복합 출력(숫자열, 문자열)
# print(10, '호랑이', 20, '독수리')
#
# # True와 False의 첫자는 반드시 대문자!
# print(True)
#
# # 한 줄에서 연결 할 때 ; 사용
# print(10); print(20)
#
# print(10, end='\n')  # end = '\n'은 default 값 : 줄바꿈
# print(20)
#
# # 구분자
# print("-" * 50)
#
# # %치환
# print("%d %d %s" % (10, 20, '호랑이'))
# print("%s%s%s" % ('코', '끼', '리'))
#
# # 숨겨진 default 값
# print(10, 20, 30, 40, sep=' ')
# print(10, 20, 30, 40, sep=',')
# print(10, 20, 30, 40, sep=',', end='\n')
#
# # 타입 묻기
# print(type(10), type('호랑이'), type(3.14), type(True))
# print(type([]), type(()), type({}))
#
# # 문자열과 정수형
# print(10 + 20)
# # print(10 + '호랑이') # 문법이 성립하지 않음
# # print('호랑이' + 10) # 문법이 성립하지 않음
# print('호랑이' + ' 독수리')
#
# # 형 변환
# print(10 + int('123'))
# print('호랑이' + str('10'))
#
# # 파이썬은 변수를 선언하는 타입이 없다!
# a = 10
# b = 20
# print(a, b)
#
# a = 30
# b = 40
# print(a, b)
#
# a, b = 50, 60
# print(a, b)
#
# a = b = 70
# print(a, b)
#
# # a = 10 b = 20 # 안되는 문법! ;을 활용하자
#
# a = 10
# b = 20
# # 파이썬에서 Swap
# b, a = a, b
# print(a, b)
#
# a = 10
#
# # a++은 안됨
# a = a + 1
# a += 1
# print(a)
#
# # 고유 식별 번호 확인 : id()
# a = 10
# b = 20
# c = 10
# print(id(a), id(b), id(c))
#
# a = '호랑이'
# b = '독수리'
# c = '호랑이'
# print(id(a), id(b), id(c))
#
# a = 0x10 # 16진수 표기법
# # print(a)
#
# a = 0o10 # 8진수 표기법
# print(a)
#
# # 몫과 나머지 구하기
# a = 10
# b = 5
# print(a%b)
# print(a//b)
#
# print(2**8)
#
# print(round(3.14))

# 배열 공부 하기



