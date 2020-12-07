# # Casting
# print(65)
# # chr : 숫자 -> 문자
# print(chr(65))
# # ord : 문자 -> 숫자
# print(ord('B'))

# # List
# # C : List 생성
# a = [10, 20, 30, 40]
# print(a)
#
# b = ['호랑이', '코끼리', '독수리']
# print(b)
#
# c = [10, '호랑이', 3.14, True]    # 서로 다른 타입도 가능함
# print(c)

# R : List Reading
# a = [10, 20, 30, 40]
# print(a)
# print(a[0], a[1], a[2], a[3])
# # print(a[4])    # Error : out of bound
# print(a[:2])

#
# for i in a:
#     print(i, end=' ')
# print('')
#
# for value in a:
#     print(value, end=' ')
# print('')
#
# for item in a:
#     print(item, end=' ')
# print('')
#
# for data in a:
#     print(data, end=' ')
# print('')

# U : List Update
# a = [10, 20, 30, 40]
# a[0] = 50
# print(a)
# # 기존 주소가 변경 되었음 : 기존 데이터를 삭제 후 새 값을 넣음 => Update
# print(id(a[0]), id(a[1]))
# a[0] = 60
# print(id(a[0]), id(a[1]))

# D : List Delete
# a = [10, 20, 30, 40]
# del(a[0])
# print(a)

# List 의 길이 구하기 : 총 갯수
# a = [10, 20, 30, 40]
# print(len(a))

# 중첩 List
# a = [10, '호랑이', [20, '코끼리',[30, '독수리']]]
# print(a)
# print(a[2][1])    # 2차원 : List 가 두개
# print(a[2][2][1])    # 3차원 : List 가 3개

# 문자열과 List 의 차이
# a = 'Apple'
# b = ['A', 'p', 'p', 'l', 'e']
# print(a)
# print(b)
#
# print(a[0])    # a[0] = 'B' 오류 : 문자열은 수정이 불가
# print(b[0])    # b[0] = 'B' 수정 가능

# ':'을 활용한 방법
# a = ['a', 'b', 'c', 'd', 'e']
# print(a[1:3])
#
# a[1:3] = ['F','G']
# print(a)
#
# a[1:3] = ['H', 'I', 'J', 'K', 'L']    # 삭제 후 입력 = 갯수가 정확하지 않아도 괜찮아~
# print(a)

# ':'을 활용한 특정부분 삭제
# a = ['a', 'b', 'c', 'd', 'e']
# a[1:3] = []    # 엄밀하게 말하면 삭제가 아닌 추가할 내용이 없는 것
# print(a)
#
# a = ['a', 'b', 'c', 'd', 'e']
# del(a[1:3])    # 정확한 삭제 방법
# print(a)

# Append 함수 : List 에 추가
# a = ['Orange']
# print(a)
# a.append('Banana')
# print(a)
# a.append(10)
# print(a)

# Insert 함수 : 원하는 위치에 추가
# a = ['Orange']
# a.insert(0, 10)    # .insert( 인덱스 번호(원하는 위치), 입력 값)
# print(a)
# append 와 insert 는 속도에서 차이가 난다 : 연결고리 문제
# 보통 마지막에 데이터를 추가한다는 가정하에 append 를 사용

# Pop 함수 : 무조건 제일 마지막 값을 제거함
# a = ['Orange', 'Banana', 'Apple']
# a.pop()
# print(a)
#
# a.pop(0)    # 인덱스 번호를 삽입하였을 때 원하는 값을 제거 가능
# print(a)

# Remove 함수 : 검색을 해서 값을 삭제하게 됨, 중복 된 값이 있으면 제일 앞 값만 삭제하게 됨
# a = ['O','r', 'a', 'n', 'r', 'e']
# a.remove('r')
# print(a)
# 찾지 못할 상황에 대하여 예외처리( Exception )를 하게 된다.

# 예외 처리( try - exception )
# a = ['O', 'r', 'a', 'n', 'r', 'e']
# try:
#     a.remove('t')
# except:
#     print('Error : Occur Exception!!')
#     pass
# print('Escape Success!!')

# Index 함수 : Return 값이 있다: 해당 값의 위치를 알려줌
# a = ['O','r', 'a', 'n', 'r', 'e']
# b = a.index('r')
# print(b)

# Sort 함수 : 순서대로 나열해줌(비용이 많이 든다 : 시간↑) : '메모리 > 속도' 중시
# a = ['O','r', 'a', 'n', 'g', 'e']
# a.sort()
# print(a)
# # Reverse 함수 : 역순으로 나열해준다.
# a.reverse()
# print(a)

# Reverse 함수 사용시 유의 사항
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.sort()
# print(a)
#
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.reverse()
# print(a)    # 역순정렬이 아닌 인덱스의 처음과 끝의 자리를 바꿔줌
#             # 이미 순차 정렬이 된 상태에서 사용했을 시 역순정렬
#
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.sort(reverse=True)    # 역순정렬의 형태
# print(a)

# Append 와 Extend : 1개 추가, 합치기
# a = [1, 2, 3]
# a.append(4)
# print(a)
#
# a = [1, 2, 3]
# a.append([4,5])
# print(a)    # List 를 하나의 데이터로 받는다.
#
# a = [1, 2, 3]
# a.extend([4])
# print(a)
#
# a = [1, 2, 3]
# a.extend([4,5,6])
# print(a)    # 두개의 List 를 하나의 List 로 합친다.
#
# a = [1, 2, 3]
# a = a + [4, 5, 6]
# print(a)    # 합 연산 가능