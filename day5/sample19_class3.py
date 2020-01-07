class Student:
    def __init__(self, std_name, std_no, std_age):  # 지역(local) 변수
        print("init 호출")
        self.std_name = std_name  # 인스턴스 변수
        self.std_no = std_no
        self.std_age = std_age

    def print_field(self):  # 메서드(내부 함수)는 매개변수로 self(는 인스턴스) 필수
        print("print_field 호출", self)
        print(self.std_school, self.std_name, self.std_no, self.std_age)
        print("*"*50)

    def set_age(self, age):
        self.std_age = age

    def get_age(self):
        return self.std_age

    std_school = "고려대학교"


s = Student("홍길동", "2014123123", 24)  # 변수명 = 클래스명() -> 생성자 함수가 자동으로 호출(__init__)
s.print_field()
s.set_age(30)
s.print_field()
print(s.get_age())

s2 = Student("이순신", "123123123", 22)
s2.print_field()
s2.std_age = 25  # 객체 지향에서 필드에 직접 접근하는 것은 안좋다
# -> 직접 접근할 경우 메소드를 활용했을 때와는 다르게 원하지 않는 형식의 데이터를 줄 수 있게 되므로
s2.print_field()
