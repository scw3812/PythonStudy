# 표준 출력: 모니터로 출력, print() 함수사용 콘솔에 출력
# 더하기가 산술연살자지만 "문자열"+값==> 연결
# 근데 age를 연결할라니까 안돼 숫자라서
# 더하기로 연결할려면 둘다 문자열이어야 해  다른언어는 문자 숫자여도 연결돼
# 에이지 연결할려면 str()로 감싸줘야해

# 1. 기존 방법
name = "홍길동"
age = 20
name2 = "이순신"
age2 = 44
# output: 이름은: 홍길동, 나이는: 20
print("이름은:"+name+", 나이는: " + str(age))
print("이름은:"+name2+", 나이는: " + str(age2))  # 두개가 되면 이런식으로 해야해  다섯사람이면 이거 다섯번 만들어야해
# 문제는 포맷이 이름: 으로 변경되면 다 바꿔줘야 해

# 2. 새로운 방법: format 함수 이용
# 문법: "이름: {0} , 나이는 {1}".format(값, 값2)         중괄호로 연결
print("이름:{}".format("유관순"))  # 중괄호의 포맷뒤에 있는 값이 맵핑된다.  값하나면 위치값 안줘도 돼
# 얘가 실행되면 이름 유관순이 나와 데이터니까  변수에다 저장할 수 도 있어

mesg = "이름:{0}".format("유관순")
print(mesg)
mesg = "이름:{0}, 나이:{1}" .format("유관순", 20)  # 0번째는 포맷뒤에 있는 첫번째 값 1번째는 포맷뒤의 두번째값으미
print(mesg)
mesg = "이름:{0}, 나이:{1},{1}" .format("유관순", 20)  # 필요하면 중괄호로 계속 맵핑시킬수도 있다.
print(mesg)

# 뒤에 값을 집합형으로 둘수도 있다.
mesg = "이름:{0}, 이름:{0} ,이름:{0}" .format(["유관순", "이순신", "강감찬"])  # 포맷뒤에 데이터 하나니까 무조건 0만 써
print(mesg)  # 이름:['유관순', '이순신', '강감찬'], 이름:['유관순', '이순신', '강감찬'] ,이름:['유관순', '이순신', '강감찬']
# 이렇게 3번씩나와 근데 리스트를 자동으로 풀어헤칠수 있어 아까 별표 변수에 붙였는데
#  데이터에 붙이면 언팩


mesg = "이름:{0}, 이름:{1} ,이름:{2}" .format(*["유관순", "이순신", "강감찬"])  # 데이터에 별표 붙이면 언팩해
print(mesg)   # 결과값  이름:유관순, 이름:이순신 ,이름:강감찬
print()
mesg = "이름:{0}, 이름:{1} ,이름:{2}" .format(*"유관순")  # 문자열에 붙이면 한글자 씩 언팩돼
print(mesg)   # 결과값: 이름:유, 이름:관 ,이름:순
print()
data = {"username": "홍길동", "age": 20}
mesg = "이름:{username}, 나이:{age}".format(**data)  # 딕트는 위치값이 아니라 키로 접근을 하니까 위치가 아니라 키값을 넣어야해
# 근데 이것도 딕트 하나를 분리 했다는거 의미  그래서 별표 줘야하는데 딕트인경우에는 별표 두개
# 리스트 해체 리스트 언패킹은 별표하나지만 딕트는 두개
print(mesg)    # output 이름:홍길동, 나이:20