# list comprehension -> 리스트를 가공해서 반환, 리스트뿐 아니라 다른 집합형 데이터에서도 되는듯
# 1. 문법 : 조건X -> 변수명 = [표현식 for 변수 in 리스트]
m = {
    "java": 90,
    "sql": 100,
    "python": 90,
    "c++": 70
}
for k, v in m.items():
    print(k, v)

m2 = {k: v for k, v in m.items()}
print(m2)

# 2. 문법 : 조건O
#           단일 if -> 변수명 = [표현식 for 변수 in 리스트 if 조건식]
#           if~else -> 변수명 = [표현식(참) if 조건식 else 표현식(거짓) for 변수 in 리스트]
m3 = {k: v for k, v in m.items() if v >= 90}
print(m3)
m4 = {k: m[k] for k in m if m[k] >= 90}
print(m4)

# 실습 국가:수도 -> 수도:국가로 변경
x = {
    "대한민국": "서울",
    "미국": "워싱턴",
    "일본": "도쿄"
}

x2 = {v: k for k, v in x.items()}
print(x2)
x2 = {x[k]: k for k in x}
print(x2)
