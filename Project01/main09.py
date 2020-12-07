# for i in range(5):
#     print(i)

# for i in range(2, 7):
#     print(i)

# for 문을 활용하여 파일에 문자 넣기
# file = open("main09.txt", "w", encoding='UTF-8')
# for i in range(5):
#     file.write('호랑이')
# file.close()

# int 형은 입력이 불가하다!( str 변환 사용 )
# file = open("main09.txt", "w", encoding='UTF-8')
# for i in range(5):
#     file.write(str(i))
# file.close()

# .write 에서 줄바꿈 '\n' 은 , 가 아닌 +로 연결한다
# file = open("main09.txt", "w", encoding='UTF-8')
# for i in range(5):
#     file.write('호랑이' + str(i) + '\n')
# file.close()

# with ~ as 변수명 : 약식형 ( file.close() 를 생략 할 수 있다. )
# Reading 용으로 사용, Write 는 안쓰임
# with open("main09.txt", "w", encoding='UTF-8') as file:
#     for i in range(5):
#         file.write('호랑이' + str(i) + '\n')

# if 에 문자열을 넣어도 True, False 값이 나올 수 있다.
# if '호랑이':
#     print(1)
# if '':
#     print(2)

# .readline 함수를 활용한 문서 읽기
# file = open("main09.txt", 'r', encoding='UTF-8')
# data = file.readline()  # Return 값이 있으므로 변수를 지정해준다.
# print(data)
# if data:    # data 를 읽었는지 확인하기 위해 -> 확인 했으면 10을 출력
#     print(10)
#
# data = file.readline()
# print(data)
# if data:    # 읽을 데이터가 없기때문에 출력값이 없다.( null 값은 False )
#     print(20)
# file.close()

# while 문을 활용한 문서 읽기
# file = open('main09.txt', 'r', encoding='UTF-8')
# while True:
#     data = file.readline()
#     print(data)
#     if not data:    # 읽을 데이터가 없으면 break
#         break
# file.close()

# for 문을 활용한 문서 읽기
# file = open("main09.txt", 'r', encoding='UTF-8')
# for i in file:
#     print(i)
# file.close()

# .readlines : 전체 파일 한번에 읽기 = List 에 넣어준다
# file = open('main09.txt', 'r', encoding='UTF-8')
# data = file.readlines()
# print(data)
# for i in data:
#     print(i, end='')
# file.close()

# 줄바꿈 제거 하기 : for 문을 활용하여 .replace 사용하기
# a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
#
# for i in range(0, len(a)):
#     a[i] = a[i].replace('\n', '')
#
# for i in a:
#     print(i)

# 줄바꿈 제거 하기 : enumerate 사용하기 = Index 를 포함하는 객체를 리턴한다.
# a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
# for Index,Value in enumerate(a):
#     a[Index] = Value.replace('\n', '')
#
# for i in a:
#     print(i)

# 바로 문자열로 파일 읽기
# file = open('main09.txt', 'r', encoding='UTF-8')
# a = file.read()
# file.close()
# print(a)

# 외부 경로 파일 불러오기
# file = open('C:\\Users\\BIT_R45\\Desktop\\과제\\Yolo Model.txt', 'r', encoding='UTF-8')
# for i in file:
#     print(i)

# import 를 활용하여 파일 끌어오기
# import tiger
# tiger.f01()
#
# from tiger import *
# f01()

# 별칭 사용하기 : import A as B = A: 파일명, B: 별칭
# import tiger as t
# t.f01()

# 실행 되고 있는 곳이 어디 인지 알려줌
# print(__name__)
#
# import tiger as t
# t.f01()
# t.f02()     # 외부에서 끌어왔기 때문에 파일명이 출력되게 된다.

# tiger 파일과 연계하여 볼 것
# 연관 if __name__ == __main__
# import tiger as t
# if __name__ == '__main__':
#     t.f01()

# Entry point
# def main():
#     print(1)
#     f01()
#
#
# if __name__ == '__main__':
#     main()
#
#
# def f01():
#     print('H')

# Dictionary 복습
# Apple = {'n1': '호랑이', 'n2': '코끼리', 'n3': '독수리'}
# print(Apple['n3'])
# 
# Orange = {10: 20, 20: '독수리', 30: True}
# print(Orange[10])

# Kiwi = {'이름': '홍길동',
#         '나이': 20,
#         '특기': ['독서', 'SkateBoard', '프로그래밍'],
#         '가족': {'아버지': '아빠', '어머니': '엄마'}}
#
# print(Kiwi['이름'], Kiwi['나이'])
# print(Kiwi['특기'][1])
# print(Kiwi['가족']['어머니'])    # 중첩 Dictionary 출력

