# 1번 1~15까지 출력
# for i in range(15):
#     print(i + 1)


# 2번. 30~1까지 출력
# for i in range(30):
#     print(30 - i)


# 3번. 1~100가지 중 홀수만 출력
# for i in range(1, 101, 2):
#     print(i)

# 반복 횟수는 50번(홀수만 세므로)
# (0 ~ 49) * 2 + 1 == 1 ~ 99
# for i in range(50):
#     print(i * 2 + 1)


# 4번. 1~10까지 합 출력
# 합계값 저장할 변수의 초기값 지정
# sum = 0

# 반복문 돌리면서 이전의 sum 값에 현재 i 값을 더하고, 그 합계를 다시 sum에 저장
# sum += i 는 sum = sum + i 와 같은 의미
# 10까지 반복해야 되는데 초기값은 0 -> 따라서 반복횟수는 11번
# for i in range(11):
#     sum += i

# 만약 끝 값을 10으로 설정했다면, i 값이 0부터 시작한다는 점 주의
# for i in range(10):
#     sum += i + 1

# 결과값 출력
# print(sum)


# 5번. 1~n까지 합 출력
# 입력할 때의 메세지를 변수로 지정
# message = '숫자를 입력하세요: '

# 입력값을 input으로 받고, int() 함수를 사용하여 정수로 형변환
# num = int(input(message))

# 초기값 설정
# sum = 0

# 반복문
# num + 1을 맨 끝 값으로 해야 num이 될 때까지 반복을 돌림
# for i in range(num):
#     sum += i + 1

# 결과 메세지 변수화
# result_message = f'1부터 {num}까지의 합은 {sum}입니다'

# 결과 메세지 출력
# print(result_message)


# 6번. 3 4 5 6 3 4 5 6 3 4 5 6 출력
# 3 4 5 6 을 숫자가 아니라, 문자열 '3 4 5 6 '으로 본다면?

# 반복할 문자열 생성
# num_string = '3 4 5 6 '

# 최종 반복횟수를 저장할 변수 생성하고 초기화
# repeat_time = 0

# 반복문 돌려서 repeat_time을 1씩 늘림
# for i in range(3):
#     repeat_time = i + 1

# num_string을 repeat_time 값만큼 반복
# print(f'{num_string * repeat_time}')


# 6-2번. 만약 숫자로 계산하고 싶다면?
# 나머지 연산자를 사용해보자
# 숫자 4개가 반복되므로 4로 나눈 나머지(0 ~ 3)에 +3을 하면 3 ~ 6이 된다
for i in range(12):
     print(i % 4 + 3, end=' ')

# 7번. '1,235,500'을 1235500으로 출력
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i

result = int(result)
print(result + 5)

