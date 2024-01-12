# 리스트 내에 있는 리스트들 중, 어느 위치에 놓을 것인지를 정하기 위한 변수를 따로 설정
bank_index = 0


# 중복 체크 함수 - 계좌 번호, 휴대폰 중복 체크에 사용
# 매개변수로 계좌 번호 or 휴대폰 번호 여부(str)과 번호(계좌/휴대폰)를 받음
# 해당 항목이 기존 리스트에 있는지 검사

# Bank 클래스 내 banks 라는 이름의 list의 각 인덱스(dict 데이터)를 돌면서 입력값과 일치하는 게 있는지 검사
# 1. 가장 외부에 있는 리스트(Bank.banks)에서 특정 은행의 리스트을 지정(banks[bank_index])
# 2. 해당 리스트 내에 있는 인덱스를 0번 ~ 끝번까지 순회
# 3. 거기서 입력한 값이랑 일치하는 게 있는지 검사
def check(*, account_or_phone, num) -> bool:
    for i in range(len(Bank.banks[bank_index])):
        # 만약 순회 도중에 해당 키 값이 입력값과 같다면 True 반환
        if Bank.banks[bank_index][i][account_or_phone] == num:
            return True

    # 만약 리스트 전체를 순회하는 동안 못 찾았다면 False 반환
    return False


# 은행 클래스
class Bank:
    # 정적 변수
    total_count = 3

    # 일단 각 은행 별 회원 정보를 저장할 2차원 리스트 생성
    # 인덱스 번호: 0 - 신한, 1 - 국민, 2 - 카카오
    banks = [[] for count in range(total_count)]

    # 클래스 객체 선언시 입력 받을 값들 - 키 = 값 형태(dict)로 받음
    def __init__(self, **kwargs):
        self.owner = kwargs.get('owner')
        self.account_number = kwargs.get('account_number')
        self.phone = kwargs.get('phone_number')
        self.password = kwargs.get('password')
        self.bank_balance = kwargs.get('bank_balance')

    # 계좌 개설 메소드: 클래스 메소드 = __init__ 실행 전 탈취해서 사용
    # 아래의 중복 검사 메소드에서 통과해야 실행
    @classmethod
    def open_account(cls, **kwargs):
        data_dict = {"owner": kwargs.get('owner'),
                     "account_number": kwargs.get('account_number'),
                     "phone_number": kwargs.get('phone_number'),
                     "password": kwargs.get('password'),
                     "bank_balance": kwargs.get('bank_balance')}

        # Bank 클래스 자체에 저장된 사용자 리스트에, 입력 받은 dict 데이터를 append
        # 각 은행 중 어디에 들어갈 것인지에 대한 값은 각 자식 클래스가 선언될 때마다 재할당됨
        Bank.banks[bank_index].append(data_dict)

        return data_dict

    # 계좌번호 중복 검사 메소드
    # 개설에만 사용
    @staticmethod
    def check_account_number(account):
        return check('account_number', account)

    # 전화번호 중복 검사 메소드
    # 개설에만 사용
    @staticmethod
    def check_phone(phone):
        return check('phone_number', phone)

    # 입금 메소드 - 입금할 금액 입력받음
    def deposit(self, amount: int):
        # 0원보다 큰 돈을 입금했는지 검사
        if amount > 0:
            self.bank_balance += amount

    # 출금 메소드 - 출금할 금액과 비밀번호 입력받음
    def withdraw(self, amount: int):
        # 사용자로부터 메세지 입력받음
        password_confirm = int(input(password_message))

        # 만약 비밀번호가 틀렸다면 에러 출력
        if password_confirm != self.password:
            print(f"비밀번호가 일치하지 않습니다. {error_message}")

        else:
            # 비밀번호가 일치했다면, 다음은 현재 잔고보다 같거나 적은 금액을 출금했는지 검사
            if self.bank_balance >= amount:
                # 만약 그렇다면 해당 수치만큼 잔고 차감
                self.bank_balance -= amount

            else:
                print('잔고가 부족합니다')

    # 잔액 조회 메소드
    def balance(self):
        # 사용자로부터 메세지 입력받음
        password_confirm = int(input(password_message))

        # 만약 비밀번호가 틀렸다면 에러 출력
        if password_confirm != self.password:
            print(f"비밀번호가 일치하지 않습니다. {error_message}")

        # 비밀번호가 일치했다면 현재 잔고 출력
        else:
            print(f'잔고: {self.bank_balance}원')

    # 매직 메소드를 이용해 __str__ 재정의
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.bank_balance}'


