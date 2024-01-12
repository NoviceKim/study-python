# email을 입력받고, 아이디와 도메인(사이트 주소)을 각각 분리하여 출력한다
# .split('@') 사용

# input으로 입력받은 문자열을 변수에 저장
# message = input('email 주소를 입력하세요: ')

# .split()을 사용해서 '@'을 기준으로 문자열 분리하고 각각 다른 변수에 저장
# email_id, email_domain = message.split('@')

# id와 도메인 값으로 formatting 문자열 생성
# formatting = f'아이디: {email_id}\n도메인: {email_domain}'

# 문자열 출력
# print(formatting)


# 첫 번째 값으로 yard, 두 번째 값으로 인치를 입력받아
# 각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘째자리까지 출력한다

# 문제 메세지 문자열을 변수에 저장
message = '야드와 인치 값을 아래 예시처럼 입력하세요'
ex_message = 'ex) yard 입력: 10\ninch 입력: 10'

# 문제 메세지 출력
print(message + '\n' + ex_message + '\n')

# 야드와 인치 값을 input으로 입력받고, 아래의 연산을 위해 float로 형변환
yard = float(input('yard 입력: '))
inch = float(input('inch 입력: '))

# 형변환한 input 값으로 연산하고 변수에 저장
# round로 감싸서 소수점 2번째 자리 반올림하고, 뒷자리 0은 생략함
yard_cm = round(yard * 91.44, 2)
inch_cm = round(inch * 2.54, 2)

yard_formatting = f'{yard} yard는 {yard_cm}cm'
inch_formatting = f'{inch} inch는 {inch_cm}cm 입니다'

print(yard_formatting, inch_formatting, end='\n')
