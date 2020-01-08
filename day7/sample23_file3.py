# 파일 처리 : 파일 읽기, 쓰기 -> 파일 없거나 못만들때를 대비해 예외 처리 해줘야됨
# -> open()

# 2. 파일 읽기 -> 없으면 예외 발생 -> 예외 처리
# mode="r"

try:
    f = open("./pet_handler.py", "r", encoding="UTF-8")  # .은 현재 디렉토리, ..은 상위 디렉토리, 한글을 읽으려면 encoding="UTF-8"
    msg = f.read()  # read() -> 인자를 안주면 파일 내용 전체를 읽어서 스트링 반환, 인자를 주면 그 수 만큼만 읽음
    print(msg)
except Exception as e:
    print("예외처리", e)
finally:
    f.close()
