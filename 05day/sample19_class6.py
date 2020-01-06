class Student:
    def __init__(self, std_name, std_no, std_age):  # 지역(local) 변수 -> 파이썬은 함수 안에서 선언된 것만 -> 함수 호출 시 생성 -> 함수 끝나면 제거
        print("init 호출")
        self.std_name = std_name  # 인스턴스 변수 self.변수 -> 인스턴스 생성 시 생성 -> 인스턴스 제거(인스턴스에 다른 값 할당) 시 제거
        self.std_no = std_no
        self.std_age = std_age

    std_school = "고려대학교"  # 클래스 변수 -> 프로그램 실행 시 한번만 생성 -> 프로그램 종료 시 제거 -> 인스턴스끼리 공유


s = Student("홍길동", "2014123123", 24)  # 변수명 = 클래스명() -> 생성자 함수가 자동으로 호출(__init__)

s2 = Student("이순신", "123123123", 22)

