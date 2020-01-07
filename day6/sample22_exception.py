# 예외처리
# 예외? 에러
# 예외 발생하면 프로그램이 비정상 종료 된다. -> 예외 처리를 해줘서 이후의 작업을 정상적으로 작동하게 해야됨
# 예외 처리 : 비정상 종료되는 프로그램을 정상종료하도록 유도하는 것(문제 발생 코드를 수정하는 것이 아님)
# -> try:
#       수행코드
#    except [Exception 클래스 as e]:
#       예외발생시 처리코드
#    except [Exception 클래스 as e]:
#       예외발생시 처리코드              => 반복해서 여러 예외를 처리

print("시작")
num = input("숫자를 입력하세요 :\n")
try:
    result = 10 / float(num)
    print("결과값:", result)
except:
    print("나눌 수 없습니다.")
print("정상종료")
