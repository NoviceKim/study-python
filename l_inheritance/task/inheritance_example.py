# 중복 검사 함수
# Bank 클래스 내 메소드에서 사용 - 핸드폰 번호와 계좌 번호 검사
# 어떤 것을 검사할 지는 사용자에게 전달받은 key로 확인할 수 있다
def check(*, key: str, value: str):
    # 저장소(DB)에서 각 은행의 고객 리스트를 가지고 온 다음,
    for bank in Bank.banks:
        # 각 은행에서 회원 정보(dict)를 하나하나씩 가지고 온다
        for user in bank:
            # 전달받은 값(key)로 회원의 정보와 일치하는 지 검사
            if user[key] == value:
                # 만약 일치하면 해당 회원의 정보(dict)를 반환
                return user
    # 만약 찾지 못했다면 None을 반환
    return None


# Bank 클래스
class Bank:
    # 총 은행 수
    total_count = 3

    # 총 은행 수만큼 리스트 안에 리스트 생성
    banks = [[] for i in range(total_count)]

    # Bank 클래스를 불러오면 실행될 생성자
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # 객체가 생성될 때, 'object' 라는 변수가 같이 만들어지고
        # 'object' 필드에는 필드의 주소값(self)이 담긴다
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 계좌 개설 메소드 - 어떤 은행에서 개설할 지를 bank_choice에 입력받음
    # 개설에 필요한 기타 모든 정보는 **kwargs에 전달받음
    # 클래스 메소드 - 만약 객체를 open_account() 메서드를 통해 접근하게 되면
    # bank_choice(1~3) + 기존에 입력받았던 것들을 입력받아서 가공 처리 후 생성자에 전달한다
    @classmethod
    def open_account(cls, bank_choice: int, **kwargs):
        # 회원이 어떤 은행에서 개설할 지, 이 시점에서는 아직 알 수 없음
        # 우선, 아래의 자식 클래스들을 하나의 리스트로 묶음
        # 그리고, '입력한 값 - 1' 번 인덱스에 있는 자식 클래스에
        # 입력한 다른 데이터 값들 넣고 해당 자식 클래스의 생성자 선언 -> user 변수에 할당(객체 타입)
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 그리고 원본 클래스(Bank)의 banks(list)의 '입력한 값 - 1' 번 인덱스(list) 에
        # 아까 만든 user(생성자)를 dict 타입으로 바꿔서 넣어주기
        # check(중복 검사) 함수에서 원하는 key로 회원 정보를 찾기 위함
        cls.banks[bank_choice - 1].append(user.__dict__)
        # 개설된 회원 정보 반환
        return user

    # 계좌번호 중복 체크 메소드 - 계좌번호(str)를 인자로 받음
    # staticmethod 인 이유는, self에 접근할 필요가 없기 때문
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check(중복 검사) 함수 안에 'account_number'(key)와 입력값(value) 넣은 결과를 반환(dict 타입)
        return check(key='account_number', value=account_number)

    # 전화번호 중복 체크 메소드
    @staticmethod
    def check_phone(phone: str) -> dict:
        # key는 'phone' 이라는 것만 다르고, 나머지는 위와 동일
        return check(key='phone', value=phone)

    # 입금 메소드 - 입금액(int)을 받음
    def deposit(self, money: int):
        # 객체가 갖고 있던 money 값에 입력 값만큼 더해서 재할당
        self.money += money

    # 출금 메소드 - 출금액(int)을 받음
    def withdraw(self, money: int):
        # 객체가 갖고 있던 money 값에 입력 값만큼 빼서 재할당
        self.money -= money

    # 잔액 확인 메소드
    def balance(self):
        # 현재 money 값 반환
        return self.money

    # 매직 메소드로 str 메소드를, 아래의 값을 출력하도록 재선언
    # 객체를 출력하면 __str__() 이 실행되기 때문에, 빠르고 편하게 회원 정보 확인이 가능하다
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


# 자식 클래스들 - 신한, 국민, 카카오
# 신한은행 클래스
class ShinHan(Bank):
    # 입금(deposit) 메소드 오버라이딩
    def deposit(self, money: int):
        # 입력값(money) / 2 한 다음, 몫만 떼서 money 변수에 재할당
        money //= 2
        # 그 이후, 부모 클래스(Bank)의 입금 메소드 그대로 사용
        super().deposit(money)


