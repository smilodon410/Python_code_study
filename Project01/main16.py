import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import random

# ticks : 축에 눈금선 표시
# plt.plot()

# plt.xticks(range(0, 110, 10))
# plt.yticks(range(0, 110, 10))

# plt.xticks([1, 2, 3, 4], ['1day', '2day', '3day', '4day'], rotation='50')
# plt.yticks([1, 2, 3, 4], ['tiger', 'dog', 'lion', 'cat'])


# label 과 legend : 라벨과 범례
# plt.plot([1, 2, 3, 4], label='tiger')
# plt.plot([4, 3, 2, 1], label='lion')
#
# plt.legend(loc=2)

# 배경 색상 바꾸기( R, G, B )
# plt.gca().set_facecolor([0.87, 0.87, 0.87])

# Pop-up 창의 크기 조절하기
# plt.figure(figsize=(10, 8))
# plt.plot([1, 2, 3, 4], label='tiger')
# plt.plot([4, 3, 2, 1], label='lion')
#
# plt.legend(loc=2)
# plt.gca().set_facecolor([0.87, 0.87, 0.87])

# Open CV(영상처리) 공부하기

# 한글 설정하기
font_location = 'C:/Windows/Fonts/malgun.ttf'
font_family = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_family)
#
# plt.plot([1, 2, 3, 4], ['호랑이', '독수리', '코끼리', '강아지'])


# subplot
# plt.subplot(2, 2, 2)
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
#
# plt.subplot(2, 2, 3)    # 3번째 인수 : plot 의 위치
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
#
# plt.subplot(4, 3, 1)    # 1, 2번째 인수 : box 를 몇 개로 분할 할지(가로, 세로)
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])


# twin
# age = [10, 20, 30, 40, 50, 60]
# weight = [20, 40, 55, 50, 70, 63]
# height = [100, 120, 140, 150, 170, 165]
#
# plt.plot(age, weight, 'r', label='age-weight')
# plt.twinx()
# plt.plot(age, height, 'b', label='age-height')
# plt.legend(loc=4)


# 그래프 image 파일로 저장하기
# age = [10, 20, 30, 40, 50, 60]
# weight = [20, 40, 55, 50, 70, 63]
# height = [100, 120, 140, 150, 170, 165]
#
# plt.plot(age, weight, 'r', label='age-weight')
# plt.twinx()
# plt.plot(age, height, 'b', label='age-height')
# plt.legend(loc=4)
# fig = plt.gcf()
#
# plt.show()
# fig.savefig('test.png')


# Bar chart
# a = [1, 2, 3]
# b = [2, 3, 1]
#
# plt.bar(a, b)


# barh : 가로로 보여주기
# a = [1, 2, 3]
# b = [2, 3, 1]
#
# plt.barh(a, b)


# align='center or edge' : 바의 위치 조절
# a = ['Python', 'C++', 'Java', 'Scala', 'Lisf', 'Pearl', 'JavaScript']
# b = [12, 10, 8, 6, 4, 2, 1]
#
# plt.bar(a, b, align='edge')    # default = center


# Ctrl + B : 정의된 함수 확인(default 값을 확인)
# * 뒤는 변수 값을 무조건 써야 한다
# alpha= : 배경과 그래프가 섞이는 정도(블랜딩) = 0: 100% 섞임, 1: 독립
# a = ['Python', 'C++', 'Java', 'Scala', 'Lisf', 'Pearl', 'JavaScript']
# b = [12, 10, 8, 6, 4, 2, 1]
#
# plt.bar(a, b, 0.2, 10, align='edge', alpha=0.5)


# 일반 list 는 연산이 불가 하지만 Numpy list 는 연산이 가능하다
# a = plt.bar(np.arange(4)+0.0, [90, 55, 40, 65], 0.4, color='r', label='Tiger')
# b = plt.bar(np.arange(4)+0.2, [65, 40, 55, 95], 0.4, color='b', label='Lion')    # align='edge'
# plt.legend(loc=9)


# Bar 병합
# a = plt.bar(np.arange(4), [90, 55, 40, 65], 0.4)
# b = plt.bar(np.arange(4), [65, 40, 55, 95], 0.4, bottom=[90, 55, 40, 65])


# 예시 : 연도별 석탄 채굴량
plt.title('연도별 석탄 채굴량')

y = [i for i in range(1980, 2021)]
z = []
for _ in range(1980, 2021):
    c = random.randint(0, 50)
    z.append(c)

a = plt.bar(y, z, 0.5, label='단위(t)')

plt.xlabel('년도')
plt.ylabel('채굴량')
plt.legend(loc=1)

plt.show()

# 유형
# 1. 나이별 급여
# 2. 직업별 월급 차이
# 3. 성별 급여 차이
# 4. 학과별 경쟁률
# 5. 월별 수익률
# 6. 팀별 성적
# 7. 종교 유무에 따른 이혼률
# 8. 동물원별 사자와 호랑이에 대한 개체수
# 9. 나라별 성별에 대한 인구수
# 10. 나라별 성별에 대한 월급차이
# 11. 성별 직업에 대한 빈도수
# 12. 지역별 연령대 비율
# 연령대별 정당에 대한 지지율
# 14. 지역별 정당에 대한 지지율
# 15. 나라별 금은동에 대한
# 16. 도시별 성별에 대한 범죄율
# 기타 등등

# 도표로 주로나오는 수치
# 경제성장률
# 자살률
# 합격률
# 취업률
# 백분율
# 판매량
# 재고량
# 성장률
# 생산량
# 분포량
# 빈도
# 유입량
# 이자율

