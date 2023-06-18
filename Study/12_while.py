customer = "카리나"
index = 5
while index >= 1 :
    print("{0}님, 커피가 준비되었습니다. 순서가 {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "윈터"   --> 무한 루프
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

customer = "닝닝"
person = "unknown"
while person != customer: # person = customer이면 멈춤
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("고객님의 성함을 입력하세요.")