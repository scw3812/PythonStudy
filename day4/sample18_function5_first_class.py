# 함수는 1급객체(first-class) -> 함수를 데이터로 처리
#       -> 변수에 저장 가능
#       -> 함수 인자값으로 사용 가능
#       -> 함수 리턴값으로 사용 가능

def xxx():
    print("xxx 호출")


xxx()
yyy = xxx
print(id(xxx), id(yyy))

def yyy(x):
    x()


yyy(xxx)

def zzz():
    return yyy


zzz()(xxx)
