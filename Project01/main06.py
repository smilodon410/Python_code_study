# Function : 함수
# # 1번째 함수 생성
# print(99)
# def func01():
#     print(1)
#     print(2)
#     print(3)
#
# func01()
# print(100)
#
# func01()
#
# # 2번째 함수 형식 : 전달 인수
# def func02(num):
#     print('A')
#     print('B')
#     print('C')
#
# func02(50)
#
# # 3번째 함수 형식 : Return 이 있는 형식
# def func03():
#     return 100
#
# a = func03()
# print(a)
#
# print(func03())
#
# # 정말 이것은 주의하자!!
# # print(func01())    # 리턴 값이 없는 함수는 사용이 불가
#
# print(func03() * 7)
#
# # 4번째 유형 : 전달 인수 + Return
# def func04(num):
#     return num + 100
#
# a = func04(100)
# print(a)
#
# print(func04(55))


# 함수의 활용
# def func05(a, b, c):
#     sum = a * b * c
#     print(sum)
#     print(a * a + b * b + c * c)
#
#
# func05(2, 3, 4)
# func05(3, 4, 5)
#
#
# # Unreached Code
# def func06():
#     print(1)
#     return;
#     print(2)  # Unreached code
#
#
# func06()
#
#
# def func07(a, b):
#     print(a, b)
#     print(type(a), type(b))
#
#
# func07(10, '호랑이')
#
#
# # default 값을 정한 함수
# def func08(a, b, c=10, d=20):  # 최소 인수 2개 이상을 넣어준다
#     print(a, b, c, d)
#
#
# func08(1, 2)  # c, d 값은 default 값
# func08(1, 2, 3)  # c 값은 지정 값으로 바뀜
# func08(1, 2, 3, 4)
#
# # 가변 인수 : 인수 줘도 되고 안줘도 되고~ 니맘이야~
# def func09(*args) :
#     print('니맘이야~')
#     for data in args:
#         print(data)
#     print('*' * 50)
#
# func09()
# func09(10)
# func09(20, 30)
# func09(40, 50, '호랑이')
#
# def func10(a, b, *args):
#     print(a, b)
#     for data in args:
#         print(data)
#     print('-' * 10)
#
# func10(10, 20)
# func10(10, 20, 30)
# func10(10, 20, 30, 40)
#
# # '*' 뒤에 인수는 호출 시 반드시 변수 명을 입력하고 값을 줄 것!!
# def func11(a, b, *, colar, data):
#     print(a, b, colar, data)
#
# func11(1, 2, colar=3, data=4)
#
# # Dictionary 화
# def func12(**star):
#     print(star)
#     for k,v in star.items():
#         print('(', k, v, ')')
#
# func12(a = 10, b = 20)

