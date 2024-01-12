# for문 문제
# n번째 피보나치 수 구하기

# 알고 싶은 n번째 피보나치 수를 출력하기 위해, n의 값을 입력 받음
for_message = 'n번째 피보나치 수: '
count = int(input(for_message))

# n-1, n-2번째 피보나치 수를 초기값으로 지정
fib_n_1 = 1
fib_n_2 = 1

# n번째 피보나치 수를 for문으로 구현
# i = 0; i < count; i ++
for i in range(count):
    # 만약 1을 입력했다면, 첫 번째 피보나치 수인 1을 출력
    if i == 0:
        fibonacci = 1
        continue

    # n번째 피보나치 수 = 그 이전 수 2개의 합
    fibonacci = fib_n_1 + fib_n_2

    # n-1, n-2번째 값을 한 칸 뒤의 것으로 재할당
    # ex) 2번째 -> 3번째, 3번째 -> 4번째
    fib_n_1 = fib_n_2
    fib_n_2 = fibonacci

# 출력할 문자열을 변수에 할당
for_formatting = f'{count}번째 피보나치 수는 {fibonacci}입니다'

# 문자열 출력
print(for_formatting)
