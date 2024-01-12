# 인간(부모) - 이름, 나이 / 걷기 메소드 - '두 발로 걷습니다' -> 출력 메소드
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷습니다")

# 원숭이(자식) - 이름, 나이, 동물원 이름 / '두 발로 걷습니다', '네 발로 걷습니다' 출력
class Monkey(Person):
    def __init__(self, name, age, zoo: str):
        super().__init__(name, age)
        self.zoo = zoo

    def walk(self):
        super().walk()
        print('네 발로 걷습니다')

person = Person("김광협", 27)
person.walk()

monkey = Monkey("고릴라", 7, "에버랜드")
monkey.walk()
