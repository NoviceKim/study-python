class Student:
    status = "쉬는 중"

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    # 모든 학생들의 status를 "공부 중"으로 바꿀 것
    # 하지만, 매개변수 self를 지우면 오류 발생
    # 따라서, 앞에 데코레이터 @staticmethod 를 붙여서 클래스 자체에 적용되는 것임을 표시
    # 이렇게 하면, 정적 변수를 쓸 때처럼 Student 클래스 전체에 일괄 적용되며
    # 메소드에 접근하고 싶다면, 클래스 자체에 접근하면 된다
    @staticmethod
    def print_its_time_to_study():
        print("9시 땡")
        Student.status = "공부 중"

# 일단 학생을 만듭시다
kim = Student(0,0,0)
lee = Student(0,0,0)

# 상태 확인
print(Student.status)

# Student 클래스 자체에 대하여 static method 형태로(@staticmethod) 만든 메소드 실행 
Student.print_its_time_to_study()

# 다시 상태 확인하면 '공부 중' 으로 바뀐 것을 볼 수 있음
print(Student.status)
