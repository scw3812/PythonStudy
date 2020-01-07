# 상속(inheritance)
# 'is a' 관계 -> ex) 고양이 is a 동물, 대학생 is a 학생
# 모든 클래스는 Object 클래스의 상속을 받는다
# 파이썬은 다중 상속 가능

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
    pass

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


cat = Cat("나비", 1, "여")
print(cat.get_name())
print(cat.pet_info())
dog = Dog("백구", 3, "남", "하양")
print(dog.pet_info())
print(dog.get_name())
