# bank.py에 들어가는 메세지 변수들을 이 파일에 따로 분리

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
