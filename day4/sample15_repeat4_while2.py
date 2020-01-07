# s = ""
# while s != "q":
#     s = input("글자를 입력하세요\n")
#     print(s)
for n in range(1, 11):
    if n == 8:
        break
    print(n)
print("end")

m = 1
while m <= 10:
    if m == 8:
        break
    print(m)
    m += 1
print("end")

while 1:
    s = input("글자를 입력하세요\n")
    print(s)
    if s == "q":
        break
