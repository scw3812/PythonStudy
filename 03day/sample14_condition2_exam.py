# 실습
# 1. 키보드로 숫자를 입력받아서 짝수이면 "짝수입니다" 홀수이면 "홀수입니다" 출력
num = int(input("숫자를 입력하세요\n"))
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

# 2. 키보드로 도시 입력 리스트 안에 있는지 출력
location = ["서울", "제주", "광주", "부산"]
city = input("도시를 입력하세요\n")
if city.strip() in location:
    print(city+" 속합니다")
else:
    print(city+" 속하지 않습니다")

# 3. 키보드로 취미값 입력받고 리스트에 속하는지 출력 단, 대소문자 구분 없이
hobby = ["football", "baseball", "basketball", "swimming"]
m = input("취미를 입력하세요\n")
if (m.lower()).strip() in hobby:
    print(m+" 속합니다")
else:
    print(m+" 속하지 않습니다")

# 4. 키보드로 입력한 값이 key에 포함?
fruit = {"봄": "딸기", "여름": "수박", "가을": "사과"}
m = input("계절을 입력하세요\n")
if m.strip() in fruit:
    print(m+" 속합니다")
else:
    print(m+" 속하지 않습니다")

# 5. 영문자 입력 -> 대소문자 바꾸기
word = input("영문자 입력\n")
# if 64 < ord(word) < 91:
#     print(word.lower())
# else:
#     print(word.upper())
# print(word.swapcase())
if word.islower():  # islower() 함수로 문자 전체가 소문자인지 파악
    print(word.upper())
else:
    print(word.lower())

# 6. 주민번호 입력받고 성별 출력
id_num = input("주민번호를 입력하세요\n")
if id_num[7] == "1" or id_num[7] == "3":
    print("남자")
else:
    print("여자")

# 7. 주민번호 입력받고 *로 출력
id_num = input("주민번호를 입력하세요\n")
# print(id_num[:8]+"******")
if len(id_num) > 8:
    print(id_num[:8]+"*"*len(id_num[8:]))

# 8. 전화번호 입력받고 통신사 출력
phone = input("전화번호를 입력하세요\n")
if phone[:3] == "011":
    print("SKT")
elif phone[:3] == "016":
    print("KT")
elif phone[:3] == "019":
    print("LG")
else:
    print("잘못된 전화번호입니다")
