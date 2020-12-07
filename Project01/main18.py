import numpy as np

# # 파이썬 스위치
# def f1(n):
#     a = {10: '호랑이', 20: '독수리'}
#     print(a[n])

# 스위치에서 함수 호출
# def f02():
#     print('나는 구구단')
#
#
# def f03():
#     print('나는 합산')
#
#
# def f04(n):
#     b = {10: f02, 20: f03}
#     b[n]()
#
#
# f04(20)


# Exclusive Or
# print(False ^ False)
# print(True ^ False)
# print(True ^ True)


# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
#
# b = a * 2
# print(b)


# a = np.random.randn(3, 4)
# print(a)
# print('-' * 50)
#
# print(a.shape)
# print(a.dtype)
#
# # 배열의 차원 묻기
# print(a.ndim)
# print('-' * 50)
#
#
# print(np.zeros(5))
# print('-' * 50)
#
# print(np.zeros((2, 3, 2)))
# print('-' * 50)

# np.array 사칙연산
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[2, 3, 4],[5, 6, 7]])
# print(a)
# print(b)
# print('-' * 50)
#
# print(a + b)
# print('-' * 50)
#
# print(a - b)
# print('-' * 50)
#
# print(a * b)
# print('-' * 50)
#
# print(a / b)
# print('-' * 50)
#
# print(a // b)
# print('-' * 50)
#
# print(a % b)
# print('-' * 50)
#
# print(1 / a)
# print('-' * 50)

# a = np.array(['호랑이', '코끼리', '독수리'])
# print(a == '호랑이')
#
# print(a != '호랑이')
#
# b = a == '호랑이'
# print(a[~b])

# a = np.arange(32)
# print(a)
#
# b = a.reshape(4, 8)
# print(b)

# a = np.array([-10, 0, 10])
# print(np.sign(a))

# a = np.array([1, 2, 3])
# b = np.array([2, 3, 4])
#
# c = np.add(a, b)
# print(c)

# imshow
# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
#
# z = np.sqrt(xs ** 2 + ys ** 2)
#
# import matplotlib.pyplot as plt
#
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
#
# plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a gird of value')
#
# plt.show()


a = np.arange(10)
np.save('some_array', a)

b = np.load('some_array.npy')
print(b)

