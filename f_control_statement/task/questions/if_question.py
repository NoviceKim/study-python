# if문 문제
# 점수에 따른 학점 출력

# 점수를 입력 받아서 변수에 저장
if_message = '점수를 입력해주세요: '
score = int(input(if_message))

# 학점 저장할 변수의 초기값 지정
grade = ''

# if문을 사용해서 입력한 점수에 따라 서로 다른 학점 출력
# elif, else문에 걸렸다는 것은 위쪽 조건문에 걸리지 않았다는(False) 것
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# 출력할 문자열을 변수에 할당
if_formatting = f'당신의 학점은 {grade} 입니다'

# 문자열 출력
print(if_formatting)
