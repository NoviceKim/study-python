# input 함수로 입력한 값 자체가 문자열 값 = 변수에 저장할 수 있다
name = input("이름: ")
height = input("키: ")
formatting = f'제 이름은 {name}, 키는 {height}cm 입니다.'

print(formatting)

# 파이썬에서 문자열끼리 연산자를 사용하면 '연결'이 된다
# 연결(+)은 문자열끼리만 가능하다
# print('안' + '녕')

# 문자열과 다른 자료형을 연결하려고 하면 에러가 발생하기에
# str()을 사용해서 문자열로 형변환을 해줘야 한다
# data = 3
# print('안' + str(data))

# 두 정수를 입력받은 후, 곱셈 결과 출력
# message1 = '첫 번째 숫자: '
# message2 = '두 번째 숫자: '

# input은 기본적으로 str 타입의 '값'이기 때문에
# int()를 써서 정수로 형변환을 해줘야 한다
# num1 = int(input(message1))
# num2 = int(input(message2))

# 곱셈 값을 저장할 변수 선언
# sum = num1 * num2

# print()로 출력할 문자열 선언
# formatting = f'두 숫자의 곱은 {sum}입니다.'

# 문자열 출력
# print(formatting)

# split() - 특정 구분점으로 문자열 분리
# 'A,B,C' 라는 하나의 값을 'A', 'B', 'C'라는 3개의 값으로 분리한다
# 이 때 print() 함수를 써서 출력하면, []로 감싸진 list 형식으로 출력된다
print('A,B,C'.split(','))

# map(각각 어떻게 바꿀 것인가, [])
# 각각 어떻게 바꿀 것인가 - 함수의 주소(소괄호 생략)가 들어간다
# 여기서는 int가 들어갔으니, 입력한 값들을 일괄적으로 int(정수) 타입으로 변경한다
message = '두 정수를 아래 예시처럼 입력하세요'
ex_message = 'ex) 1, 3'
num1, num2 = map(int, input(message + '\n' + ex_message + '\n').split(', '))
sum = num1 * num2

formatting = f'{num1} * {num2} = {sum} 입니다'
print(formatting)

# 실습
# 현재 시간을 입력하고, 시간과 분을 분리하여 출력
# 핸드폰 번호를 -(하이픈)과 함께 입력받은 뒤, 각 자리의 번호를 분리하여 출력
# 이름과 나이를 한 번에 입력받은 뒤, "000님의 나이는 00살 형식으로 출력"
# 3개의 정수를 입력받은 뒤, 덧셈 결과 출력


