# unpacking - 값을 풀어서 적는 것
# def get_total(num1, num2, num3):
#     return num1 + num2 + num3

# packing - 값을 묶어서 적는 것
# def get_total(*numbers):
#     # 외부에서 전달받은 값들이 numbers(튜플)에 저장된다
#     print(type(numbers))    # tuple
#
#     total = 0
#
#     for number in numbers:
#         total += number
#
#     return total

# result = get_total(1, 2, 3, 4, 5)
#
# print(result)

# 여러 개의 값을 한 번에 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통째로 들어가게 된다
# 즉, ([1, 2, 3, 4, 5], ... ) 같이 전달된다
# numbers = [1, 2, 3, 4, 5]

# 함수에 여러 개의 데이터를 담은 매개변수를 전달할 때
# 앞에 * 를 붙이면, 해당 변수가 가리키는 곳(변수 내부의 요소들)에 직접 접근하며
# 그 요소들을 각각 전달하게 된다.
# total = get_total(*numbers)

# print(total)


# 1. 국어, 영어, 수학 점수를 전달받은 뒤, 총점을 출력하는 함수
# packing을 이용해서 제작

# packing의 원리를 이용해서 여러 개의 변수를 튜플로 묶어서 매개변수로 받음
# def score_total(*scores):
#     # 총점의 초기값 설정
#     total = 0
#
#     # 매개변수로 받은 점수 데이터들을 순회하며
#     for score in scores:
#         # 그 값들을 total에 추가
#         total += score
#
#     # 최총 합계 반환
#     return total
#
# # 점수 데이터들이 담긴 list 생성
# result = [90, 85, 100]
#
# # 점수 데이터(list) 안에 있는 내용물들을 풀어서(*) score_total 함수에 전달한 다음,
# # 함수 연산으로 나온 결과를 변수에 할당
# final_score = score_total(*result)
#
# print(final_score)


# 2. 문자열에서 대문자 'A'가 몇 개 있는지 검사하는 함수
# 마찬가지로 packing을 이용해서 제작

# 문자열도 리스트의 일종이다
def check_count_of_a(*targets):
    # 매개변수로 전달된 문자열들(targets)을 인덱스 순으로 순회하면서
    # 각 인덱스 내 문자열에서 'A'의 개수를 해당 인덱스(같은 번호)에 넣어서 반환
    return [str.count('A') for str in targets]

# 위 list의 내용물을 풀어서 함수에 전달 -> 리턴값을 변수에 할당
check = check_count_of_a('Apple', 'BanAna', 'Carrot', 'Dill', 'EggplAnt')

print(check)
