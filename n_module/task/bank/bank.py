# bank_module.py와 message_module.py 안에 있는 내용물을 전부 가져옴
from bank_module import *
from message_module import *


# 실행부 - 코드는 여기부터 실행됨
# if __name__ == '__main__' - 이 파일이 실행하는 파일임을 의미
if __name__ == '__main__':
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
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    # None은 False 값이지만, 직관성 및 가독성을 확보하기 위해 is 연산자로 검사한다
                    # 만약 계좌번호 중복 메소드 반환값이 None 일 경우
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break

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
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)

                # 만약 회원 정보를 찾았다면
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
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
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
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                    #
                    phone = input(phone_message)
                    user = Bank.check_phone(phone)

                    if user is not None:
                        if user['password'] == input(password_message):
                            while True:
                                account_number = input(account_number_message)
                                if Bank.check_account_number(account_number) is None:
                                    break
                            # 새로 설정한 계좌번호로 기존 번호를 덮어씌운다
                            # 계좌를 개설할 때(open_account 클래스 메소드 사용), __dict__ 로 저장했다
                            # 이 경우, __dict__ 를 수정하는 것보다, 객체로 직접 접근해서 바꾸는 게 안전하다
                            # 결국 __dict__ 도 self를 받아서 만들어진 객체이므로
                            # 뿌리인 self로 접근해서 바꾸는 게 안전하다
                            # 뿌리를 바꾸면, 거기서 파생된 모든 것이 바뀐다
                            user.get('object').account_number = account_number
                            continue

                    else:
                        print('휴대폰 번호나 계좌번호를 다시 확인해주세요')

            # 서비스 메뉴의 else문 - 1~6번에 걸리지 않으면 전부 다 여기로 온다
            else:
                print(error_message)
