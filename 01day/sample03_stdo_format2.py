# 1. 위치값 접근
# 2. 키값 접근

mesg = "이름:{0}, 나이:{1}" .format("유관순", 20)  # 아까는 이렇게 값만 넣었는데 이제 딴거 넣고 딕트처럼 키값으로 접근
print(mesg)

mesg = "이름:{username}, 나이:{age}" .format(username="유관순", age=20)  # 아까는 이렇게 값만 넣었는데 이제 딴거 넣고 딕트처럼 키값으로 접근
print(mesg)

mesg = "이름:{0}, 나이:{age}" .format("유관순", age=20)  # 혼합도 가능 키없는 거는 위치값으로 해야해
print(mesg)
