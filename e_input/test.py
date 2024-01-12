# 실습
# 1. 현재 시간을 입력하고, 시간과 분을 분리하여 출력
# message = '현재 시간을 입력해주세요: '
# time = input(message)
#
# hour, minute = time.split(':')
#
# formatting = f'현재 시간은 {hour}시 {minute}분 입니다'
#
# print(formatting)


# 2. 핸드폰 번호를 -(하이픈)과 함께 입력받은 뒤, 각 자리의 번호를 분리하여 출력
# message = '휴대폰 번호를 아래 예시처럼 입력해주세요'
# ex_message = 'ex) 010-1234-5678'
#
# phone1, phone2, phone3 = input(message + '\n' + ex_message + '\n').split('-')
#
# formatting = f'입력하신 번호는 {phone1}, {phone2}, {phone3} 입니다'
#
# print(formatting)


# 3. 이름과 나이를 한 번에 입력받은 뒤, "000님의 나이는 00살 형식으로 출력"
# message = '이름과 나이를 아래 예시처럼 입력해주세요'
# ex_message = '김광협 26'
#
# name, age = input(message + '\n' + ex_message + '\n').split()
#
# formatting = f'{name}님의 나이는 {age}살 입니다'
#
# print(formatting)


# 4. 3개의 정수를 입력받은 뒤, 덧셈 결과 출력

# 출력 메세지(문자열)를 변수에 할당
message = '덧셈 할 정수 3개를 아래 예시처럼 입력해주세요'
ex_message = 'ex) 1, 3, 5'

# 입력받은 정수 3개와, 그 합을 저장할 변수 선언
# input으로 받은 문자열을 split을 사용해서 구분점(, )에 따라 분리 -> 1개의 list안 3개의 str 값
num1, num2, num3 = map(int, input(message + '\n' + ex_message + '\n').split(', '))
sum = num1 + num2 + num3

# 결과 출력 메세지 formatting
formatting = f'입력하신 {num1}, {num2}, {num3}의 합은 {sum}입니다'

print(formatting)
