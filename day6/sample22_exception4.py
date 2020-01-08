# 파이썬이 보기에는 예외가 아니지만 우리가 예외로 정의해 예외 처리할 수 있음
# -> if 조건:
#       raise Exception("메시지")  -> Exception 클래스를 생성해서 예외를 발생시키는 개념
#       -> 비정상종료되기 때문에 try ~ except 처리 필수

print("시작")

try:
    num = 10
    # print("결과값 :"+num)  # TypeError
    print(num/0)  # ZeroDivisionError
except TypeError as e:
    print("에러발생1", e)
except ZeroDivisionError as e:
    print("에러발생2", e)
except Exception as e:
    print("에러발생3", e)

print("정상종료")
