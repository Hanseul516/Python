class Unit:
    def __init__(self, name, hp, damage):  # self는 제외하고 값을 던져줌
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스: 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #.~~로 멤버변수에 접근

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  #wraith2에만 할당함 (clocking은 wraith2에만 있음) -> 클래스 외부에서 변수를 확장할 수 있음/확장한 변수는 해당되는 것에만 적용가능함

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
