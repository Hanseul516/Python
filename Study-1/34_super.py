class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  # 다중상속일때 super를 하면 맨 처음 상속받은 class만 호출됨
        Unit.__init__(self)
        Flyable.__init__(self)  # 이렇게하면 함수 2개 다 출력.


# 드랍쉽
dropship = FlyableUnit()  # super일때 출력: Unit 생성자
