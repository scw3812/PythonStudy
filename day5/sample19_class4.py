class Pet:
    def __init__(self, name, age, sex, cry_sound, eat_sound):
        self.name = name
        self.age = age
        self.sex = sex
        self.cry_sound = cry_sound
        self.eat_sound = eat_sound
        print("이름:", self.name, "나이:", self.age, "성별:", self.sex)

    def cry(self):
        print(self.name+" 운다:", self.cry_sound)

    def eat(self):
        print(self.name+" 먹는다:", self.eat_sound)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex


cat = Pet("나비", 3, "여", "야옹야옹", "쩝쩝")
cat.cry()
cat.eat()

print("="*50)

dog = Pet("백구", 4, "남", "멍멍멍", "냠냠")
dog.cry()
dog.eat()
