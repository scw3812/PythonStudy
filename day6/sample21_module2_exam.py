# 모듈 실습
from day6.child.pets import Cat, Dog

class PetHandler:
    pets = [Dog("백구1", 2, "남"), Dog("백구2", 3, "여"),
            Cat("야옹이1", 4, "남", "검은색"), Cat("야옹이2", 2, "남", "하얀색"), Cat("야옹이3", 1, "여", "갈색")]

    def print_pets(self):
        print("모든 애완동물 출력")
        print(*self.pets, sep=" / ")
        print("="*50)

        print("강아지만 출력")
        print(*[x for x in self.pets if isinstance(x, Dog)], sep=" / ")
        print("=" * 50)

        print("고양이 나이 합계 출력")
        print(sum([x.age for x in self.pets if isinstance(x, Cat)]))


h = PetHandler()
h.print_pets()
