# 일반 가격
def price(people):
    print("{0}명 일반 가격은 {1}원 입니다.".format(people, people * 10000))


# 조조 가격
def price_morning(people):
    print("{0}명 조조 가격은 {1}원 입니다.".format(people, people * 6000))


# 군인 가격
def price_soldier(people):
    print("{0}명 군인 가격은 {1}원 입니다.".format(people, people * 4000))


#다른 문서에서 끌어서 쓰는거
#끌어올 문서이름은 theater_module.py
import theater_module
theater_module.price(3) 
theater_module.price_mornung(4)
theater_module.price_soldier(5)

import theater_module as tm #별명
tm.price(2)

from theater_module import * #전체 데려옴
price(2)

from theater_module import price, price_morning #부분으로 데려옴
price_soldier(2)  #에러

from theater_module import price_soldier as price #부분, 별명
price(4)  #일반가격의 price 아님, soldier임


