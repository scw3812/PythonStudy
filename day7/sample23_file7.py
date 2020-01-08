# 파일 처리 : 파일 읽기, 쓰기 -> 파일 없거나 못만들때를 대비해 예외 처리 해줘야됨
# -> open()

# with -> close()를 자동으로 해주는 방법
# 문법 with open(file, mode, encoding,...) as f:
#           문장
try:
    with open("./output.txt", mode="w") as f:
        f.write("Hello")
except Exception as e:
    print(e)

try:
    with open("./pet_handler.py", mode="r", encoding="utf-8") as f:
        while True:
            s = f.readline()
            if not s:
                break
            print(s, end="")
except Exception as e:
    print(e)
