# 람다 함수 ex) list filter 함수의 인자로 람다 함수 씀
# 1. 이름이 없는 익명 함수 표현식
# 2. 람다 함수는 단일 실행문만 허용
def xxx():
    print("xxx 호출")


# -> 람다 함수에서 함수명은 변수명으로 대체, def -> lambda
xxx = lambda: print("xxx 호출")
xxx()

def xxx(a):
    print("xxx 호출", a)


# -> 람다 함수에서 함수명은 변수명으로 대체, def -> lambda,
xxx = lambda a: print("xxx 호출", a)
xxx(1)

def xxx(n, n2):
    print("xxx 호출", n, n2)


# -> 람다 함수에서 함수명은 변수명으로 대체, def -> lambda,
xxx = lambda n, n2: print("xxx 호출", n, n2)
xxx(1, 2)

def xxx(a=1):
    print("xxx 호출", a)


# -> 람다 함수에서 함수명은 변수명으로 대체, def -> lambda,
xxx = lambda a=1: print("xxx 호출", a)
xxx()

def xxx(n, *a, **b):
    print("xxx 호출", n, a, b)


# -> 람다 함수에서 함수명은 변수명으로 대체, def -> lambda,
xxx = lambda n, *a, **b: print("xxx 호출", n, a, b)
xxx(1, 2, 3, name="서창우")

def kkk(n, n2):
    return n+n2


# return 생략하고 값만 씀
kkk = lambda n, n2: n+n2
print(kkk(1, 2))
