def my_len(n):
    return len(n)


n1 = my_len("홍길동")
n2 = my_len([10, 20, 30, 40])
n3 = my_len({"username": "홍길동"})

print(n1, n2, n3)

def my_sum(n):
    return sum(n)


print(my_sum([9, 8, 7, 6, 5]))

def my_avg(n):
    return sum(n)/len(n)


print(my_avg([9, 8, 7, 6, 5]))

def negative_zero(n):
    # m = []
    # for a in n:
    #     if a > 0:
    #         m.append(a)
    #     else:
    #         m.append(0)
    # return m
    return [0 if x < 0 else x for x in n]


print(negative_zero([10, -7, 4, -2]))

def top_n_three(n):
    # n.sort(reverse=True)
    m = sorted(n, reverse=True)
    return m[:3]


print(top_n_three([90, 45, 22, 100, 55]))

def top_n(n, a):
    # n.sort(reverse=True)
    m = sorted(n, reverse=True)
    return m[:a]


print(top_n([90, 45, 22, 100, 55], 2))

def top_n_sort(n, a, reverse):
    # n.sort(reverse=True)
    m = sorted(n, reverse=True)[:a]
    if reverse:
        m.reverse()
    return m


print(top_n_sort([90, 45, 22, 100, 55], 2, True))
