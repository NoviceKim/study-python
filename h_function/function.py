# f(x) = 2x+1

# 함수 선언
# def f(x):
#     return 2 * x + 1
#
# # 선언한 함수에 값을 넣어서 나온 리턴값을 변수에 할당
# result = f(2)
#
# print(result)


# 두 정수의 곱셈
# def num_multiple(num1, num2):
#     return num1 * num2
#
# result = num_multiple(8, 7)
#
# print(result)


# 두 정수의 나눗셈 후, 몫과 나머지 구하는 함수
# def num_divide(num1, num2):
#     # 나누는 수가 0이면 안되니, if문으로 검사
#     if num2 != 0:
#         # 몫과 나머지를 튜플로 묶어서 한 번에 반환
#         portion_rest = num1 // num2, num1 % num2
#         return portion_rest
#
#     # if문에 걸리지 않으면(num2 = 0), None 반환
#     # 에러 방지 목적. 에러 대신 None을 반환함
#     return None
#
# # 튜플형 자료 2개(몫, 나머지)를 각각 다른 변수에 할당
# portion, rest = num_divide(25, 7)
#
# print(portion, rest)


# 1~10까지 print()로 출력하는 함수
# 출력 범위가 정해져 있기 때문에 매개변수 필요 없음
# 함수 로직 자체에 출력 기능이 있기 때문에, 실행할 때는 함수 이름만 쓰면 된다
# def print_1_to_10():
#     for i in range(10):
#         print(i + 1)
#
# print_1_to_10()


# 이름을 n번 print() 해주는 함수
# def print_name(name, count):
#     for i in range(count):
#         # 몇 번째 출력인지 확인하기 위해, 현재 반복 횟수(i + 1)를 formatting 해서 같이 출력
#         print(f'{name} ({i + 1})')
#
# print_name('KGH', 10)


# 1~n까지의 합을 구해주는 함수
# def add_num_to_n(num):
#     # 최종 합계가 담길 변수 선언하고 초기값 지정
#     result_num = 0
#
#     for number in range(num):
#         result_num += number + 1
#
#     # 최종 합계 반환
#     return result_num
#
# # 함수에 10을 넣은 결과값을 변수에 할당
# result = add_num_to_n(10)
#
# print(result)


# 1~100까지 중 n의 배수를 print()로 출력해주는 함수
# 함수 안에 print() 기능이 있기 때문에 리턴 필요 없음
# print() 함수는 리턴 값이 없음. 따라서 값으로서 사용(변수에 할당 등)하는 게 불가능
def multi_of_n(num):
    # 0의 배수는 0 밖에 없으니, if문의 else로 분리
    if num != 0:
        # 1~100까지의 숫자들 중 n의 배수만 반환
        # 1. 1~100까지 순회 - for문
        # 2. 조건식 - 1~100 % n == 0 - if문
        for i in range(100):
            if (i + 1) % num == 0:
                print(i + 1, end=' ')

    # 매개변수에 0이 전달되었을 경우, 0 하나만 출력
    else:
        print(0)

# 함수의 값으로 들어간 정수의 배수만 출력
multi_of_n(0)


# 두 정수의 뺄셈 함수
# def subtract_number(num1, num2):
#     num1, num2 = int(num1), int(num2)
#
#     return num1 - num2
#
# print(subtract_number(12, 5))


# 문자열을 입력받고, 원하는 문자의 개수를 구해주는 함수

# 매개변수 - 문자열, 문자
# 리턴값 - 문자열 내에서 문자의 개수(정수)
def count_char(target, keyword):
    # 개수 저장할 변수의 초기값 지정
    count = 0

    #
    # return len([i for i in target if i == keyword])

    # 문자열을 순회하면서
    for i in target:
        # 문자와 같은 글자를 발견하면
        if i == keyword:
            # count + 1
            count += 1

    # 반복 끝난 이후의 count 값 반환
    return count

print(count_char('apple', 'p'))


'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''

# 문자열과 문자를 매개변수로 받고
def find(target, keyword):
    # 문자열 길이만큼 반복 = 문자열의 처음부터 끝까지(target[0] ~ target[len(target) - 1]) 검사
    for i in range(len(target)):
        # 만약 문자를 발견하면
        if target[i] == keyword:
            # 해당 문자의 인덱스 번호 반환
            # return을 만나면 함수 연산이 끝남
            return i

    # 위 반복문 내 if문에 걸리지 않으면(해당 문자가 없으면) 여기로 이동
    return -1

result = find('apple', 'a')

print(result)