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
