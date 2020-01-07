for x in [1, 2, 3, 4, 5]:  # 튜플, 셋, 딕트도 들어감
    print(x * 5)
for x in range(5):
    print("hello")
for idx, data in enumerate([1, 2, 3]):  # enumerate(list)를 통해 index와 data를 모두 얻을 수 있다
    print(idx, data)

m = {"username": "홍길동", "age": 20, "address": "서울", "email": "sdfsdf@naver.com", "phone": "010-3829-1241"}
# 문장이 길어서 엔터 치면 문자열 사이에 \가 들어가는데 트리플로 만들면 안들어감
for k in m:
    print(m[k])  # 딕트를 반복하면 키값이 반복
for x, y in m.items():
    print(x, y)

# 실습 1부터 10가지 반복, 짝수 출력
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
