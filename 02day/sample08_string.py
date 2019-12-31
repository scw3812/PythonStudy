# 한 번 만들어진 문자열은 변경 불가
# raw string을 이용해 escape 문자 무시 가능
# ''' ''', """ """(트리플)은 docstring 만들 때, 여러 줄 주석에 사용

# 문자열 관련 함수
# 함수는 xx.str() 이런 식으로 써야되는데 str() 등은 앞의 builtins가 생략된 것
import builtins

print(builtins)
print(dir(builtins))  # dir(클래스) -> 클래스 구성 반환
print(builtins.str(10))
print(str(10))

m = "helloWorld"

print(len(m))  # 문자열 길이
print(dir(m))
help(m.count)  # help에서 []는 생략 가능하다는 것
print(m.count("o", 0, 5))  # 특정 문자 수 구하기 0~4
print(m.find("o"))  # 특정 문자 첫번째 위치, -1이면 없는거
print(m.upper())  # 전체 대문자로
print(m.lower())  # 소준자로
print(m.capitalize())  # 첫 글자만 대문자로
print(m.swapcase())  # 대소문자 바꾸기
print(m.startswith("h"))  # 특정 문자로 시작하는지
print(m.endswith("d"))  # 특정 문자로 끝나는지
n = "  Hello World"
print(n.strip())  # 좌우 공백 제거, lstrip은 왼쪽, rstrip은 오른쪽 공백 제거
print("Hello".lstrip("H"))  # strip으로는 공백뿐 아니라 문자도 지울 수 있음
print("ABAABA".rstrip("A"))
print(n.replace("H", "Y"))
mmm = "a/b/c"
print(mmm.split("/"))  # 문자열을 인자로 구분해서 list로 바꿔줌
print(mmm.partition("/"))  # 문자열을 (첫 번째, 구분자, 나머지)의 튜플로 바꿔줌
ppp = ["a", "b", "c"]
print(" and ".join(ppp))  # list를 문자열로 연결시킨 문자열 반환
