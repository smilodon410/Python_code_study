import numpy as np
from numpy.linalg import inv, qr, solve
import math
import random

# 행렬의 곱셈
# x = np.array([[1, 2, 3], [4, 5, 6]])
# y = np.array([[6, 23], [-1, 7], [8, 9]])
#
# print(x)
# print('-' * 50)
# print(y)
# print('-' * 50)
#
# print(x.dot(y))
# print('-' * 50)
#
# print(np.dot(x, y))
# print('-' * 50)
#
# print(np.dot(x, np.ones(3)))
# print('-' * 50)
# print(np.ones(3))
# print(x @ np.ones(3))


# linalg 함수
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(x.T)  # .T = 대각을 중심으로 값의 위치를 변경한다
#
# mat = x.T.dot(x)
#
# inv(mat)  # 정사각 행렬의 역행렬을 구해준다
#
# mat.dot(inv(mat))
#
# q, r = qr(mat)

# a = np.array([1, 2, 3])
# print(np.diag(a))   # a 를 대각으로 하고 나머지를 0으로 채운 단위 행렬을 반환한다
#
# print(np.trace(np.diag(a)))    # 행렬 대각의 합을 구해준다

# c = inv(np.diag(a))
# print(c)


# a = [[1, 2], [3, 4]]
# b = [[2, 3], [4, 5]]
#
# c = solve(a, b)   # a 가 정사각형 행렬일 때, a * x = b 를 만족시키는 x 값 반환
# print(c)


# solve 함수 예시
# a = [[2, 3], [3, 1]]
# b = [[5], [2]]
#
# c = solve(a, b)
# print(c)


# 사각형의 이동
import matplotlib.pyplot as plt

# x = [10, 20, 20, 10, 10]
# y = [10, 10, 20, 20, 10]
#
# dx = 50
# dy = 30
#
# c = []
# d = []
#
# for i in range(len(x)):
#     e = x[i]
#     f = y[i]
#     a = [[1, 0, dx], [0, 1, dy], [0, 0, 1]]
#     b = [[e], [f], [1]]
#     t = np.dot(a, b)
#     c.append(t[0])
#     d.append(t[1])


# 회전하는 사각형( 원점을 기준으로, 각도는 30으로 고정 )
# c1 = []
# d1 = []
#
# for i in range(len(x)):
#     e = x[i]
#     f = y[i]
#
#     a1 = [[np.sqrt(3)/2, -1/2, 0], [1/2, np.sqrt(3)/2, 0], [0, 0, 1]]
#     b1 = [[e], [f], [1]]
#     t = np.dot(a1, b1)
#     c1.append(t[0])
#     d1.append(t[1])


# # 제자리에서 회전한 사각형하기
# x1 = [-5, 5, 5, -5, -5]
# y1 = [-5, -5, 5, 5, -5]
#
# c2 = []
# d2 = []
#
# 원점에서 회전
# for i in range(len(x)):
#     e = x1[i]
#     f = y1[i]
#
#     # print(math.radians(30)) # sin30
#     a1 = [[np.sqrt(3)/2, -1/2, 0], [1/2, np.sqrt(3)/2, 0], [0, 0, 1]]
#     b1 = [[e], [f], [1]]
#     t = np.dot(a1, b1)
#     c2.append(t[0])
#     d2.append(t[1])
#
# # 회전한 사각형을 이동
# for i in range(len(c2)):
#     c2[i] = c2[i] + 15
#     d2[i] = d2[i] + 15


# Scale (?)
# c3 = []
# d3 = []
#
# for i in range(len(x)):
#     e = x1[i]
#     f = y1[i]
#     sx = 2
#     sy = 2
#     a3 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
#     b3 = [[e], [f], [1]]
#     t = np.dot(a3, b3)
#     c3.append(t[0])
#     d3.append(t[1])


# 그래프 구하기
# plt.plot(x, y)
# plt.plot(x1, y1)    # 원점 사각형
# plt.plot(c, d)      # 사각형 이동
# plt.plot(c1, d1)    # 원점기준 회전한 사각형
# plt.plot(c2, d2)    # 회전 사각형 이동
# plt.plot(c3, d3)    # scale
#
# plt.xlim(-50, 100)
# plt.ylim(-50, 100)
#
# plt.show()


