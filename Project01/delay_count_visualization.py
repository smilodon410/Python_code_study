# 1. HDFS에 접속 -> 결과 파일 읽기
# 2. 결과 내용을 DataFrame 으로 변환
# 3. Matplotlib 으로 시각화
from hdfs import InsecureClient
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO # 문자열을 파일로 읽어주는

client = InsecureClient('http://192.168.56.100:50070', user='hadoop')
# print(client)

# 데이터 읽어오기
with client.read('output/arr_delay_count/part-r-00000', encoding='utf-8') as reader:
    data = reader.read()

# print(data)
# data ->str -> stream
stream = StringIO(data)
df = pd.read_csv(stream, sep='\t', header=None)
# print(df)

# 가공
# print(df[0].str.split(','))
df['year'] = df[0].str.split(',').str[0]
df['month'] = df[0].str.split(',').str[1]

# year, month 컬럼을 int로 변환
df['year'] = df['year'].astype('int')
df['month'] = df['month'].astype('int')

# print(df)

# 데이터 프레임을 year 기준으로 group
grouped_df = df.groupby('year')

# 시각화
fig, ax = plt.subplots()    # 여러개의 플롯을 겹치기 위한 서브 플롯
for year, df in grouped_df:
    # print(year)
    # print(df)
    sorted_df = df.sort_values(by='month', axis=0)
    ax.plot(sorted_df['month'], sorted_df[1], label=year, marker='*')


plt.legend(loc=2)
plt.show()



