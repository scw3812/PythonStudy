m = {10, 20, 30, 10}

print(m)
m.add(40)
m.add((1, 2, 3))
m.update({9, 8, 7})  # update()는 집합형을 풀어서 넣어줌
print(m)
m.remove(10)
m.discard(200)  # discard()는 값이 없어도 에러가 안남
print(m)
