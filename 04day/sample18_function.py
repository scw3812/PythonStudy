# 함수 -> 기능처리 담당, 동적, 재사용
# 함수 종류
#   1. 시스템 함수(built-in 함수)
#        -> buitins 모듈 함수 : int(), str(), zip(), len(), max()...
#        -> 문자열 함수 : s.count(), s.strip(), s.lower()...
#        -> 리스트 함수 : x.count(), x.append(), x.extend(), x.remove()...
#        -> 딕셔너리 함수 : x.keys(), x.items(), x.update()...
#   2. 사용자가 만든 함수 -> def 함수명([parameter]): 문장 [return [값]]
# 함수 호출 -> 제어권이 함수로 넘어감 -> 함수가 끝나고 return(다시 제어가 돌아감)
def hello():
    print("hello1")


def hello2(a, b):
    print("hello2\n"*a, end="")


def hello3():
    return "hello3"


def hello4(a):
    return "hello4\n"*a


hello()
hello2(b=1, a=1)  # 함수 호출시 파라미터변수=인자값 형식으로 사용 가능, 순서 상관 없이
print(hello3())
print(hello4(1), end="")
