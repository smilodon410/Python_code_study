# import 방법
# 1번
# import matplotlib.pyplot
#
# matplotlib.pyplot.plot()
# matplotlib.pyplot.show()

# 2번
# from matplotlib.pyplot import *
#
# plot()
# show()

# 3번 : 대중적으로 쓰임
import matplotlib.pyplot as plt

plt.plot()


# plot 의 종류
# line plot : 점과 점 사이를 연결
# bar plot / bar chart : 막대그래프 형식
# histogram plot : 연속 분포를 나타낼 때 주로 사용
# scatter plot : 산점도
# contour plot : 등고선(?)
# surface plot : contour plot 의 3차원 곡면 플롯
# box plot : 상자그래프
# pie plot : 원그래프


# title 설정

plt.title('Tiger')


# 값 입력하기
# plt.plot([1, 4, 9, 16])     # 1개만 있을 때는 y축

# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])   # x축, y축


# 배경에 격자 넣기
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])   # x축, y축
# plt.grid(True)  # default 값은 False
# plt.show()


# x 축, y 축에 이름 넣기
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])   # x축, y축
#
# plt.xlabel('tiger')
# plt.ylabel('eagle')


# Hold 기법
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.plot([10, 20, 30, 40], [1, 2, 3, 4])


# range 를 활용한 plot
# x, y 값을 정확하게 일치 시켜야 한다
# plt.plot([10, 20, 30, 40], range(4))
# plt.plot([10, 20, 30, 40], range(2, 6))


# 색상 설정
# plt.plot(range(1, 5), 'r')
# plt.plot(range(2, 6), 'g')
# plt.plot(range(3, 7), 'b')
# plt.plot(range(4, 8), 'c')
# plt.plot(range(5, 9), 'm')
# plt.plot(range(6, 10), 'y')
# plt.plot(range(7, 11), 'k')
# plt.plot(range(8, 12), 'w')

# range + color
# plt.plot(range(0, 10), range(30, 40), 'k')


# marker 종류
#a = '.,ov^<>w1234sp*hH+xDd'
# for k, v in enumerate( a ):
#     plt.plot( range( 1+k, 5+k ), v + '-' )

# marker 설정
# plt.plot(range(1, 5), range(1, 5), 'D-')


# line style
# plt.plot(range(1, 5), '-')     # 직선 : default
# plt.plot(range(2, 6), '--')    # 점선
# plt.plot(range(3, 7), '-.')    # 파선
# plt.plot(range(4, 8), ':')     # 더 세밀한 점선


# 색상, marker, line style 합성 : '' 안에 모두 합쳐서 넣는다
# plt.plot(range(1, 5), 'rD:')
# plt.plot(range(1, 5), range(4, 0, -1), 'gH--')


# 선 세부 설정
# plt.plot(
#     [10, 20, 30, 40],  # x축
#     [1, 4, 9, 16], # y축
#     c="b",    # 선 색깔
#     lw=5,     # 선 굵기
#     ls="--",      # 선 스타일
#     marker="o",       # 마커 종류
#     ms=10,        # 마커 크기
#     mec="g",      # 마커 선 색깔
#     mew=5,        # 마커 선 굵기
#     mfc="r"       # 마커 내부 색깔
# )
#
#
# plt.plot(
#     [1, 4, 9, 16],  # x축
#     [40, 30, 20, 10], # y축
#     c="g",    # 선 색깔
#     lw=3,     # 선 굵기
#     ls=":",      # 선 스타일
#     marker="D",       # 마커 종류
#     ms=5,        # 마커 크기
#     mec="y",      # 마커 선 색깔
#     mew=3,        # 마커 선 굵기
#     mfc="k"       # 마커 내부 색깔
# )


# x 축, y 축의 유효범위 설정
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.xlim(-10, 30)
# plt.ylim(-10, 30)
# plt.grid(True)
#
# plt.show()