# 국민은행 클래스
class KookMin(Bank):
    # 출금(withdraw) 메소드 재정의
    def withdraw(self, money: int):
        # 입력값 * 1.5 한 다음 재할당
        money *= 1.5
        # 부모 클래스의 출금 메서드 불러와서 사용
        # int로 형변환하는 이유는, 실수를 곱했기 때문에 결과값도 실수인 상태라서
        super().withdraw(int(money))


# 카카오뱅크 클래스
class KaKao(Bank):
    # 잔액조회 메소드 재정의
    def balance(self):
        # '객체를 생성했을 때' 받은 money 변수에 / 2 한 다음 몫을 재할당
        # 위의 두 클래스의 입급/출금 메소드에서 받은 'money' 랑은 다르다는 것에 주의할 것
        self.money //= 2
        # 부모 클래스의 잔액조회 메소드가 self.money를 return 하는 메소드였기 때문에
        # 자식 클래스에서도 부모 클래스의 메소드를 실행한 값을 리턴한다
        return super().balance()


# 실행부 - 코드는 여기부터 실행됨
# if __name__ == '__main__' - 이 파일이 실행하는 파일임을 의미
if __name__ == '__main__':

    # 은행 선택 메뉴를 문자열(str)로 만들어서 변수에 할당
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    # 은행 선택 이후에 띄울 업무 선택 메뉴 역시 문자열(str)로 만들어서 변수에 할당
    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 재설정\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

    # 각 메뉴에서 띄울 메세지도 문자열 형태로 변수에 할당
    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    #  while True -> 반복문 내에서 break를 만나기 전까지 무한 반복
    while True:
        # 은행 메뉴
        # 은행 선택 메뉴(bank_menu)를 띄우고 받은 입력값(숫자 1~4)을 int형으로 바꿔서 변수에 할당
        bank_choice = int(input(bank_menu))
        # 만약 '4. 나가기' 선택 시 반복문 탈출(break)
        if bank_choice == 4:
            break

        # 만약 입력받은 값이 1보다 작거나 은행 종류 수보다 크면서
        # 위에서 걸리지 않은, 즉 4번도 아닌 경우 => 메뉴에 있는 번호 이외의 숫자를 입력한 경우
        # len(Bank.banks) 인 이유는 은행 종류 수가 바뀌어도 유연하게 실행하기 위함
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            # 아래의 문장을 실행하지 않고, 다음 반복으로 넘어감
            continue

        # 위에서 반복문을 탈출하지 않았다면(걸리지 않았다면) 이하의 무한 루프 반복문 실행
        while True:
            # 서비스 메뉴
            # 업무 선택 메뉴(menu)를 띄우고 입력받은 숫자(1~6)를 menu_choice 변수에 할당
            menu_choice = int(input(menu))
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                # owner 변수에 입력값 저장
                owner = input(owner_message)

                # 조건부 무한 루프 - 중복되지 않은 계좌번호를 입력할 때까지 무한 반복
                while True:
                    # account_number 변수에 입력값 저장
                    account_number = input(account_number_message)
                    # None은 False 값이지만, 직관성 및 가독성을 확보하기 위해 is 연산자로 검사한다
                    # 만약 계좌번호 중복 메소드 반환값이 None 일 경우 = 기존 회원 중에 중복이 없을 경우
                    if Bank.check_account_number(account_number) is None:
                        # 반복문 탈출
                        break

                while True:
                    # 입력 값을 phone 변수에 저장
                    phone = input(phone_message)
                    # 기존 회원의 전화 번호와 중복되지 않을 경우, 반복문 탈출
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    # 입력값을 password 변수에 저장
                    password = input(password_message)
                    # 만약 password의 길이가 4일 경우 반복문 탈출
                    # 위 input에서 받은 값의 길이를 재기 위해서는
                    # int로 형변환하지 않고 str 형태 그대로 쓴다
                    if len(password) == 4:
                        break

                # 입력값을 int로 바꾸고 money에 저장
                # 이 문장이 실행된다는 건, 위에 있는 while 무한 루프들을 전부 탈출했다는 것을 의미
                money = int(input(money_message))

                # 계좌 개설
                # 어떤 은행에서 개설했는지는 bank_choice에 담기고
                # open_account() 메소드는 **kwargs 형태로 받으므로, 나머지 정보는 키=값 형태로 전달한다
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)

                # 위에서 재정의 된 __str__ 이 여기서 사용되고
                # 회원의 전체 정보가 출력된다
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능
            elif menu_choice == 2:
                # 계좌 번호를 입력받고
                account_number = input(account_number_message)
                # 입력받은 값을 계좌번호 중복 검사 메소드에 넣어서 나온 반환값을 user 변수에 할당
                user = Bank.check_account_number(account_number)

                # 만약 회원 정보를 찾았다면 = None이 아닌, 다른 정보(회원 정보 dict)가 반한됐다면
                if user is not None:
                    # 우선 비밀번호를 검사
                    if user['password'] == input(password_message):
                        # 신한은행에 속한 회원인지 검사
                        if isinstance(user.get('object'), ShinHan):
                            # 은행 선택에서 신한은행을 선택하지 않았을 경우
                            if bank_choice != 1:
                                # 둘이 다르므로 메세지 띄우고 나서
                                print('개설할 은행에서만 입급 서비스를 이용해주세요')
                                # 아래 문장을 실행하지 않고 다음 반복으로 넘어감
                                # 입금 서비스를 이용할 수 없게 막는 용도
                                continue

                            # 만약 위 if문에 걸리지 않았을 경우(신한은행 선택), 입금 서비스 실행
                            deposit_money = int(input(deposit_message))
                            # 계좌 개설 시 담아놓은 self(객체)를 통해 메소드에 접근한다
                            user['object'].deposit(deposit_money)

                        else:
                            print(error_message)

            # 출금
            elif menu_choice == 3:
                # 계좌번호 검사
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)

                # 계좌 확인되면
                if user is not None:
                    # 비밀번호 검사
                    if user['password'] == input(password_message):
                        # 출금액을 입력받아서 int형으로 할당
                        withdraw_money = int(input(withdraw_message))
                        # 만약 로그인 한 회원이 국민은행 회원이라면
                        # 50%의 출금 수수료가 붙기 때문에, 잔액 검사할 때 * 1.5 해준다(삼항 연산)
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)
                            continue
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                # 계좌번호 검사
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)

                # 계좌 확인되면
                if user is not None:
                    # 비밀번호 검사
                    if user['password'] == input(password_message):
                        # 비밀번호까지 확인되면 user(dict) 안에 있는 'object' 키를 찾음
                        # 해당 키에는 (자식 클래스 중 하나를 가진)객체가 담겨 있을 것이니
                        # 해당 객체에 대하여 잔액 조회 메소드 실행
                        print(f'현재 잔액: {user["object"].balance()}')
                        # 그리고 이하의 내용 무시하고 다음 반복으로
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                    # 휴대폰 번호를 입력받고
                    phone = input(phone_message)
                    # 휴대폰 번호 검사
                    user = Bank.check_phone(phone)

                    # 해당 번호가 확인되면
                    if user is not None:
                        # 비밀번호 일치하는지 검사
                        if user['password'] == input(password_message):

                            # 조건부 무한 루프 - 휴대폰/비밀번호 일치하니 새로운 계좌번호를 할당해 줌
                            while True:
                                # 계좌번호 입력받고
                                account_number = input(account_number_message)

                                # 기존 계좌번호와 중복되지 않을 경우 반복문 탈출
                                if Bank.check_account_number(account_number) is None:
                                    break
                            # 새로 설정한 계좌번호로 기존 번호를 덮어씌운다
                            # 계좌를 개설할 때(open_account 클래스 메소드 사용), __dict__ 로 저장했다
                            # 이 경우, __dict__ 를 수정하는 것보다, 객체로 직접 접근해서 바꾸는 게 안전하다
                            # 결국 __dict__ 도 self를 받아서 만들어졌므로
                            # 뿌리인 self로 접근해서 바꾸는 게 안전하다
                            # 뿌리를 바꾸면, 거기서 파생된 모든 것이 바뀐다
                            user.get('object').account_number = account_number
                            continue

                    # 휴대폰 번호, 비밀번호 쪽 if문에 걸리지 않으면 여기로 온다
                    else:
                        print('휴대폰 번호나 비밀번호를 다시 확인해주세요')

            # 서비스 메뉴의 else문 - 1~6번에 걸리지 않으면 전부 다 여기로 온다
            else:
                print(error_message)
