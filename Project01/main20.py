import pandas as pd
import numpy as np

# 상관계수
# df = pd.DataFrame({'t1': [2, 4, 6, 8],
#                    't2': [81, 93, 91, 97]})

# print(df.corr(method='pearson'))    # Pearson
# print('-' * 50)
# print(df['t1'].corr(df['t2']))      # 단일로 계산하기


# 오류 문제 해결 : 방법1
# li = [(2, 81)]
# df = pd.DataFrame(li, columns=['t1', 't2'])
#
# df.loc[1] = [4, 93]
# df.loc[2] = [6, 91]
# df.loc[3] = [8, 97]
#
#
# print(df.corr(method = 'pearson')) # 문제의 코드
# print(df['t1'].corr(df['t2'])) # 요것이 에러


# 오류 문제 해결 방법2
# df = pd.DataFrame( columns=[ 't1', 't2' ] )
#
# df.loc['0'] = [2, 81]
# df.loc['1'] = [4, 93]
# df.loc['2'] = [6, 91]
# df.loc['3'] = [8, 97]
#
# df = df.astype(float)
#
# print(df.corr(method = 'pearson')) # 문제의 코드
# print(df['t1'].corr(df['t2'])) # 요것이 에러


# 실습
# a = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# b = a.unique()
# print(b)
#
# c = a.value_counts(sort=False)
# print(c)

# mask = a.isin(['b', 'c'])
# print(mask)
# print(a[mask])

# df = pd.read_csv('venv/ex1.csv')
# print(df)


