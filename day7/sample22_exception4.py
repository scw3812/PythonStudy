# 파이썬이 보기에는 예외가 아니지만 우리가 예외로 정의해 예외 처리할 수 있음
# -> if 조건:
#       raise Exception("메시지")  -> Exception 클래스를 생성해서 예외를 발생시키는 개념
#       -> 비정상종료되기 때문에 try ~ except 처리 필수

from random import randint

def my_random():
    try:
        n = randint(1, 4)
        if n == 2:
            raise Exception("2")  # 아무 예외 클래스로 해도 됨 -> 하지만 적합한 클래스를 쓰는게 맞지 -> 직접 예외 클래스를 만들어서 사용
        print("랜덤값:", n)
    except Exception as e:
        print("예외", e)


my_random()

# try:
#     my_random()
# except Exception as e:
#     print("예외", e)
