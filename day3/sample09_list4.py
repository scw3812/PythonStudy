m = [10, 20, 30, 40, 50]

# 리스트 복사 1. 얕은 복사(shallow copy) -> 같은 주소
m2 = m
m[0] = 100
print(m2)
# 2. 깊은 복사(deep copy) -> 다른 주소, 데이터 복사 형태(copy() 함수 처럼)
# 1) copy()
m2 = m.copy()
m[0] = 10
print(m2[0])
# 2) 슬라이싱 활용
m3 = m2[:]
m2[0] = 10
print(m3)
# 3) list() 함수 -> 다른 집합형을 list로 바꿔줄 때 사용
m4 = list(m3)
m3[0] = 10
print(m4)

# 중첩된 형태 : copy()하면 바깥 리스트는 deep copy 안쪽 리스트는 shallow copy
xyz = [[10, 20, 30]]
xyz2 = xyz.copy()
print(id(xyz), id(xyz2))
print(id(xyz[0]), id(xyz2[0]))
xyz[0].append(30)
print(xyz2)

import copy
kkk = [[10, 20, 30], [9, 8, 7]]
kkk2 = copy.deepcopy(kkk)  # 안의 요소까지 deep copy
print(id(kkk[0]), id(kkk2[0]))

# filter() 함수 -> 집합형 데이터에서 조건에 맞는 데이터 얻기
m = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# filter(함수, 집합형) 집합형안의 요소에서 함수가 참인 것만 뽑아냄 -> filter object 반환 -> list 등으로 변환 필요
help(filter)
m2 = list(filter(lambda n: n % 20 == 0, m))  # lambda 변수: 조건 -> 이 조건에 맞는 변수를 뽑아줌
print(m2)

xxx = ["홍길동", "정조", "영조", "박혁거세"]
xxx2 = list(filter(lambda n: len(n) == 2, xxx))
print(xxx2)
