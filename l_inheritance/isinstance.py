class A:
    pass


class B(A):
    pass

a = A()
b = B()

print(isinstance(a, A))
print(isinstance(b, B))

# 모든 자식은 부모 타입이다
# b가 속한 B 클래스가 A 클래스의 자식이기 때문에
# b 역시 A 클래스에서 파생 - 결과값 True
print(isinstance(b, A))

# 단, 부모는 절대 자식 타입이 될 수 없다 - 결과값 False
print(isinstance(a, B))

# 그리고 같은 클래스를 상속받은 여러 자식 클래스들이 존재할 경우
# 해당 자식 클래스들은 모두 다른 타입이 된다
