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


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass  # 아무것도 안하고 일단은 넘어간다.


# 서플라이 디폿 : 건물, 1개건물 = 8유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()  # 아무것도 출력안나오고 그냥 넘어감
