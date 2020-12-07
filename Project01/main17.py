# Pandas(판다스) : 데이터 분석을 위한 라이브러리
# 1차원적인 자료 = series 에서 분석
import pandas as pd

# DataFrame : data 를 table 형식으로 만들어줌 = dataframe 생성
# data = {'이름': ['홍희재', '최혁준', '윤지훈'],
#         '나이': [26, 28, 26],
#         '고향': ['인천', '서울', '춘천']}
#
# df = pd.DataFrame(data)
# print(df)


# 기준을 column 으로 dataframe 생성
# a = [10, 20, 30, 40]    # 많은 부분에서 필드(column)의 성격을 지님
# b = [50, 60, 70, 80]
# c = [a, b]
#
# df = pd.DataFrame(c).T
# df.columns = ['나이', '급여']
#
# print(df)


# DataFrame 에 데이터 넣기
# df = pd.DataFrame(columns=['이름','나이','고향'])
# df.loc[20]=['호랑이', '20', '서울']
# df.loc[30]=['호랑이', '25', '대구']
#
# for i in range(10):
#     df.loc[len(df)] = ['이순신' + str(i), 20 + i, '서울' + str(i)]
#
# print(df)


# Data 삭제
# df = pd.DataFrame(columns=['이름','나이','고향'])
# df.loc[20]=['호랑이', '20', '서울']
# df.loc[30]=['호랑이', '25', '대구']
#
# for i in range(10):
#     df.loc[len(df)] = ['이순신' + str(i), 20 + i, '서울' + str(i)]
#
# # a = df.drop([20])   # table 자제를 갱신하는게 아닌 return 값이 있음
# df = df.drop([20])  # table 을 변형하기 위해 같은 변수로 받아준다.
# df = df.drop([2, 3, 4, 5])  # 다중 삭제
#
# print(df)


# Data 검색/확인하기
# df = pd.DataFrame(columns=['이름', '나이', '고향'])
# df.loc[20]=['호랑이', '20', '서울']
# df.loc[30]=['호랑이', '25', '대구']
#
# for i in range(10):
#     df.loc[len(df)] = ['이순신' + str(i), 20 + i, '서울' + str(i)]
#
# print(df.loc[5])
# print('-' * 50)
# print(df[2:4])
# print('-' * 50)
# print(df.head())   # 상위 n 개의 숫자를 보여준다 : default = 5
# print('-' * 50)
# print(df.tail())   # 하위 n 개의 숫자를 보여준다 : default = 5
