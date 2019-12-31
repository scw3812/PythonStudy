# 1. 위치값 접근
# 2. 키값 접근
# 3. 혼합사용 가능
# 4. 수치 데이터 포맷

mesg = "값:{0}".format(987654321)
# 이걸 실수로 표현할라면 콜론하고 f   값:987654321.000000
mesg = "값:{0:f}".format(987654321)
print(mesg)
print()
mesg = "값:{0:.4f}".format(987.654321)  # 소수점 4자리만 표현   값:987.6543
print(mesg)
print()

mesg = "값:{0:,}".format(987654321)  # 콜론 다음 쉼표 세자리마다 쉼표 찍어줘 값:987,654,321
print(mesg)
print()

# 도움말
help('FORMATTING')
