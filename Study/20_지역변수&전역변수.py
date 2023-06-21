gun = 10  #외부에서 gun변수를 지정

def checkpoint(soldiers):  #경계근무 나가는 군인
    # gun = 20  # 이렇게 두면 가능함
    global gun  # 전역변수 gun을 사용함
    gun = gun - soldiers  
    #이 gun은 밖에 있는 gun=10을 받은게 아니라 checkpoint() 내에서 만들어진 gun. 초기화가 안됐기때문에 쓸 수 없다. -> 지역변수
    print("[함수 내] 남은 총 : {0}".format(gun)) #[함수 내] 남은 총 : 18

def checkpoint_ret(gun, soldiers):
    gun =gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun  #return을 해줌으로써 바뀐 gun의 값을 밖으로 던져줄 수 있음

print("전체 총 : {0}".format(gun)) 
# checkpoint(2)  #2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)  #외부의 gun을 함수로 넘겨서 계산
print("남은 총 : {0}".format(gun))  