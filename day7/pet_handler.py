from day7.child.cat import Cat
from day7.child.dog import Dog

# 관례적으로 여러 모듈 중에서 먼저 실행해야되는 모듈을 표시
# if __name__ == '__main__':

print(__name__)

if __name__ == "__main__":
    pets = [
        Cat("야옹이1", 2, "수컷", "블랙"),
        Cat("야옹이2", 5, "암컷", "화이트"),
        Cat("야옹이3", 1, "수컷", "브라운"),
        Dog("멍멍이1", 2, "암컷"),
        Dog("멍멍이2", 4, "수컷")
    ]

    print("1. 모든 애완동물 출력")
    for pet in pets:
        print(pet)

    print("2. 강아지만 출력")
    for pet in pets:
        if isinstance(pet, Dog):
            print(pet)

    print("3. 고양이 나이 합계 출력")
    age_sum = 0
    for pet in pets:
        if isinstance(pet, Cat):
            age_sum += pet.age
    print(age_sum)
