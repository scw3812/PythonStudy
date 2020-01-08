from day7.parent.pet import Pet

class Cat(Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, age, gender)
        self.color = color

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.gender + " " + self.color

    def run(self, sound):
        return sound
