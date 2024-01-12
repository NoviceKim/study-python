# 클래스 메소드, 정적 메소드의 공통점
# 클래스로 선언한 객체가 아닌, 클래스 자체에 직접 접근해서 쓴다

# 둘의 차이점
# 정적 메소드는 해당 클래스를 가진 모든 객체에 대하여 실행할 문장을 작성하는 데 초점을 두고 있지만,
# 클래스 메소드는 위의 목적에 더해, 생성자를 랩핑(wrapping)하는 목적도 있다
# 이 때, cls는 클래스 자체를 받는 매개변수다(객체나 생성자 아님)

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    # Car 클래스에 직접 접근
    # 만약 color가 '빨간색' 이라면, 'red' 로 변경
    # Car 클래스로 객체를 만들기 전에, 클래스 안 메소드에서 객체화 작업을 대신 해서 제출한다
    @classmethod
    def translate_to_eng(cls, brand, color, price):
        if color == "빨간색":
            color = 'red'

        return cls(brand, color, price)

# 클래스 메소드로 선언된 메소드로 접근하면, 해당 메소드가 발동한다
car = Car.translate_to_eng('Bentz', "빨간색", 150000)
car2 = Car.translate_to_eng('Mercedes', "파란색", 200000)

print(car.color)
print(car2.color)