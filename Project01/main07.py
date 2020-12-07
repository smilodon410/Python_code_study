# Python class 기본형
# class Apple:
#     def __init__(self):    # 생성자 함수 : (self)는 필수
#         print('생성자 콜!')
#
#
# a = Apple()    # 객체 생성
#
#
# class Apple:
#     def __init__(self):
#         pass
#
#
# a = Apple()

# class 에 함수 생성하기
# class Apple:
#     def __init__(self):
#         pass
#
#     def func01(self):    # 함수 생성
#         print(1)
#
#     def func02(self, num):    # 인수를 주더라도 무조건!! self 는 포함되어야 함
#         print(2)
#
#     def func03(self):
#         return 3
#
#     def func04(self, num):
#         return num
#
# a = Apple()
# a.func01()    # 함수 호출
# a.func02(2)
#
# b = a.func03()
# print(b)
#
# c = a.func04(50)
# print(c)

# Self
# class Apple:
#     def __init__(self):
#         print(id(self))    # self = (Java) this
#         pass
# #
# #
# a = Apple()
# print(id(a))

# Field
# class Apple:
#     num = 10
#
#     def __init__(self):
#         pass
#
# a = Apple()
# print(a.num)

# Field 자동 생성
# class Apple:
#
#     def __init__(self, num):
#         self.num = num    # 필드 선언 안해도 필드 자동 생성 : 동적
#
#     def func(self, num):    # 필드 선언을 안했기에 바로 num 을 사용 할 수 없다.
#         print(num)
#
# a = Apple(20)
# print(a.num)
# a.func(30)

# 동적(Dynamic) : 필요할 때 만들어 쓰는 것
# 정적(Static : 처음부터 만들어져 있는 것

# a1 = Field, a2 = Dynamic Field, a3 = Method 변수
# class Apple:
#     a1 = 10
#
#     def __init__(self, a2):
#         self.a2 = a2
#
#     def f1(self):
#         a3 = 30
#         print(self.a1, self.a2, a3)
#
# a = Apple(20)
# a.f1()