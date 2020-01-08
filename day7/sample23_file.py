# 파일 처리 : 파일 읽기, 쓰기 -> 파일 없거나 못만들때를 대비해 예외 처리 해줘야됨
# -> open()

# 1. 파일 쓰기 -> 없으면 자동으로 생성
# mode="w" -> 덮어쓰기, mode="a" -> 추가
try:
    f = open("c:\\output.txt", mode="w")
    f.write("Hello")
except Exception as e:
    print("예외처리", e)
finally:
    f.close()
