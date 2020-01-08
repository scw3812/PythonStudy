# 파일 처리 : 파일 읽기, 쓰기 -> 파일 없거나 못만들때를 대비해 예외 처리 해줘야됨
# -> open()

# 2. 파일 읽기 -> 없으면 예외 발생 -> 예외 처리
# mode="r"

try:
    f = open("./pet_handler.py", "r", encoding="UTF-8")  # .은 현재 디렉토리, ..은 상위 디렉토리, 한글을 읽으려면 encoding="UTF-8"
    msg = f.readlines()  # readlines() -> 전체를 줄단위로 읽어서 리스트로 반환
    for s in msg:
        print(s, end="")  # 기본적으로 파일에 \n이 있고, print()도 \n을 자동으로 출력하므로 \n이 두번 들어가게 됨 -> end=""
except Exception as e:
    print("예외처리", e)
finally:
    f.close()
