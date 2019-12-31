m = [10, 20, 30]
n = m.copy()
print(len(m))
print(m.count(10))
print(m.index(10))
print(10 in m)
m.reverse()  # list 순서를 반대로 변경(void 메서드)
print(m)
print(list(reversed(m)))  # builtins 함수 reversed(list)로 순서를 뒤집은 object를 반환 -> list(object) 하면 list로 바뀜
m.append(40)
print(m)
m.extend([50, 60, 70])  # extend로 리스트를 합칠 수 있다
print(m)
m.insert(0, 0)  # insert(a, b) a 인덱스에 b를 삽입
print(m)
m.pop(3)  # pop(index)로 값 삭제, index를 넣지 않으면 -1이랑 똑같다. -> 마지막 요소 삭제, 순서로 삭제
print(m)
m.remove(20)  # remove(val)로도 삭제, 값으로 삭제
print(m)
m.clear()  # 전부 삭제
print(m)
print(n)
n[0] = 100
print(n)
xyz = [10, 20, 30, [9, 8, 7]]
xyz[3][0] = 90
print(xyz)
# 파이썬은 빅데이터를 다루는 데 최적화 -> 데이터를 일일히 복사하는 것은 비효율적 그래서 모든 변수가 참조형(주소를 저장)
xxx = [1, 8, 5, 4, 30, 2]
xxx.sort()  # 오름차순으로 정렬
print(xxx)
xxx.sort(reverse=True)  # 내림차순으로 정렬
print(xxx)
yyy = ["90", "800", "3", "6", "1"]
yyy.sort(key=int)  # key=int를 인자로 넣어서 문자도 숫자 크기순으로 정렬 가능, 기본적으로는 사전순 정렬
print(yyy)
yyy.sort(key=len)
print(yyy)
mm = [10, 20, 30]
mmm = sorted(mm)  # builtins 함수 sorted(list)로 정렬된 list를 반환
print(mmm)
print("="*50)
print(mmm*2)  # list도 곱하기 해주면 그 수만큼 반복한 새 list를 만들어줌
