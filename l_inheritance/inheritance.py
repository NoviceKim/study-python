class A:
    def __init__(self, name):
        self.name = name
        print("부모 생성자")

    def print_intro(self):
        print("A")

# 클래스 선언 시, 이름 뒤에 '소괄호+클래스명' 을 쓰면
# 소괄호 안에 있는 클래스 안 필드(변수, 메소드)를 해당 클래스에서도 그대로 쓸 수 있다
class B(A):
    # 자식 생성자는 무조건 부모 생성자를 먼저 호출한다
    # 클래스 상속이 일어나는 경우, 실은 아래의 생략된 메서드가 먼저 실행되는 것
    # 여기서 self는 B 클래스를, super()는 A 클래스를 의미한다
    # def __init__(self, name):
    #     super().__init__(name)
    #     print("자식 생성자")

    def add(self, num1, num2):
        return num1 + num2

    # 자식 클래스에서 부모 클래스 안 메소드를 같은 이름으로 다시 선언 - 오버라이딩
    # 이 때, 부모 클래스 쪽의 메소드는 무시된다
    # 하지만, 기존에 부모에 있던 요소를 그대로 가져와서 +a 하고싶다면
    # 아래처럼 'super().메소드명()' 으로 먼저 불러오면 된다
    def print_intro(self):
        # 부모에 있던 메소드를 불러오고
        super().print_intro()
        # 자식 메소드에서 추가 내용 작성
        print("B")

b = B('김광협')
print(b.name)
b.print_intro()
print(b.add(1,2))