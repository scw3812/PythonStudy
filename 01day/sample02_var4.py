n = 10
n2 = 10
n3 = 10
n = n2 = n3 = 10
print(n, n2, n3)
x, y = 10, 20
(x, y) = (20, 30)
[x, y] = [30, 40]
x, y = [30, 60]
print(x, y)

a, b, *c = [10, 20, 30, 40]
print(a, b, c)
# 1대1 대응하지 않을 때 *로 묶어줄 수 있다
*a, b, c = [10, 20, 30, 40]
print(a, b, c)
a, *b, c = [10, 20, 30, 40]
print(a, b, c)