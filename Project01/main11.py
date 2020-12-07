# 시각화
from matplotlib import pyplot as plt

# 선형 그래프
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.2, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
#
# plt.title('Nominal GDP')
#
# plt.ylabel('Billions of $')
#
# plt.xlabel('year')
#
# plt.show()


# 막대그래프
# movies = ['Annie Hall', 'Ben-hur', 'Casablanca', 'Gandhi', 'West Side Story']
# num_oscars = [5, 11, 3, 8, 10]
#
# plt.bar(range(len(movies)), num_oscars)
#
# plt.title('My Favorite Movies')
# plt.ylabel('# of Academy Awards')
#
# plt.xticks(range(len(movies)), movies)
#
# plt.show()


from collections import Counter
# 히스토그램
# grades= [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
#
# # 바에 들어갈 값을 구해준다 : Counter 활용
# histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
# print(histogram)
# # bar(바의 위치, 바의 높이, 바의 너비, 막대의 테두리 색)
# plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))
#
# plt.axis([0, 100, 0, 5])    # x 축, y 축의 값(최소, 최대)
# plt.xticks([10 * i for i in range(11)])
#
# plt.xlabel('Decline')
# plt.ylabel('# of Student')
# plt.title('Distribution of Exam 1 Grades')
#
# plt.show()


# 다중 선형 그래프
# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]
# print(xs)
#
# plt.plot(xs, variance, 'g-', label='variance')
# plt.plot(xs, bias_squared, 'r-.', label='bias^2')
# plt.plot(xs, total_error, 'b:', label='total error')
#
# plt.legend(loc=9)
#
# plt.xlabel('model complexity')
# plt.xticks([])
# plt.title('The Bias-Variance TradeOff')
# plt.show()


# 산점도
# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# plt.scatter(friends, minutes)
#
# for label, fc, mc in zip(labels, friends, minutes):
#     plt.annotate(label,
#                  xy=(fc, mc),
#                  xytext=(5, -5),
#                  textcoords='offset points')
#
# plt.title('Daily Minutes vs. Number of Friends')
# plt.xlabel('# of friends')
# plt.ylabel('daily minutes spent on the site')
# plt.show()