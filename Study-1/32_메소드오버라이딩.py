# 일반유닛
class Unit:  # 부모
    def __init__(self, name, hp, speed):  # self는 제외하고 값을 던져줌
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격유닛
class AttackUnit(Unit):  # 자식. 다중상속(부모가 둘 이상)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # 일반유닛과 연결
        self.damage = damage

    def attack(self, location):
        print(
            "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
                self.name, location, self.damage
            )
        )


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
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
