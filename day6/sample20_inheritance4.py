class Pet:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        self.name += "는 "
        return self.name

    def pet_info(self):
        return self.name + " " + str(self.age) + " " + self.gender


class Cat(Pet):  # 자식 클래스명(부모 클래스명) -> 상속
    def get_name(self):
        super().get_name()
        self.name += "고양이"
        return self.name

class Dog(Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, age, gender)  # super()가 부모를 의미
        self.color = color

    def get_name(self):
        super().get_name()
        self.name += "강아지"
        return self.name

    # 오버라이딩 메서드
    def pet_info(self):
        return self.name + " " + str(self.age) + " " + self.gender + " " + self.color


pets = [Cat("나비1", 3, "여"), Cat("나비2", 1, "여"), Cat("나비3", 2, "남"),
        Dog("백구1", 3, "남", "하양"), Dog("백구2", 5, "여", "검정")]


for p in pets:
    print(p.pet_info())

print("="*50)

for c in pets:
    if isinstance(c, Cat):
        print(c.pet_info())
