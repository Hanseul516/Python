# 파이썬 코딩대회 개최,
# 참석률을 높이기 위해 이벤트 진행하기로
# 추첨을 통해 치킨1명, 커피3명 쿠폰
# 추첨프로그램을 작성하시요.

# 조건1: 1-20명 가정
# 조건2: 무작위, 중복불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# 출력예제
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# -- 축하합니다 --

# 활용예제
from random import *
# first = [1,2,3,4,5]
# print(first)
# shuffle(first)
# print(first)
# print(sample(first, 1))



users=range(1, 21) #1부터 20까지 숫자를 생성
users=list(users) #range 자료형을 list형으로 바꿈

shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:]))
print("-- 축하합니다 --")