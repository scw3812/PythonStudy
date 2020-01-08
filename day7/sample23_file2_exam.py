# 무한반복하면서 사용자의 키보드 입력 받는다
# 입력받은 문자열을 keyboard.txt 파일에 저장

print("프로그램 시작")
try:
    f = open("c:\\keyboard.txt", "a")
    while 1:
        msg = input("문자열을 입력하세요 : ")
        if msg.upper() == "Q":
            break
        f.write(msg+"\n")
except Exception as e:
    print("예외 처리", e)
finally:
    f.close()
print("프로그램 종료")
