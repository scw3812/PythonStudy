n = 10
n2 = 3

print("더하기", (n+n2))
print("빼기", (n-n2))
print("곱하기", (n*n2))
print("나누기", (n/n2))
print("나누기(몫:정수만)", (n//n2))
print("나머지", (n % n2))
print("지수", 3**2)

result = divmod(10, 3)
# divmod(a, b)를 사용하면 (a//b, a%b)인 튜플로 반환
print(result)
a, b = result
print("몫", a, "나머지", b)
