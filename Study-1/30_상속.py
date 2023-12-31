# 일반유닛
class Unit:
    def __init__(self, name, hp):  # self는 제외하고 값을 던져줌
        self.name = name
        self.hp = hp


# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # 일반유닛과 연결
        self.damage = damage

    def attack(self, location):
        print(
            "{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(
                self.name, location, self.damage
            )
        )

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")  # 파이어뱃 : 5시 방향으로 적군을 공격합니다. [공격력16]

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)  # 파이어뱃 : 파괴되었습니다.
