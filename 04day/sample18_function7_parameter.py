def xxx(n=10, n2=10):  # 디폴트 파라미터를 함수 선언시 설정할 수 있다
    print(n, n2)


xxx()

def xxx2(n, n2):
    print(n, n2)


xxx2(n2=100, n=10)  # named 파라미터

def xxx3(n, n2, n3="유관순"):
    print(n, n2, n3)


xxx3(n2=100, n=10)

def xxx4(*n):  # *는 튜플로 묶어준다, packing만 한다. unpacking X
    print(n)


xxx4(10)
xxx4(9, 8, 6)
xxx4("홍길동", 20)

def kkk(n, n2, n3):
    print(n, n2, n3)


kkk(*[10, 20, 30])  # *로 unpack

def kkk2(n, n2, *n3):  # 매개변수로 할 때는 패킹을 제일 마지막 변수에만 줄 수 있다. -> 필수 매개변수와 나머지로 나누는 과정
    print(n, n2, n3)


kkk2(*[10, 20, 30, 40, 50])

def dict_function(name, age):
    print(name, age)


dict_function(name="홍길동", age=20)

def dict_function(**nnn):  # ** -> named 파라미터를 딕셔너리로 받기
    print(nnn)


dict_function(name="홍길동", age=20)

# * + ** -> 순서대로
def mix_function(a, b, *c, **d):
    print(a, b, c, d)


mix_function(10, 20, 3, 4, 5, name="홍길동", age=20)  # 인자를 넣을 때도 위치값 먼저 그 다음 키워드값
