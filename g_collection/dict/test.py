# 1 ~ 20 사이의 소수만 분류해서 리스트 생성 - comprehension 사용
# 조건식을 따로 변수로 만들기

# 소수의 조건
# 1이 아니면 조건 만족

# 아래 조건을 만족하는 수는 제외
# 2로 나눈 몫이 2 이상 and 나머지는 0
# 3으로 나눈 몫이 2 이상 and 나머지는 0
# 5로 나눈 몫이 2 이상 and 나머지는 0
# 7로 나눈 몫이 2 이상 and 나머지는 0

# # 조건식에 사용할 변수의 초기값 지정
# num = 0
#
# # 1이 아님 조건식 생성
# cond1 = num != 1
#
# # 2 관련 조건식
# cond2 = num // 2 >= 2 and num % 2 == 0
#
# # 3 관련 조건식
# cond3 = num // 3 >= 2 and num % 3 == 0
#
# # 5 관련 조건식
# cond5 = num // 5 >= 2 and num % 5 == 0
#
# # 7 관련 조건식
# cond7 = num // 7 >= 2 and num % 7 == 0
#
# # 위에 거 다 때려넣은 컴프리헨션 생성?
# # 아니면 만들기 전에 미리 합칠까?
# final_condition = cond1 and not cond2 and not cond3 and not cond5 and not cond7
#
# # 자료 생성(1~20까지 들어있는 리스트)
# test_list = [i + 1 for i in range(20)]
#
# # 조건 적용된 값만 뽑아내는 컴프리헨션
# print([i for i in test_list if final_condition])


# 소수 리스트 뽑아내는 함수 코드
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(1000))