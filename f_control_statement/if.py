# num = 15
#
# if num % 3 == 0 :
#     print(f"{num}은(는) 3의 배수입니다")
# if num % 5 == 0 :
#     print(f"{num}은(는) 5의 배수입니다")


# number가 양수인지, 음수인지, 0인지 검사
# number = 0

# 조건식 변수화
# pos_condition = number > 0
# neg_condition = number < 0

# if pos_condition:
#     print(f'{number}은(는) 양수입니다')
# elif neg_condition:
#     print(f'{number}은(는) 음수입니다')
# else:
#     print(f'{number}은(는) 0입니다')
    
    
# 나이를 입력받은 후, 미성년자인지 검사
# input으로 입력받고, int() 함수로 형변환
# message = "나이를 입력하세요: "
# age = int(input(message))

# 조건식 변수화
# is_not_adult = 0 < age < 20
# error_condition = age <= 0

# 조건식 결과에 따라 서로 다른 문장 출력
# if is_not_adult:
#     print("미성년자입니다")
# elif error_condition:
#     print("나이를 잘못 입력하셨습니다")
# else:
#     print('성인입니다')

# 두 정수를 입력받은 후, 대소비교 진행
# message = '정수 2개를 아래와 같이 입력해주세요'
# ex_message = 'ex) 1 3'

# 정수 2개를 공백(split() 함수에 기본 설정된 구분점)에 따라 분리하고, 전부 int 형으로 변환
# num1, num2 = map(int, input(message + '\n' + ex_message + '\n').split())

# 각 조건식을 변수화
# condition_left = num1 > num2
# condition_right = num1 < num2

# 선언할 때 어떤 값을 넣을지 모르는 경우, 초기값을 넣어준다
# 다른 개발자들에게 어떤 유형의 값을 넣을지 알려주기 위함
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: False
result_message = ''

# 설정한 조건식으로 조건문 작성하고
# 분기에 따라 서로 다른 메세지 반환
# if condition_left:
#     result_message = f'{num1}이(가) {num2}보다 큽니다'
# elif condition_right:
#     result_message = f'{num1}이(가) {num2}보다 작습니다'
# else:
#     result_message = '두 개의 값은 같습니다'

# 위 조건식에 따라 서로 다른 문자열을 print
# print(result_message)

print(list(range(10)))