# 아래 클래스들은 새로운 인자를 요구하지 않으니, 생성자는 생략함
# Bank 클래스 자체에서 선언된 bank_index(목표 인덱스 값)를 각 자식 클래스마다 다른 값으로 재할당
# 신한 - 입금(deposit) 시 수수료 50%
class ShinHan(Bank):
    # 다른 은행 업무를 처리하다가 다시 신한은행 업무를 보는 경우
    # 목표 인덱스를 0으로 초기화
    Bank.bank_index = 0
    
    # 입금 메소드 오버라이드
    def deposit(self, amount: int):
        # 입력값 절반으로 하고, 그 몫(정수)를 Bank 클래스의 deposit 메소드에 넣어줌
        if amount > 0:
            amount //= 2
            super().deposit(amount)


# 국민 - 출금(withdraw) 시 수수료 50%
class KookMin(Bank):
    Bank.bank_index = 1
    
    # 출금 메소드 오버라이드
    def withdraw(self, amount: int):
        # 입력값 1.5배하고 Bank 클래스의 withdraw 메소드에 넣어줌
        amount *= 1.5
        super().withdraw(int(amount))


# 카카오 - 잔액 조회 재산 절반
class Kakao(Bank):
    Bank.bank_index = 2
    
    # 잔액 조회 메소드 오버라이드
    def balance(self):
        password_confirm = int(input(password_message))

        if password_confirm != self.password:
            print(f"비밀번호가 일치하지 않습니다. {error_message}")

        else:
            print(f'잔고: {self.bank_balance / 2}원')


# 메인 시스템
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    # 은행 메뉴
    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    # 서비스 메뉴
    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    # 은행 메뉴
    while True:
        # 오류 출력 여부 False로 초기깂 지정
        is_error = False

        # 원하는 은행 선택
        main_formatting = f'원하는 거래처를 선택해주세요\n{bank_menu}'
        main_answer = int(input(main_formatting))

        # 4. 나가기 선택 시 반복문 탈출
        if main_answer == 4:
            break

        # 1 ~ 3 - 선택에 따라 bank 변수에 다른 클래스(은행) 지정
        elif 1 <= main_answer <= 3:
            if main_answer == 1:
                bank = ShinHan()

            elif main_answer == 2:
                bank = KookMin()
                
            else:
                bank = Kakao()

        # 1 ~ 4 이외의 숫자 입력받으면 오류 발생 및 프로그램 종료
        else:
            print(error_message)
            break

        # 서비스 메뉴
        while True:
            # 원하는 서비스 선택
            service_formatting = f'원하는 서비스를 선택해주세요\n{menu}'
            service_answer = int(input(service_formatting))

            # 개설
            if service_answer == 1:
                # 이름부터 순서대로 정보 입력
                name = input(owner_message)
                account_number = input(account_number_message)
                # 분기 처리(중복 검사 메소드) - 중복된 경우 = False
                if not bank.check_account_number(account_number):
                    print(error_message)
                    # 아래 문장 실행 안 하고 탈출
                    continue

                phone_number = input(phone_message)
                if not bank.check_phone(phone_number):
                    print(error_message)
                    continue

                # 비밀번호와 예치금은 정수(int)로 입력
                password = int(input(password_message))
                bank_balance = int(input(money_message))

                # 만약 중간에 계좌 번호나 전화 번호 중복에 안 걸렸으면 클래스 메소드 실행
                # 클래스 메서드 자체가 append() 함수를 실행하므로, 여기서 따로 append 할 필요 없음
                bank.open_account(owner=name, account_number=account_number,
                                  phone_number=phone_number, password=password,
                                  bank_balance=bank_balance)

            # 입금
            elif service_answer == 2:
                # 입력받은 금액만큼 입금
                # 단, 신한은행은 입금액이 절반(수수료 50%)
                deposit_amount = int(input(deposit_message))
                bank.deposit(deposit_amount)

            # 출금
            elif service_answer == 3:
                # 입력받은 금액만큼 출금
                # 단, 국민은행은 출금액이 절반(수수료 50%)
                withdraw_amount = int(input(withdraw_message))
                bank.withdraw(withdraw_amount)

            # 조회
            elif service_answer == 4:
                # 현재 잔고 조회
                # 단, 카카오뱅크는 절반의 금액이 출력
                print(f'현재 잔고: {bank.bank_balance}')

            # 나가기
            elif service_answer == 5:
                break

            # 1 ~ 5 이외의 번호를 입력받으면 오류 메세지 출력하고 메인 메뉴로 돌아가기
            else:
                print(error_message)
                break
