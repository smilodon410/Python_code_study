# class Apple:
#     def __init__(self):
#         pass
#     def f1(self):
#         print(1)
#     def f3(self):
#         print(3)
#
# class Orange(Apple):
#     def __init__(self):
#         pass
#     def f2(self):
#         print(2)
#     def f3(self):
#         super().f3()
#         print(4)
#     def f4(self):
#         self.f2()
#         self.f3()
#         super().f3()
#
# o = Orange()
# o.f1()
# o.f2()
# o.f3() # 자식 f3



# 파이썬은 Upcasting 개념이 없다

# print(Apple.mro())


# class Dog:
#     def __init__(self):
#         pass
#
#     def cry(self):
#         print('멍멍')
#
# class Cat:
#     def __init__(self):
#         pass
#
#     def cry(self):
#         print('냐용')
#
# class Snake:
#     def __init__(self):
#         pass
#
#     def cry(self):
#         print('띠용!')
#
# a1 = Dog()
# a2 = Cat()
# a3 = Snake()
#
# a1.cry()
# a2.cry()
# a3.cry()
#
# # for 문을 활용해서 한 번에 호출하기
# a4 = [Dog(), Cat(), Snake()]
# for obj in a4:
#     obj.cry()


# class Apple():
#     def __init__(self):
#         pass
#     def f1(self):
#         print(1)
#
# def f2(a = Apple()):
#     print(2)
#     a.f1()
#
# f2()


# 예외 상황 : Try, Except 활용
# a = 4 / 0
# print(1)

# print(0)
# try:
#     a = 4/0
# except:
#     print(1)
# print(2)

# Exception as = 무슨 상황인지 알고 싶을 때
# print(0)
# try:
#     a = 4/0
# except Exception as e:
#     print(e)
# print(2)
#
# print(0)
#
# # Finally : 예외 상황이 발생해도 무조건 실행
# try:
#     a = 4/0
# except:
#     print(1)
# finally:
#     print(30)
# print(2)


# a = [10, 20, 30]
# b = a.index(30)
# print(b)
# try:
#     c = a.index(100)
# except Exception as e:
#     print(e)
# finally:
#     print('호랑이')

# 파일 입출력
# open(파일명, 파일 형식, 언어방식)
# file = open("sample.txt", "w", encoding='UTF-8')
# file.write('Money')
# file.close()

