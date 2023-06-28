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

marine3 = Unit("마린")  # hp, damage 추가해야함
marine3 = Unit("마린", 40)  # damage 추가해야함
