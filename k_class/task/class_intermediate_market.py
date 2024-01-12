# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

# 상품, 손님의 데이터 -> 마켓
# 마켓 클래스 - 상품과 재고 데이터
# 손님 - 이름, 나이, 할인율과 낸 금액을 매개변수로 받음
# 상품 - 상품명, 가격을 매개변수로 받음

# 상품이 있어야 손님이 구매한다?
# 상품의 데이터(상품명, 가격)을 손님에게 전달 -> 할인율 적용해서 결과 출력
# 그렇다면 상품 메소드 안에 손님 메소드를 클로저로 생성?

# 상품 판매 시: 먼저, 손님이 낸 금액 >= (상품 금액 * 할인율) 인지 if문으로 분기 처리
# 만약 참이라면, 손님이 낸 금액 - (상품 금액 * 할인율) 만큼 잔액
# 거짓이라면, "금액이 부족합니다" 출력

# 상품, 손님 클래스 따로 만들고, 나중에 Market 클래스 안에서 호출해서 쓰기
# 상품 클래스 - 상품명, 가격
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(self.name, self.price)

# 손님 클래스 - 이름, 나이 / 지불 금액, 할인율(기본값 0)
class Customer:
    def __init__(self, name, age, money=0, discount_rate=0):
        self.name = name
        self.age = age
        self.money = money
        self.discount_rate = discount_rate

# 마켓 클래스 - 상품 정보, 각 상품 별 재고수
class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell(self, customer):
        # 할인 후의 금액을 구하기 위해 할인율(discount_rate) 기반으로 연산
        customer.money -= self.product.price * (1 - customer.discount_rate * 0.01)

        # 상품을 팔았으니 재고 -1
        self.stock -= 1

# 상품 객체들 생성
apple = Product('사과', 2500)
orange = Product('오렌지', 4500)
cherry = Product('체리', 3500)
melon = Product('멜론', 12000)
avocado = Product('아보카도', 7000)

customer_1 = Customer("김광협", 27, 20000, 20)
customer_2 = Customer("유재석", 50, 50000, 40)
customer_3 = Customer("KGH", 25, 18000, 15)

# Market 클래스 불러와서 판매 실행
market = Market(apple, 40)
market.sell(customer_1)

# market의 재고수와 손님의 남은 금액 출력
print(market.stock)
print(int(customer_1.money))
