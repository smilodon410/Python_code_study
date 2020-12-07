# Tuple
# a = ()
# b = []    # List
#
# print(a, b, type(a), type(b))
#
# # ','차이에 따라 튜플이나 아니야가 결정 : 기본형 = b
# a = 10,    # 괄호 생략
# print(type(a))
#
# b = (10,)
# print(type(b))
#
# c = 10
# d = (10)
# print(type(c), type(d))

# f = 10, 20, 30    # Tuple 형 : '()' 생략
# print(type(f))

# a = (10, 20, 30)
# b, c, d = a
# print(a, b, c, d)
#
# a = [10, 20, 30]
# b, c, d = a
# print(a, b, c, d)

# a = 10
# b = 20
# a, b = b, a    # Swap 시키기
# print(a, b)
#
# a = [10, 20, 30]
# b = tuple(a)    # List 자료형을 Tuple 로 변환시키는 함수 : Return 값이 있다
# print(type(b))
#
# a = (10,) + (20, 30)    # Tuple 끼리의 결합
# print(a)
# print((10,) + (20, 30))

# Tuple 비교
# a = (1, 2, 3)
# b = (1, 4)
# print(a == b)

# Tuple 과 List
# a = (10, 20, 30)
# b = [10, 20, 30]
# # print(a(0))    # Error!
# print(a[0])    # List 와 같은 방식으로 사용
#
# # a[0] = 40    # Tuple 은 수정 불가
# b[0] = 40    # List 는 수정 가능
# print(a, b)

# List and Tuple
# a = [10, '호랑이', [20, 30], (40, '코끼리', [50, 60])]
# print(a)
#
# a = []
# b = list()
# print(type(a), type(b))
#
# c = ()
# d = tuple()
# print(type(c), type(d))
#
# e = [10, 20]
# f = list('Apple')    # Tuple 을 List 로 변환해줌
# print(e, f)

# Type 변환
# a = []
# b = tuple(a)
# c = list(b)
# print(type(a), type(b), type(c))

# Split 함수
# a = '호 랑이'
# b = a.split()
# print(b)

# Offset : 기준점으로부터 상대적으로 떨어진 거리
# 배열에서 Index 와 같은 말

# Index < 0 : 역순
# a = [10, 20, 30]
# print(a[-1], a[-2], a[-3])

# Dictionary : a = {(k:v), (k:v), ... }
    # Key 로 값을 찾기때문에 Index 가 없다
# a = {1:10, 2:20, 3:30, 4:40}
# print(type(a))
# print(a)

# a = {10:'호랑이', 20:'코끼리', 30:'독수리'}
# print(a)

# Key 가 중복될 경우 최근에 변경된 값으로 출력된다
# a = {1:10, 2:20, 2:30, 4:40}
# print(a)

# Dictionary 의 다양한 형태 : Key 값은 가급적 통일
# a = {1: list('10'), 2: list('20'), 3: list('30')}
# print(a)
#
# a = {1: tuple('10'), 2: tuple('20'), 3: tuple('30')}
# print(a)
#
# a = {1: 10, 2: '호랑이', 3: list('Apple'), 4: tuple('40'), 5: {}}
# print(a)
#
# a = {'호랑이': 10, '코끼리': 20, '독수리': 30}
# print(a)

# JSON 에 맞춰 만들었기에 형태가 유사
# a = {'Name': '홍길동', 'Age': 20, 'Salary': 300}

# Update : Data 갱신
# a = {'Name': '홍길동', 'Age': 20}
#
# a['Name'] = '이순신'
# print(a)
# print(a['Name'], a['Age'])
#
# Insert : Data 추가 = 키가 없으면 새로운 값으로 추가 ( 있으면 갱신 )
# a['Height'] = 100
# print(a)

# # Dictionary Create
# a = {'Name': '이순신', 'Age': 20}
# print(a)
# # Dictionary Reading
# b = a['Name']
# print(b, a['Name'])
# # Dictionary Update
# a['Name'] = '홍길동'
# print(a)
# # Dictionary Delete
# del a['Age']    # 예약어
# print(a)
#
# del(a ['Age'])    # 함수를 생성
# print(a)

# Get 함수
# a = {'Name': '홍길동', 'Age': 20, 'Salary': 300}
# b = a['Name']
# c = a.get('Name')
# print(b, c)

# Key 함수 : Key 값 출력
# print(a.keys())

# Item 함수 : Key 와 Value 를 Tuple 형태로 담아줌
# for item in a.items():
#     print(item)    # Tuple 로 출력함
#     print(item[0], item[1])    # 데이터 값을 하나씩 출력함
#
# values 함수 : value 값을 출력
# for i in a.values():
#     print(i)

# 참조
# a = [10, 20, 30]
# b = a
# print(id(a))
# print(id(b))
# a[0] = 4
# b[2] = 5
# print(a, b)
# a.append(99)
# print(a, b)

# Copy() : 얕은 복사 = 하위 값의 메모리는 공유하나, 상위 값은 새로운 메모리를 할당받음

# Deepcopy : 깊은 복사 = 서로 다른 메모리를 가지게 됨
# a = [10, 20, 30]
# b = a[:]
# print(id(a))
# print(id(b))
# a[0] = 4
# b[2] = 5
# print(a, b)
# a.append(99)
# print(a, b)

# import copy
# a = {1: 100, 2: 200, 3: 300}
# b = copy.deepcopy(a)
# print(id(a), id(a[1]))
# print(id(b), id(b[1]))


