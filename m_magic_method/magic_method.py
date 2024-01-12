# class Magic:
#     def __init__(self, name):
#         self.name = name
#
#     # 초기화된 필드를 확인하고자 할 때 사용한다 = 객체만 출력해도 되기 때문에, 이후의 작업이 편해진다
#     def __str__(self):
#         return f'name: {self.name}'
#     # def __str__(self):
#     #     return f'{self.__repr__()}, __repr__()이 사용됨'
#
# # Magic() = Magic 클래스의 주소값 = 문자열 값
# # 뒤에 __repr__() - 객체의 주소를 표현하는 메소드가 생략되어 있음
# # 주의 - __repr__() 은 재정의하면 안 되는 메소드
# # 만약 클래스 주소를 출력했을 때 나오는 문자열 값을 재정의하고 싶다면, __str__() 을 사용할 것
# # 특정 클래스에서 __str__() 을 재정의하면, __repr__() 대신 __str__() 이 사용된다
# # 이에 따라, 생략해서 작성하면 __str__() 이 붙는다는 것을 알 수 있다
# magic = Magic('magic')
#
# print(magic)

class Student:
    def __init__(self, number, score):
        self.number = number
        self.score = score

    # __add__ 를 클래스 내에서 재정의
    # other에 Student 클래스를 가지는 다른 객체를 넣어주면 두 학생의 점수 합계를 리턴함
    def __add__(self, other):
        return self.score + other.score

    # 같다(==) 연산자 재정의
    def __eq__(self, other):
        # 만약 self와 other의 주소가 같다면 - 같은 객체임을 의미
        if self.__repr__() == other.__repr__():
            print('들어옴')
            return True

        # isinstance - 앞에 있는 객체가 뒤에 있는 클래스 타입인지 검사
        # 만약 other가 Student 클래스라면(number 값이 있는지 검사)
        if isinstance(other, Student):
            return self.number == other.number

        # 만약 여기에 걸렸다면, self, other는 다른 학생임(주소가 다름)을 의미
        return False


student_1 = Student(1, 30)
# student_2 = Student(1, 50)
student_2 = student_1

# 두 학생의 점수를 더하려면 원래는 이렇게 각각에 .score 를 붙여서 써야했음
# 이는 객체가 많아질수록 쓰기 불편할 수 있다
# student_1.score + student_2.score

# 위에서 재정의한 __add__ 메소드를 사용해서 새롭게 연산
# total = student_1.__add__(student_2)

# 연산자만 써도 재정의 된 메소드가 적용됨
total = student_1 + student_2
print(total)
print(student_1 == student_2)
