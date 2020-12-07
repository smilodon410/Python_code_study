# 벡터
# 벡터의 합
# 벡터의 차
# 내적(Dot Product) : 양수, 0, 음수에 따라 각을 알 수가 있음
# 외적
# 벡터 스케일
# 스칼라
# 벡터의 길이 : 피타고라스 정리
# 단위 벡터 : 벡터의 거리가 1인 벡터


# 벡터의 합
# def add(a, b):
#     c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
#     return c
#
#
# print(add([1, 2, 3], [4, 5, 6]))
#
#
# def add01(a, b):
#     return [a_i + b_i for a_i, b_i in zip(a, b)]
#
#
# print(add01([1, 2, 3], [4, 5, 6]))
#
#
# # 벡터의 차
# def minus(a, b):
#     c = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
#     return c
#
#
# print(minus([1, 2, 3], [4, 5, 6]))
#
#
# def minus01(a, b):
#     return [a_i - b_i for a_i, b_i in zip(a, b)]
#
#
# print(minus01([1, 2, 3], [4, 5, 6]))
#
#
# # 모든 벡터의 합
# def vsum(a):
#     num = len(a[0])
#     return [sum(b[i]
#             for b in a)
#             for i in range(num)]
#
#
# print(vsum([[1, 2], [3, 4], [5, 6], [7, 8]]))
#
#
# # 스칼라 곱셈
# def smul(c, v):
#     return [c * i for i in v]
#
#
# print(smul(2, [1, 2, 3]))
# print(smul(0.5, [2, 4, 6]))
#
#
# # 벡터의 평균
# def vmean(v):
#     n = len(v)
#     return smul(1/n, vsum(v))
#
#
# print(vmean([[1, 2], [3, 4], [5, 6]]))
#
#
# # 벡터의 내적
# def dot(v, w):
#     return sum(i * j for i, j in zip(v, w))
#
#
# print(dot([1, 2, 3], [4, 5, 6]))
#
#
# # 벡터의 크기?
# import math
#
#
# def vmag(v):
#     return math.sqrt(dot(v, v))
#
#
# print(vmag([3, 4]))
#
#
# # 벡터의 차를 이용하여 벡터의 크기 구하기
# def dist(v, w):
#     return vmag(minus01(v, w))
#
#
# print(dist([1, 1], [4, 5]))


# 행렬

# A = [[1, 2, 3],
#      [4, 5, 6]]
# B = [[1, 2],
#      [3, 4],
#      [5, 6]]
#
#
# def shape(a):
#     r = len(a)
#     c = len(a[0])
#     return r, c
#
#
# print(shape(A))
#
#
# # row 구하기
# def getrow(a, i):
#     return a[i - 1]


# print(getrow(A, 0))


# column 구하기
# def getcol(a, j):
#     return [c[j] for c in a]


# print(getcol(B, 0))


from typing import Callable


# 행렬 만들기
# def make(r, c, m):
#     return [[m(i, j) for i in range(c)]
#             for j in range(r)]
#
#
# def iden_mat(r, c):
#     return make(r, c, lambda i, j: 1 if i == j else 0)
#
#
# for i in iden_mat(5, 5):
#     print(i)



# 행렬의 곱

# A = iden_mat(3, 2)
# B = iden_mat(2, 3)
#
#
# for i in A:
#     print('')
#     for j in range(len(B[0])):
#         C = getcol(B, j)
#         d = dot(i, C)
#         print(d, end=' ')


# 행렬의 곱(내꺼)
# def mulmat(A, B):
#     for i in A:
#         print('')
#         for j in range(len(B[0])):
#             C = getcol(B, j)    # getcol 함수 호출
#             d = dot(i, C)   # dot 함수 호출
#             print(d, end=' ')

# a = [[1, 2],
#      [3, 4],
#      [5, 6]]
# b = [[1, 2, 3],
#      [4, 5, 6]]
#
# mulmat(a, b)