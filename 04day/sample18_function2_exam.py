# 실습
# 1. 두 개의 값을 전달해서 최대값 출력하는 함수
def get_max(a, b):
    # print(max(a, b))
    if a > b:
        print(a)
    else:
        print(b)


get_max(2, 4)

# 2. 주민번호 star print
def star_print(n):

    print(n[:8]+"******")


star_print("951017-1933915")

# 3. 주민번호로 성별 출력
def gender_check(id_num):

    if id_num[7] == "1":
        print("남자")
    else:
        print("여자")


gender_check("951017-1933915")
