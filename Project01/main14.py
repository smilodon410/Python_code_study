import matplotlib.pyplot as plt

# x = [2, 4, 6, 8]
# y = [81, 93, 91, 97]
# l = ['tiger', 'eagle', 'elephant', 'dog']

# plt.scatter(x, y)
# plt.axis([1, 9, 70, 100])
#
# for label, fc, mc in zip(l, x, y):
#     plt.annotate(label,
#                  xy=(fc, mc),
#                  xytext=(5, -5),
#                  textcoords='offset points')
#
# plt.xlabel('Time')
# plt.ylabel('Score')
# plt.title('Score compare with Time')
#
# plt.show()

# 최소 제곱법
# a = ([x[i] - (x의 평균)] * [y[i] - (y의 평균)])의 합 / ([x[i] - (x의 평균)]의 제곱)의 합

# avx = sum(x)/len(x)
# avy = sum(y)/len(y)
#
# x1 = [x[i] - avx for i in range(len(x))]
# y1 = [y[i] - avy for i in range(len(y))]
# xy = sum([x1[i] * y1[i] for i in range(len(x))])
#
# sqx = sum([x1[i] ** 2 for i in range(len(x))])
#
# a = xy/sqx
# print(a)


# 최소 제곱근 : 라이브러리 사용
import numpy as np

# mx = np.mean(x)
# my = np.mean(y)
#
# t1 = sum([(i - mx) * (j - my) for i, j in zip(x, y)])
# t2 = sum([(i - mx)**2 for i in x])
#
# a = t1 / t2
# b = my - (mx * a)
# print(a, b)

# 선형 회귀
# c = [a*i + b for i in range(10)]
#
# plt.scatter(x, y)
# plt.plot(range(10), c)
# plt.axis([0, 9, 70, 100])
#
# for label, fc, mc in zip(l, x, y):
#     plt.annotate(label,
#                  xy=(fc, mc),
#                  xytext=(5, -5),
#                  textcoords='offset points')
#
# plt.xlabel('Time')
# plt.ylabel('Score')
# plt.title('Score compare with Time')
#
# plt.show()


# 평균 제곱 오차 : 선형회귀가 가지는 오차
# y = [81, 93, 91, 97]    # 실제값
# z = [83.6, 88.2, 92.8, 97.4 ]   # 예측값
#
# # mean(sum(예측값 - 실제값) ** 2)
# e = [z[i] - y[i] for i in range(len(z))]
# f = sum([i ** 2 for i in e])/len(e)
# print(f)


# 기울기에 따라 달라지는 오차를 확인
# a = 2.4
# b = 79.0
# c = [a*x[i] + b for i in range(len(x))]
#
# e = [c[i] - y[i] for i in range(len(c))]
# f = sum([i ** 2 for i in e])/len(e)
# print(f)


# 2차 방정식 그래프
# a = [i for i in np.arange(0, 4.7, 0.1)]
# er = []
# for i in range(len(a)):
#     a1 = a[i]
#     b = 79.0
#     c = [a1*x[i] + b for i in range(len(x))]    # 예측값
#     e = [c[i] - y[i] for i in range(len(c))]    # 예측 - 실제
#     f = sum([i ** 2 for i in e])/len(e)         # 오차
#     er .append(f)
#
# plt.plot(a, er)
# plt.show()


# 코드 공부 하기!
# xdata = np.array(x)
# ydata = np.array(y)
# print(type(xdata), xdata) # 배열이다.
# a = 0; b = 0
# lr = 0.05 # 확습률
# for i in range(1000):
#     y = a * xdata + b
#     a_dif = -(1 / len(xdata)) * sum(xdata * (ydata-y))
#     b_dif = -(1 / len(xdata)) * sum(ydata - y)
#     a = a - lr * a_dif
#     b = b - lr * b_dif
#     print(i, round(a,3), round(b,3))
