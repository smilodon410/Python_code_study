import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'venv/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

# print(names.head(10))

# 년도별 출생자 수 확인
total_birth = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# print(total_birth.tail())
# total_birth.plot(title='total birth by year')    # 그래프 화
# plt.show()


# 년도별 이름이 가지는 비율
def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)

# print(names)

# 비율 확인
prop_sum = names.groupby(['year', 'sex']).prop.sum()
# print(prop_sum)


# 년도별 선호도 상위 1000명 산출

# group = names.groupby(['year', 'sex'])
#
# sort_group = names.sort_values(by=['year', 'prop'], ascending=[True, False])
# top_1000 = sort_group.groupby(['year']).head(1000)
#
# data_list = []
# for i in range(131):
#     i = i * 1000
#     j = i + 1000
#     data = top_1000[i: j]
#     data_list.append(data)
#
#
# def year_cal(y):
#     return y - 1880
#
#
# print(data_list[year_cal(2000)])





