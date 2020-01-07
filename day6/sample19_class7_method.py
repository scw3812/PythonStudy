class Student:
    msg = "Hello"
    info = "World"

    @classmethod
    def get_msg(cls):  # 클래스 메서드는 파라미터 변수로 cls
        return Student.msg

    @classmethod  # 클래스 메서드의 용도는 주로 클래스 변수를 사용하는 것
    def get_info(cls):
        return cls.info


print(Student.get_msg())
print(Student.get_info())
