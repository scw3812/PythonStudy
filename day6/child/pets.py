import day6.parent.pet as pet

class Cat(pet.Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, age, gender)
        self.color = color

    def __str__(self):
        return self.name+" "+str(self.age)+" "+self.gender+" "+self.color

    def run(self):
        print("run")

class Dog(pet.Pet):
    def swim(self):
        print("swim")
