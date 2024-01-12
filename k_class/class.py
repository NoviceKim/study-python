# 클래스 선언
class A:
    # 진짜 생성자는 이것(__new__)
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    # 보통 이걸(__init__) 생성자라고 많이 알고 있음
    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(self)

        # 생성자 호출 시 이 변수들이 같이 만들어짐
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    # self = 자신의 주소값
    # 생성자가 만들어질 때, __init__의 매개변수 name에 전달된 값을 가져옴
    def print_name(self):
        print(self.name)

# 객체화
# A 뒤에 함수처럼 소괄호가 있지만, 함수가 아닌 생성자
# 클래스 이름은 항상 대문자로 시작 - 이걸 기억하고 있으면 편할 것
a = A(10, 20, name='apple')

# a의 주소값 출력
print(a)

# a.data1 = 10
# a.data2 = 20

# A 클래스에 data1, data2를 만든 적이 없는데 10 20이 출력되는 이유?
# 파이썬의 동적 바인딩 때문 - 없으면 만든다
print(a.data1, a.data2)
a.print_name()

# A 클래스를 가지는 변수 b 생성
# 이 아래부터는 위쪽 변수 a와 주소값 다름
b = A(100, 200, name='banana')

# 따라서 a와는 다른, b 고유의 주소값이 나온다
print(b)

# b.data1 = 100
# b.data2 = 200

print(b.data1, b.data2)
b.print_name()

# 추가
# a와 b 뒤의 print_name()은 서로 다른 함수
# a.print_name('a')
# b.print_name('b')

