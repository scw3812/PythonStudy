# list comprehension -> 리스트를 가공해서 반환
# 1. 문법 : 조건X -> 변수명 = [표현식 for 변수 in 리스트]
m = [9, 8, 7]
m2 = [x * 2 for x in m]
print(m2)
# 2. 문법 : 조건O
#           단일 if -> 변수명 = [표현식 for 변수 in 리스트 if 조건식]
#           if~else -> 변수명 = [표현식(참) if 조건식 else 표현식(거짓) for 변수 in 리스트]
m2 = [x for x in range(1, 11) if x % 2 == 0]
print(m2)
m2 = [(x, " 짝수") if x % 2 == 0 else (x, " 홀수") for x in range(1, 11)]
print(m2)
