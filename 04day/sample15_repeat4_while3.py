# 실습 반복 문자열 입력 -> 문자열이 Q 또는 q이면 반복 종료

# s = ""
# while s.lower() != "q":
#     s = input("글자를 입력하세요\n")
#     print(s)

while 1:
    s = input("글자를 입력하세요\n")
    print(s)
    if s.lower() == "q":
        break
