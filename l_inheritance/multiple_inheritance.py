# 파이썬은 다중 상속을 지원
# 하지만 여러 부모를 상속받았을 때, 같은 이름의 필드가 겹치면 자식에서 사용할 때 혼란을 유발함
# 이 때에는 mro()를 사용해서 접근 순서를 확인할 수 있지만,
# 자식에서 재정의한 뒤에 사용하는 것이 오히려 낫다
# 다중 상속은 다양한 모호성을 발생시키기 때문에 되도록 피하는 것이 좋다
class A:
    pass


class B(A):
    def print_info(self):
        print("B")


# B 클래스와 같은 이름의 메소드 선언 시
class C(A):
    def print_info(self):
        print("C")


# B, C를 모두 상속받는 D 클래스는 둘 중 어느 쪽에 있는 것을 받을 지 알 수 없다
class D(B, C):
    pass


# 클래스 접근 순서를 출력(D -> B -> C -> A -> Object)
print(D.mro())

# 위의 이유로, 실행하면 'B'가 출력된다
D().print_info()
