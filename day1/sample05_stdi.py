name = input("이름을 입력하세요\n")
age = input("나이를 입력하세요\n")
# input()으로 입력받은 데이터는 모두 문자
print(name, age+"살")
age = int(age)
print("내년에는", str(age+1) + "살")
