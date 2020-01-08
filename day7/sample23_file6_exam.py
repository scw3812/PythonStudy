# 주민번호.txt를 읽고 출력은 981010-1******
try:
    f = open("./주민번호.txt", "r")
    nums = f.readlines()
    for num in nums:
        print(num[:8]+"******")
except Exception as e:
    print("에러", e)
finally:
    f.close()
