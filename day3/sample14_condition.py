# 실행문
#     1. 순차문 : 순차적으로 실행
#     2. 제어문 : 조건문 - if, if~else, 다중 if
#                 반복문 - for, while
#
# 비실행문 : 주석문
print(1)
if False:
    print(2)  # 스페이스 4번, 탭으로도 스페이스 4번이니까 괜찮
print(3)
print("end")

if False:
    print("a")
elif True:
    print("b")
else:
    print("c")
