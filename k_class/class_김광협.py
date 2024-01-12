# - 기본 출연료: 100000원
# - 기본 출연 시간: 1시간
# - 1시간 초과 당 : 50000원

# ○ TV 프로그램
# 1. 프로그램 이름, 유형(예능, 다큐 등..), 방송 분량(시간 단위), 출연자 수
# 2. TV 프로그램 정보 출력 메소드

# ○ 출연자
# 1. 이름, 나이, 직업(코미디언, 가수, 배우 등..), 출연료
# 2. 출연자가 추가될 때 마다 출연자 수 1증가
# 3. 방송 분량에 따른 출연료 계산 메소드 정의
# 4. 출연자는 인당 1개의 프로그램에만 참여할 수 있음

# 프로그램 클래스
class Program:
    # 생성자 - 이름, 유형, 방송 분량, 출연자 수 순으로 입력받음
    def __init__(self, name: str, program_type: str, running_time: int, casts: int):
        self.name = name
        self.program_type = program_type
        self.running_time = running_time
        self.casts = casts

    # 프로그램 정보 출력 메소드
    # 위에서 입력받은 것들을 콤마(,)를 구분점으로 해서 출력
    def print_program_info(self):
        print(self.name, self.program_type, self.running_time, self.casts, sep=', ')


# 출연자 클래스
class Cast:
    # 전체 출연자 수를 저장할 변수 생성(초기값 0)
    total_casts = 0

    # 기본 출연료, 기본 출연 시간, 초과시간 1시간 당 출연료도 클래스 자체에 저장
    base_pay = 100000
    base_time = 1
    additional_pay = 50000

    # 생성자 파트 - 이름, 나이, 직업을 입력받음
    def __init__(self, name: str, age: int, job: str):
        self.name = name
        self.age = age
        self.job = job

        # 클래스 자체에 있는 총 출연자 수 +1
        Cast.total_casts += 1

    # 방송 시간에 따른 총 출연료 - 프로그램 클래스를 가진 객체를 입력받음
    def calculate_pay(self, program):
        # 총 출연료 = 100000 + (출연 시간 - 1) * 50000
        total_pay = Cast.base_pay + (program.running_time - 1) * Cast.additional_pay

        # 출연료 계산 결과를 정수형(int)으로 반환
        return int(total_pay)


# Program 클래스로 객체 생성
# 프로그램 정보 출력
program_1 = Program('연기대상', '시상식', 4, 6)
program_2 = Program('편스토랑', '예능', 2, 10)

# 프로그램 정보 출력
program_1.print_program_info()
program_2.print_program_info()

# Cast(출연자) 클래스로 객체 생성
cast_1 = Cast('남궁민',45, '배우')
cast_2 = Cast('류수영', 44, '배우')

# 출연자 별로, 특정 프로그램에 출연했을 때 방송 시간에 따른 총 출연료 출력
print(cast_1.calculate_pay(program_1))  # 100000 + (4 - 1) * 50000 = 250000
print(cast_2.calculate_pay(program_2))  # 100000 + (2 - 1) * 50000 = 150000
