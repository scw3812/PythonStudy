# 1. sum()
m = [1, 2, 3]
print("합계", sum(m))

# 2. 최대, 최소
m = [9, 29, 92, 4, 2, 1, 0, 142, 213]
print("최댓값", max(m))
print("최솟값", min(m))
m2 = {100: "백", 10: "십", 1000: "천"}
print("딕트 최댓값", max(m2))
print("딕트 최솟값", min(m2))

# 3. 데이터 변환
print("10진수 -> 2진수", bin(8))
print("정수로 변환", int(4.3))
print("정수로 변환", int("100"))
print("실수로 변환", float(4))
print("문자열로 변환", str(4.3)+"이다")

# 4. 수치 관련
print("반올림", round(1.2), round(1.6))
import math
print("근사치중에서 큰 정수", math.ceil(1.2), math.ceil(1.6))
print("근사치중에서 작은 정수", math.floor(1.2), math.floor(1.6))

# 5. all() : 모든 데이터가 True -> True 반환, any() : 하나라도 True -> True 반환
m = [True, True, True, False]
m = ["", "sdf", 100]
print("m의 데이터가 모두 참?", all(m))
print("m의 데이터가 하나라도 참?", any(m))

m = [1, 2, 3, 4, 5, 6]
print("m의 데이터가 모두 짝수냐?", all([x % 2 == 0 for x in m]))
print("m의 데이터가 하나라도 짝수냐?", any([x % 2 == 0 for x in m]))
print("m의 데이터가 모두 10보다 작냐?", all([x < 10 for x in m]))

# 6. zip(a, b) -> a, b를 하나의 쌍으로 묶어줌 -> dict
a = ["이름", "나이"]
b = ("홍길동", 22)
result = zip(a, b)
print(dict(result))
x, y = zip(a, b)
print(x, y)

country = ["대한민국", "중국", "미국"]
capital = ["서울", "베이징", "워싱턴"]
for a in zip(country, capital):
    print("국가명:", a[0], "수도:", a[1])
