# 1. 2000보다 크고 3200보다 작은 7의 배수이고 5의 배수가 아닌 정수값을 ,를 구분자로 한줄로 출력
# s = ""
# for n in range(2001, 3200):
#     if n % 7 == 0 and n % 5 != 0:
#         s += str(n) + ", "
# print(s[:-2])

s = []
for n in range(2001, 3200):
    if n % 7 == 0 and n % 5 != 0:
        s.append(str(n))
print(", ".join(s))

# 2. 문자와 수치 입력 받아 각각의 개수 출력
s = input("문자와 숫자를 입력하세요\n")
letters = 0
digits = 0
for n in s:
    if n.isalpha():  # 문자열.is~()함수를 활용해 문자가 무슨 문자인지 알 수 있다
        letters += 1
    elif n.isdigit():
        digits += 1
print("LETTERS", letters)
print("DIGITS", digits)

# 3. list comprehension을 사용해 리스트의 0,2,4,6번째 값 제거 후 출력
m = [12, 24, 35, 70, 88, 120, 155]
# m2 = [m[i] for i in range(len(m)) if i % 2 != 0]
# print(m2)
m2 = [x for i, x in enumerate(m) if i % 2 != 0]
print(m2)
