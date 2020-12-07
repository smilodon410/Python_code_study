import pandas as pd
import sys
import csv
import json
import numpy as np
import re

# df = pd.DataFrame({'something': ['one', 'two', 'three'],
#                    'a': [1, 5, 9],
#                    'b': [2, 6, 10],
#                    'c': [3.0, None, 11.0],
#                    'd': [4, 8, 12],
#                    'message': [None, 'world', 'foo']})
#
# # df.to_csv('venv/out_df.csv')
#
# fn = '호%s랑%s이' % (' to the ', ' to the ')
# print(fn)
# print('-' * 50)
#
# # for i in range(10):
# #     df.to_csv('venv/out%04d.csv' % (i))
#
#
# df.to_csv(sys.stdout, sep='|')
#
# print('-' * 50)
#
# df.to_csv(sys.stdout, na_rep='없지롱~')
#
# print('-' * 50)
#
# print(df.notnull())    # 결측치 확인
# print('-' * 50)
# print(df.fillna(0))    # 결측치 대체


# 데이터를 딕셔너리로 만들기
# f = open('venv/out.csv')
# reader = csv.reader(f)
#
# # for i in reader:
# #     print(i)
#
# with open('venv/out.csv') as f:
#     line = list(csv.reader(f))
#
# header, values = line[0], line[1:]
#
# data_dict = {h: v for h,v in zip(header, zip(*values))}
#
# print(data_dict)


# Json
# obj = """
# {"name": "Wes",
#  "places_lived": ["United States", "Spain", "Germany"],
#  "pet": null,
#  "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
#               {"name": "Katie", "age": 38,
#                "pets": ["Sixes", "Stache", "Cisco"]}]
# }
# """
#
# result = json.loads(obj)    # Json -> Python
# print(type(result))
#
# asjson = json.dumps(result) # Python -> Json
# print(type(asjson))
# print('-' * 50)
#
# siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
# print(siblings)
# print('-' * 50)
#
# # Pandas 로 json 읽기
# data = pd.read_json('venv/sample.json')
# print(data)


# xlsx = pd.read_excel('venv/ex1.xlsx', 'Sheet1')
# print(xlsx)


# 데이터 끌어오기
# import requests
#
# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
# resp = requests.get(url)
#
# data = resp.json()
#
# issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
# print(issues)


# 데이터 관리
# 결측치 확인 => isnull, notna, notnull
# 결측치 제거 => dropna
# 결측치 변환 => fillna


# 데이터 변형
## 중복 제거하기

# data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
#                      'k2': [1, 1, 2, 3, 3, 4, 4]})
#
# print(data.duplicated())    # duplicated() = 중복확인을 boolean 값으로 반환
# print('-' * 50)
#
# data_drop = data.drop_duplicates()  # drop_duplicated() = 중복값 제거
# print(data_drop)
# print('-' * 50)
#
# data['v1'] = range(7)
# print(data.drop_duplicates(['k1'])) # k1 컬럼을 기준으로 제거
# print('-' * 50)
#
# print(data.drop_duplicates(['k1', 'k2'], keep='last'))


## mapping 활용해서 데이터 변형하기

# data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
#                               'Pastrami', 'corned beef', 'Bacon',
#                               'pastrami', 'honey ham', 'nova lox'],
#                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
#
# meat_to_animal = {
#     'bacon': 'pig',
#     'pulled pork': 'pig',
#     'pastrami': 'cow',
#     'corned beef': 'cow',
#     'honey ham': 'pig',
#     'nova lox': 'salmon'
# }
#
# lower_data = data['food'].str.lower()
#
# data['animal'] = lower_data.map(meat_to_animal)
#
# print(data)


## 개별화 양자화

# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
#
# cats = pd.cut(ages, bins)
#
# cat_in_where = cats.codes
#
# categories = cats.categories
#
# count = pd.value_counts(cats)
#
# group_name = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# cut_by_name = pd.cut(ages, bins, labels=group_name)
#
# print(pd.value_counts(cut_by_name))


## 표시자 더미 변수 계산하기
#
# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
#                    'data1': range(6)})

# print(pd.get_dummies(df['key']))

# dummies = pd.get_dummies(df['key'], prefix='key')   # 컬럼에 key 접두어 추가
# df_with_dummy = df[['data1']].join(dummies)
# print(df_with_dummy)

## 한 로우가 여러 카테고리에 속하는 경우(예시 : 영화 장르)

# mnames = ['movie_id', 'title', 'genres']
#
# movies = pd.read_table('venv/movies.dat', sep='::',
#                        header=None, names=mnames)
#
#
# all_genres = []
# for x in movies.genres:     # 데이터 장르 중복제거
#     all_genres.extend(x.split('|'))
#
# genres = pd.unique(all_genres)
#
# zero_matrix = np.zeros((len(movies), len(genres)))
#
# dummies = pd.DataFrame(zero_matrix, columns=genres)
#
# gen = movies.genres[0]
# gen_shaped = gen.split('|')
#
# for i, gen in enumerate(movies.genres):
#     indices = dummies.columns.get_indexer(gen_shaped)
#     dummies.iloc[i, indices] = 1
#
# movies_windic = movies.join(dummies.add_prefix('Genre_'))
#
# print(movies_windic.iloc[0])


data = pd.Series({'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
                  'Rob': 'rob@gmail.com', 'Wes': np.nan})


pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

matches = data.str.match(pattern, flags=re.IGNORECASE)

print(matches)


