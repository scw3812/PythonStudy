print("시작")
num = input("숫자를 입력하세요 :\n")
try:
    result = 10 / float(num)
    print("결과값:", result)
except ValueError as e:
    print("문자로 나눌 수 없습니다.", e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.", e)
except ArithmeticError as e:
    print(e)
except Exception as e:
    print(e)

# 예외 클래스는 계층 구조가 있다. -> 예외 처리 시 예상되는 예외의 범위가 클 수록 뒤에 적어준다.

print("정상종료")
