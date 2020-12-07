# NT = int(input('올해 여름은 몇 일? '))
# # T = int(input('자라는데 몇 일? '))
# # C = int(input('최대 StarFruits 몇 개? '))
# # P = int(input('개당 가격? '))
# #
# # print(N, '', , '', C, '  ',P )
#
# a = N//T * C * P
# print(a, '원')

# Map 함수 : List 나 Tuple 의 형변환
# skill = split 함수로 한 번에 입력값 받기
n, t, c, p = map(int, input().split())

print(n, t, c, p)