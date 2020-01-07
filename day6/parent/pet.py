class Pet:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name+" "+str(self.age)+" "+self.gender

    def cry(self):
        print("cry")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")
