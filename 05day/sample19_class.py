class Student:
    def xxx(self):  # 메서드(내부 함수)는 매개변수로 self(는 인스턴스) 필수
        print("xxx 호출", self)
        print(self.std_name, self.std_no)

    def __init__(self, std_name, std_no):  # 지역(local) 변수
        print("init 호출")
        self.std_name = std_name  # 인스턴스 변수
        self.std_no = std_no


s = Student("홍길동", "2014123123")  # 변수명 = 클래스명() -> 생성자 함수가 자동으로 호출(__init__)
s.xxx()
print(s)
s2 = Student("이순신", "123123123")
s2.xxx()
