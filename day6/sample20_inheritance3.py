# 부모 요소 상속을 방지 -> private -> 앞에만 __(언더바 2개)

class SuperClass:
    def __init__(self):
        self.__gold = "금"  # private
        self._silver = "은"  # 가능은 하지만 외부에서는 쓰지 않겠다는 의미만 표현
        self.bronze = "동"

    def __xxx(self):  # 메서드를 private하게 하는 이유는 재정의 못하도록 하려고
        print("xxx")


class ChildClass(SuperClass):
    def print_info(self):
        # print(self.__gold)
        print(self._silver)
        print(self.bronze)


c = ChildClass()
c.print_info()
