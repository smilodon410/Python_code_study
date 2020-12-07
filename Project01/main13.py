from collections import Counter
import matplotlib.pyplot as plt
import math
from enum import Enum
import random

# nf = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15,
#       15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10,
#       10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#       10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
#       9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7,
#       7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
#       6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5,
#       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4,
#       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3,
#       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
#       3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#       1, 1, 1, 1
#       ]


# 히스토그램
# fc = Counter(nf)
# xs = range(101)
# ys = [fc[i] for i in xs]
#
# plt.bar(xs, ys)
# plt.axis([0, 100, 0, 25])
#
# plt.show()

# 기본 통계
# np = len(nf)
# print(np)
#
# maxf = max(nf)
# minf = min(nf)
# print(maxf, minf)
#
# sv = sorted(nf)
# maxf = sv[-1]
# minf = sv[0]
# print(maxf, minf)
#
#
# # 평균
# def mean(avg):
#     return sum(avg) / len(avg)
#
#
# print(mean(nf))


# 중앙값
# def median(a):
#     sr = sorted(a)
#     mid = len(sr) // 2
#     return (sr[mid - 1] + sr[mid]) / 2 if len(sr) % 2 == 0 else sr[mid]
#
#
# print(median(nf))


# 분위
# def quantile(a, f):
#     index = int(f * len(a))
#     return sorted(a)[index]
#
#
# print(quantile(nf, 0.75))


# 최빈값
# def mode(a):
#     counts = Counter(a)
#     mc = max(counts.values())
#     return [i for i, count in counts.items()
#             if count == mc]
#
#
# print(mode(nf))


# 편차 구하기 : 변위 - 평균 = 편차
# a = [1, 2, 3, 4, 5]     # 데이터를 변위라고 한다.
# b = sum(a)/len(a)       # 평균
#
# c = [a[i] - b for i in range(len(a))]    # 편차
# # print(c)
#
# # 평균 편차: 편차 절대값의 합의 평균
# d = [abs(c[i]) for i in range(len(c))]
# adev = sum(d) / len(d)
# # print(adev)
#
# # 분산 : 편차 제곱의 합의 평균
# f = [pow(c[i], 2) for i in range(len(c))]
# var = sum(f)/len(f)
# print(var)
#
# # 표준 편차
# stdev = sqrt(var)
# print(stdev)


# 조건부 확률
# class Kid(Enum):
#     Boy = 0
#     Girl = 1
#
# def rk():
#     return choice([Kid.Boy, Kid.Girl])
#
# both_girls = 0
# older_girl = 0
# either_girl = 0
#
# seed(0)
#
# for _ in range(10000):
#     younger = rk()
#     older = rk()
#     if older == Kid.Girl:
#         older_girl += 1
#     if older == Kid.Girl and younger == Kid.Girl:
#         both_girls += 1
#     if older == Kid.Girl or younger == Kid.Girl:
#         either_girl += 1
#
#
# print("P(both | older):", both_girls / older_girl)
# print("P(both | either):", both_girls / either_girl)


# 예제 프로그램
# count = 0
# count1 = 0
#
# for i in range(100000):
#     a = []
#     b = random.randint(1, 10)
#     for c in range(2):
#         while b in a:
#             b = random.randint(1, 10)
#         a.append(b)
#     d = sorted(a)
#     while True:
#         x = []
#         y = random.randint(1, 10)
#         for z in range(2):
#             while y in x:
#                 y = random.randint(1, 10)
#             x.append(y)
#         t = sorted(x)
#         if d == t:
#             break
#         else:
#             count += 1
#
#     sum = count + count1
#     count1 = sum
#     count = 0
#
# print(count1 / 100000)


# 정규 분포
# SQRT_TWO_PI = math.sqrt(2 * math.pi)
#
# def normal_pdf(x, m, s):
#     return (math.exp(-(x-m)**2/2/s**2)/(SQRT_TWO_PI*s))
#
# xs = [x / 10.0 for x in range(-50, 50)]
#
# plt.plot(xs,[normal_pdf(x, 0, s=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs,[normal_pdf(x, 0, s=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs,[normal_pdf(x,0, s=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs,[normal_pdf(x, m=1, s=1) for x in xs], '-.', label='mu=1, sigma=1')
#
# plt.legend()
# plt.show()