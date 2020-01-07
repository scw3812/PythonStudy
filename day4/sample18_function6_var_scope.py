# 변수 스코프 : 변수 인식여부 => 함수 블럭에서만 구분
n = 10
if True:
    m = 20
    print(n, m)
print(n, m)  # if 안 변수를 밖에서 쓸 수 있다

for a in range(3):
    m2 = 20
    print(n, m2)
print(n, m2)  # for 안 변수도 밖에서 쓸 수 있다

def xyz():
    m3 = 2000
    print(n, m3)


xyz()
# print(n, m3) 함수 안 변수는 밖에서 못 씀 -> 함수 블럭 스코프
