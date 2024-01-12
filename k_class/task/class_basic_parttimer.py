# '모든 직원' 에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원' 별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
# '근무 시간 + 상여금' 에 따른 직원 급여 계산
# '상여금' 은 지정 하지 않으면 0 으로 처리

class PartTimer:
    # 기본적인 시급과 총 파트 타이머 수를 정적 변수로 생성
    # 이 클래스를 사용하는 변수가 새로 만들어지더라도, 값이 초기화 되지 않게 하기 위함
    pay_per_hour = 10000
    total_of_part_timers = 0

    # 생성자 관련 파트
    # 인자로 받아야 되는 것 - 별명, 근무지(기본값 '청담동')
    def __init__(self, nickname, work_space="청담동"):
        # 입력값 받아서 각 변수에 할당
        self.nickname = nickname
        self.work_space = work_space

        # 생성된 객체 별 총 누적 급여를 저장할 함수
        self.total_money = 0

        # 직원 하나 생성할 때마다 총 직원수 + 1
        PartTimer.total_of_part_timers += 1

    # 직원 별 급여 계산 메소드 - 업무 시간, 상여금(기본값 0)을 받음
    def calculate_money(self, work_hour, bonus=0):
        # 일당 = 업무 시간 * 시급 + 상여금
        # 이 total_money는 함수 내의 지역변수로, 이번에 받은 금액(일당)을 의미
        total_money = PartTimer.pay_per_hour * work_hour + bonus

        # self.total_money는 클래스 내의 전역변수로, 지금까지 받은 총 금액을 의미
        # 둘은 별개로 취급하며, 이 차이를 보여주기 위해 일부러 이름을 똑같이 지정(동명이인 같은 거라고 생각하면 됨)
        # 총 급여에 이번에 받은 값 누적
        self.total_money += total_money

# 생성자를 이용해서 PartTimer 클래스를 가진 새로운 변수 생성
part_timer1 = PartTimer("KGH", "역삼동")

# 현재까지 받은 총 금액, 파트타이머 별명, 근무지 출력
print(part_timer1.total_money, part_timer1.nickname, part_timer1.work_space)

# 급여 계산 메소드로 일당 지급하고, 위와 같은 거 출력
part_timer1.calculate_money(8, 10000)
print(part_timer1.total_money, part_timer1.nickname, part_timer1.work_space)

part_timer1.calculate_money(7, 15000)
print(part_timer1.total_money, part_timer1.nickname, part_timer1.work_space)
