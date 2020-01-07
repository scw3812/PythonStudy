# 반복문에서 else문 사용 가능 -> 반복문이 완전히 다 반복된 후에 else 안의 구문이 실행됨, break를 만나면 else문이 실행 안됨
for x in range(1, 10):
    if x == 8:
        break
    print(x)
else:
    print("정상종료")
print("end")

n = 1
while n < 10:
    # if n == 8:
    #     break
    print(n)
    n += 1
else:
    print("정상종료")
print("end")