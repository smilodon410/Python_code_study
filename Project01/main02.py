# # %를 이용한 치환
# print('호%s랑%s이' % (10,'코끼리'))
# print('호%d랑이' % 10)  # 짝이 하나뿐이면 ()생략 가능
#
# # Format을 활용한 치환
# print('무궁화 {0} 꽃이 {1} 피었습니다'.format(10, '호랑이'))
#
# # 변수에 직접 format을 할 경우 변수 재설정을 해줘야 결과값으로 나오게 된다.
# s = '무궁화 {0} 꽃이 {1} 피었습니다'
# print(s)
# s.format('삼천리', '화려하게')
# print(s)
# t = s.format('삼천리', '화려하게')
# print(t)
# s = s.format('삼천리', '화려하게')
# print(s)
#
# # len함수 : 문자열의 길이를 알고 싶을 때
# s = '무궁화꽃이피었습니다'
# print(len(s))
#
# # .count(찾고자 하는 것) : 찾고자 하는 것의 개수
# s = '무궁화꽃이무궁화피었무궁화습니다무궁화'
# print(s.count('무궁화'))
# print('무궁화꽃이무궁화피었무궁화습니다무궁화'.count('무궁화'))
#
# # find : 해당 글자의 첫글자의 인덱스 번호를 알려준다.
#     # 결과값을 찾지 못했을 때 -1 값을 리턴합니다.
# s = '무궁화 꽃이 꽃이 피었습니다'
# print(s.find('꽃이'))
#
# s = 'Apple'
# t = s + ' Orange'
# s = s + ' Banana'
# print(t, s)
# print(s.lower())  # lower : 대상 문자를 전부 소문자로 바꿔준다
# print(s)                    # 원본 데이터의 변환이 아닌 한시적인 return 값을 가진다.
#                             # 대부분의 경우 원본데이터를 변경하지 않는다.
# print(s.upper())  # upper : 대상 문자를 전부 대문자로 바꿔준다
#
# # replace(old, new) : 대치된 데이터를 변경해준다.
# print(s.replace('Banana','Orange'))
# print(s)  # 원본 데이터는 그대로 살아있다.
#
# # split : space(default값)를 기준으로 나눠서 list에 담아서 결과값을 도출해준다.
# s = '무궁화 꽃이 피었습니다.'
# print(s.split())  # => ['무궁화', '꽃이', '피었습니다']
# t = s.split()
# print(t)
# print(len(t)) # list 값의 개수
# print(t[0],t[1] * 3,t[2])
#
# s = '무궁:화:꽃이:피었:습니다'
# print(s.split(':'))  # split에 기준을 부여함 : , 를 기준으로 삼고 나눈다
#
# # 산술 연산
#
# print( 16 + 3 )
# print( 16 - 3 )
# print( 16 * 3 )
# print( 16 / 3 )
# print( 16 // 3 )
# print( 16 % 3 )
# print( 16 ** 3 )
#
# # 관계(대소) 연산
# print( 3 > 2 )
# print( 3 < 2 )
# print( 3 >= 2 )
# print( 3 <= 2 )
# print( 3 == 2 )
# print( 3 != 2 )
#
# # 논리 연산
# print( False & False )
# print( False & True )
# print( True & False )
# print( True & True )
# print( False or False )
# print( False or True )
# print( True or False )
# print( True or True )
#
# # 부정 연산
# print( not(3 > 2) )
#
# # 연산의 우선 순위( 산술 > 관계 > 논리 )
# print( 3 + 2 > 4 & 6 < 2 * 4 )
# print( 5 > 4 & 6 < 8 )
# print( True & True )
#
# print( ( (3 + 2) > 4 ) & ( 6 < (2 * 4) ) )
#
# # random : 0.0 부터 1.0까지의 값을 랜덤으로 뽑아준다.
# import random
# print(random.random())
# # randint(a,b) : a와 b 사이의 숫자를 랜덤으로 뽑아준다.
# print(random.randint(3, 5)) # 3 <= randint <= 5
# # randrange(시작, 최대값, 간격)
# print(random.randrange(2, 20, 3))
# # 결과 : [2, 5, 8, 11, 14, 17, 20] 중에서 랜덤으로 하나를 뽑아준다.

# Input함수
# a = int(input('입력하세요: '))
# print(a * a)

# 4대 문장( if, for, for, switch )
# 괄호는 안하는게 정석
# 제어문 뒤에는 : 을 삽입
# 조건이 실행 될 때의 문장은 반드시 tab처리

# # if 문장
# if 3 >2 :
#     print(1)

# tab에 항상 주의하며 적는다!
# x = int(input('숫자를 입력하세요: '))
# if x > 0 :
#     print('양수입니다')
# else :
#     print('음수입니다')
#     print(3)  # else에 해당하는 문장
# print(3)  # if, else와 전혀 다른 문장

# 나의 학점은?
# x = int(input('점수를 입력하세요: '))
#
# if x > 90 :
#     print('학점은 A입니다.')
# elif x > 80 :
#     print('학점은 B입니다.')
# elif x > 70 :
#     print('학점은 C입니다.')
# elif x > 60 :
#     print('학점은 D입니다.')
# else :
#     print('학점은 F입니다.')

# 오늘의 점심은?
# x = int(input('오늘의 메뉴는? : '))
#
# a = x // 10;
# b = x % 10;
#
# if a % 2 == 0 :
#     if b % 2 == 0 :
#         print('우동')
#     else :
#         print('짜장')
# else :
#     if b % 2 == 0 :
#         print('냉면')
#     else :
#         print('탕수육')

# False 취급 하는 것 : False, {}, [], (), None
# if('') :
#     print('호랑이')
# else :
#     print('코끼리')

# in : []안에 숫자가 있을까 없을까~
# if 19 in [10,20,30,40] :
#     print('Success')
# else :
#     print('Fail')
#
#
# s = '무궁화 꽃이 피었습니다.'
# t = s.split()
# print(t)
#
# if '무궁화' in t :
#     print('성공!')
# else :
#     print('실패ㅠ^ㅠ')

# while문
# a = 10
# while a > 0 :
#     a -= 1;
#     print(a)
# print('BAAAAM!')

# a = 0
# while a < 10 :
#     a += 1
#     if a == 3 :
#         continue
#     if a == 6 :
#         break
#     print(a)
# print('탈출!!')


# # 우박수
# a = 0
# x = int(input('숫자를 입력하세요: '))
#
# while True :
#     if x % 2 == 0 :
#         a = int(x / 2)
#         print(a)
#         x = a
#     else :
#         a = x * 3 + 1
#         print(a)
#         x = a
#     if x == 1 :
#         break;
# print("탈출!")



