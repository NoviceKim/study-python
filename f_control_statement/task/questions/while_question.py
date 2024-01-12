# while문 문제
# 'Hello Python!' 이라는 문장을 원하는 횟수만큼 출력하는 코드

# 원하는 횟수를 입력받을 변수 생성
while_message = "'Hello Python!' 문장을 출력할 횟수를 입력해주세요: "
count = int(input(while_message))

# 현재 반복 횟수를 저장할 변수의 초기값 지정
repeat_time = 0

# while문으로 repeat_time < count가 False가 될 때까지 반복
while repeat_time < count:
    # 반복이 진행되는 동안 출력될 문장의 서식(문자열)을 변수에 저장
    while_formatting = f"'Hello Python!' ({repeat_time + 1})"

    # 반복이 진행되는 동안 문장 계속 출력, 반복 횟수 +1 해주기
    print(while_formatting)
    repeat_time += 1
