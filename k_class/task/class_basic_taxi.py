# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 실습 1.
# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 실습 2.
# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# 실습 1.
# class Taxi:
#     default_fare = 5800
#     default_distance = 2
#     fare_per_km = 1000
#
#     def __init__(self, money, distance):
#         self.money = money
#         self.distance = distance
#
#     def calculate_fare(self):
#         cost = Taxi.default_fare
#         if self.distance > Taxi.default_distance:
#             cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km
#
#         return cost
#
#     def get_change(self):
#         return self.money - self.calculate_fare()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_fare(), taxi.get_change())
#
# taxi = Taxi(30000, 10)
# print(taxi.calculate_fare(), taxi.get_change())


# 실습 2.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        # 총 수익을 저장할 동적 변수 선언
        self.income = 0

    # 요금 계산 메소드
    def calculate_fare(self, money, distance):
        # 정적 변수 가져다가 cost 변수에 할당
        cost = Taxi.default_fare

        # 메소드가 전달 받은 거리가 기본 거리보다 크다면
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        # 그 동안 쌓인 요금을 전역 변수에 누적
        self.income += cost

        # 요금을 계산해야 잔돈 계산이 되기 때문에, 요금 계산 메소드의 클로저로 생성
        # 요금 계산 메소드 내부에 선언되었기 때문에, 해당 메소드가 받은 money 매개변수 사용 가능
        def get_change():
            return money - cost

        return cost, get_change()

# 생성자를 이용해서 변수에 클래스 할당
taxi = Taxi()

# 택시 측에서 일정 거리를 이동하고 일정 금액을 받았을 때, 총 택시비와 잔돈 출력
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))

# 현재 택시 측에 쌓인 총 수익 출력
print(taxi.income)

