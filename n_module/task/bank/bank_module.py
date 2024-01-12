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

