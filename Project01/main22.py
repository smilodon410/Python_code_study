import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 파일 경로 확인 해주기!
# import os
# print(os.getcwd())


# Pivot table
# data = pd.DataFrame(np.arange(6).reshape(2, 3),
#                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
#                     columns=pd.Index(['one', 'two', 'three'],
#                     name='number'))
#
# print(data)
# print('-' * 50)
#
# row_pivot = data.stack()
# print(row_pivot)
# print('-' * 50)
#
# print(row_pivot.unstack())  # 원상복구


# 시각화
# subplot 에 그래프 그리기
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
#
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))


# drawstyle : steps-post
# data = np.random.randn(30).cumsum()
#
# plt.plot(data, 'k--', label='Default')
# plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
# plt.legend(loc='best')

# 3개의 선 범례 그래프
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# ax.plot(np.random.randn(1000).cumsum(), 'k',  label='one', color='r')
# ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two', color='b')
# ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three', color='g')
#
# ax.legend(loc='best')

# 주석 추가하기 (예제 : 금융 위기)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# data = pd.read_csv('venv/spx.csv')

data = pd.read_csv('venv/spx.csv')
print(data)



# plt.show()