# 함수 만들기
# def square(x, y, sx, sy, degree, dx, dy):
#     c = []
#     d = []
#     for i in range(len(x)):
#         e = x[i]
#         f = y[i]
#         a3 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
#         b3 = [[e], [f], [1]]
#         t = np.dot(a3, b3)
#         c.append(t[0])
#         d.append(t[1])
#
#     for i in range(len(x)):
#         e = c[i]
#         f = d[i]
#         a1 = [[math.cos(math.radians(degree)), -math.sin(math.radians(degree)), 0],
#               [math.sin(math.radians(degree)), math.cos(math.radians(degree)), 0],
#               [0, 0, 1]]
#         b1 = [[e], [f], [1]]
#         t = np.dot(a1, b1)
#         c[i] = t[0]
#         d[i] = t[1]
#
#     for i in range(len(x)):
#         e = c[i]
#         f = d[i]
#         a = [[1, 0, dx], [0, 1, dy], [0, 0, 1]]
#         b = [[e], [f], [1]]
#         t = np.dot(a, b)
#         c[i] = t[0]
#         d[i] = t[1]
#
#     return c, d
#
# x, y = square([-5, 5, 5, -5, -5], [-5, -5, 5, 5, -5], 2, 2, 30, 15, 15)
#
# plt.plot([-5, 5, 5, -5, -5], [-5, -5, 5, 5, -5])
# plt.plot(x, y)
#
# plt.xlim(-10, 50)
# plt.ylim(-10, 50)
#
# plt.show()


# 별 그리기
# x = 0
# y = 20
#
# a = []
# b = []
#
# a.append(x)
# b.append(y)
#
# for i in range(5):
#     degree = (144 * (i + 1))
#     c = [[math.cos(math.radians(degree)), -math.sin(math.radians(degree)), 0],
#          [math.sin(math.radians(degree)), math.cos(math.radians(degree)), 0],
#          [0, 0, 1]]
#     d = [[x], [y], [1]]
#     t = np.dot(c, d)
#     a.append(t[0])
#     b.append(t[1])
#
#
# plt.plot(a, b)
#
# plt.xlim(-50, 50)
# plt.ylim(-50, 50)
#
# plt.show()

# x = 0
# y = 2
#
# a = []
# b = []
#
# a.append(x)
# b.append(y)
#
# for i in range(5):
#     degree = (144 * (i + 1))
#     c = [[math.cos(math.radians(degree)), -math.sin(math.radians(degree))],
#          [math.sin(math.radians(degree)), math.cos(math.radians(degree))]]
#     d = [[x], [y]]
#     t = np.dot(c, d)
#     a.append(t[0])
#     b.append(t[1])
#
#
# plt.plot(a, b)
#
# plt.xlim(-50, 50)
# plt.ylim(-50, 50)
#
# plt.show()


# 사각형의 교차여부 확인시켜주기(조건 넣기 xy1 < xy2)
# xy1 = random.randint(1, 50)
# xy2 = random.randint(1, 50)
# xy3 = random.randint(1, 50)
# xy4 = random.randint(1, 50)
#
# ab1 = random.randint(1, 50)
# ab2 = random.randint(1, 50)
# ab3 = random.randint(1, 50)
# ab4 = random.randint(1, 50)
#
# x = [0, 0, 0, 0, 0]
# y = [0, 0, 0, 0, 0]
# a = [0, 0, 0, 0, 0]
# b = [0, 0, 0, 0, 0]
#
#
# x[0] = x[3] = x[4] = xy1
# x[1] = x[2] = xy2
# y[0] = y[1] = y[4] = xy3
# y[2] = y[3] = xy4
#
# a[0] = a[3] = a[4] = ab1
# a[1] = a[2] = ab2
# b[0] = b[1] = b[4] = ab3
# b[2] = b[3] = ab4
#
#
# if a[2] < x[0] or b[2] < y[0] or a[0] > x[2] or b[0] > y[2]:
#     print('교차하지 않습니다')
# else :
#     print('교차합니다')
#
# plt.plot(x, y)
# plt.plot(a, b)
#
# plt.xlim(0, 100)
# plt.ylim(0, 100)
#
# plt.show()
