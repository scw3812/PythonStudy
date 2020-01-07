class Student:
    def xxx(self):  # 메서드(내부 함수)는 매개변수로 self(는 인스턴스) 필수
        print("xxx 호출", self)
        print(self.std_name, self.std_no)

    def __init__(self, std_name, std_no):  # 지역(local) 변수
        print("init 호출")
        self.std_name = std_name  # 인스턴스 변수
        self.std_no = std_no


s = Student("홍길동", "2014123123")  # 변수명 = 클래스명() -> 생성자 함수가 자동으로 호출(__init__), 소멸자도 있음
s.xxx()
print(s)
s2 = Student("이순신", "123123123")
s2.xxx()

# 메서드
#   1. 인스턴스 메서드 : 객체 생성 후 사용
#   2. 클래스 메서드 : 객체 없이도 사용 -> 클래스명.메서드()
#      -> @classmethod라고 지정