# 예제
# data = {
#     "response":{
#         "body":{
#             "items":[{
#                     "addr":1234,
#                     "name":"홍길동"
#                 },
#                 "득템"
#             ]
#         },
#         "page":100
#     },
#     "header":{
#         "result":200,
#         "msg":"OK"
#     }
# }
#
# print(data['response']['body']['items'][0]['addr'])
# print(data['response']['body']['items'][0]['name'])
# print(data['response']['body']['items'][1])
# print(data['response']['page'])
# print(data['header']['result'])
# print(data['header']['msg'])

# Dictionary 복습 : .get
# Apple = {'n1': '호랑이', 'n2': '코끼리', 'n3': '독수리'}
# Orange = {10: 20, 20: '독수리', 30: True}
#
# print(Apple.get('n1'))
# print(Orange.get(30))
#
# try:
#     print(Apple['n4'])
# except:
#     print('Error: 검색하지 못했습니다')
#
# num = Apple.get('n4')
# if num == None:
#     print('Error: 검색하지 못했습니다.')
# else:
#     print(num)


# 함수의 Return
# a = [10, 20, 30, 40]
# print(sum(a))
# print(sum([1, 2, 3, 4]))
#
# a = sum([3, 4, 5, 6])
# print(a)

# Filter 함수 : Filter(함수명, 리스트) : 해당 하지 않는 값을 걸러준다
# def f01(a):
#     return a > 0
#
# a = list(filter(f01,[-2, -1, 0, 1, 2]))
# print(a)

# 함수 참조와 함수 호출 : () 유무에 따라
# def f01():
#     print(1)
#
# f01()  # () 를 넣으면 호출
# a = f01  # a는 함수 f01과 같다(공유, 참조)
# a()
#
# def f02():
#     print(2)
#
# def f03(tt):
#     tt()
#     print(3)
#
# f03(f02)    # tt = f02 : tt 인수가 함수가 됨
#
# def f04():
#     return 999
#
# def f05(ss):
#     print(ss)
#
# f05(f04())

# Python 에서의 Switch
# def f01(num):
#     t = {10: '호랑이', 20: '독수리', 30: '앵무새'}
#     return t[num]
#
# print(f01(10))

# List 에 반복문( for ) 사용하기 : Comprehension
# a = [i for i in range(5)]   # for 문의 결과를 for 앞 쪽의 i 에 저장한다
# print(a)
#
# a = [i * 3 for i in range(5)]
# print(a)

# 반복문과 조건문을 사용하여 List 를 생성하는 것을 Comprehension 이라고 한다.
# a = [10, 20, 30, 40]
# b = [i * 3 for i in a]
# print(b)

# a = [10, 20, 30, 40]
# # 조건문 추가 : for 문의 i 중 if 를 만족시키는 값만 저장한다.
# b = [i + 2 for i in a if i > 25]
# print(b)

# dir() : 사용 가능 한 함수를 알려줌
# print(dir())

# List 복습
# a = [10, 20, 30, 40]
# a.insert(3, 99)    # Insert 함수 : 지정 위치에 값을 추가 한다.
# a.append('호랑이')    # Append 함수 : 리스트의 마지막에 값을 추가 한다.
# a.insert(len(a), 99)    # Append 화 동일한 의미를 지님

# a.extend([50, 60])    # Extend 함수 : a + [50, 60] 과 같은 의미(합의 개념)

# b = a   # 동일한 객체
# c = a.copy()    # Copy 함수 : 새로운 객체
# print(a, b, c)
# a[0] = 99
# print(a[0], b[0], c[0])
# print(id(a), id(b), id(c))

# a.clear()    # Clear 함수 : 다 지워라~

# a = [10, 20, 30, 40, 10]
# a.remove(10)    # 목록에 없으면 Error 발생 : 예외처리 필수
#                 # 중복 값이 있더라도 첫 번째 값이 삭제 된다.

# del(a[2])    # Del 함수 : 해당 값을 삭제시킨다

# b = a.pop(2)    # Pop 함수 : 해당 위치의 값을 Return 하고 List 에서 삭제시킴
# print(b)        # default 값은 마지막 값임
# print(a)

# a = [0, 3, 6, 9, 0, 3, 6, 9]
# def f01(ss):
#     return a != 6
#
# print(list(filter(f01,a)))    # Return 값이 있는 함수만 사용이 가능하다