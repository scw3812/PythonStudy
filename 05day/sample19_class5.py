class Student:
    def __init__(self, std_name, std_no, std_age):  # 지역(local) 변수
        print("init 호출")
        self.std_name = std_name  # 인스턴스 변수
        self.std_no = std_no
        self.std_age = std_age

    def __str__(self):  # print()에서 인스턴스를 참조할 때 자동으로 호출 되는 메서드
        return self.std_school + " " + self.std_name + " " + self.std_no + " " + str(self.std_age)

    def print_field(self):  # 메서드(내부 함수)는 매개변수로 self(는 인스턴스) 필수
        print("print_field 호출", self)

    def get_field(self):
        return self.std_school, self.std_name, self.std_no, self.std_age

    std_school = "고려대학교"


s = Student("홍길동", "2014123123", 24)  # 변수명 = 클래스명() -> 생성자 함수가 자동으로 호출(__init__)
s.print_field()
print(s)

s2 = Student("이순신", "123123123", 22)
s2.print_field()
