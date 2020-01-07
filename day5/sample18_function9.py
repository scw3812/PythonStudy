# 리스트를 조건에 일치하는 값만 추출

m = list(range(1, 11))
print(m)
result = filter(lambda n: n % 2 == 0, m)
print(list(result))

func = lambda n: n % 2 == 0
result = filter(func, m)
print(list(result))

def func(n):
    return n % 2 == 0


def my_filter(f, n):
    return [x for x in n if f(x)]


func = lambda n: n % 2 == 0
result = my_filter(func, m)
print(list(result))

# def my_filter(f, n, mode):
#     return sorted([x for x in n if f(x)], reverse=not mode)
def my_filter(f, n, mode):
    r = [x for x in n if f(x)]
    r.sort(reverse=not mode)
    return r


func = lambda n: n % 2 == 0
result = my_filter(func, m, False)
print(list(result))
