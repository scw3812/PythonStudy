# 다중 상속

class Animal:
    def eat(self):
        print("eat")

class Person:
    def study(self):
        print("study")

class Student(Animal, Person):  # 다중상속 -> 단점은 불명확
    pass


s = Student()
s.eat()
s.study()
