# 일반유닛
class Unit:  # 부모
    def __init__(self, name, hp):  # self는 제외하고 값을 던져줌
        self.name = name
        self.hp = hp


# 공격유닛
class AttackUnit(Unit):  # 자식. 다중상속(부모가 둘 이상)
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


# 드랍쉽 : 공중유닛, 수송기, 마린/파이어뱃/탱크 등을 수송. 공격x


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
        )


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중공격유닛, 한 번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
