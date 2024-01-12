# Comprehension(어떤 뜻을 내포하고 있음)
# 반복하거나, 특정 조건을 만족하는 list를 보다 쉽게 만들어내기 위한 방법

# List Comprehension
# [표현식 for 항목 in Iterator (if 조건)]
# num_list = [1 ,2, 3, 4]

# 위 list에서 각각의 요소에 3을 곱하고 싶다면
# 리스트 안에서 for문을 쓸 때는 얻고자하는 결과값(여기서는 number * 3)을 for문 앞에 기재
# result_list = [number * 3 for number in num_list]

# print(result_list)

# number_list = [1 ,2, 3, 4]

# 위 요소에서 연산을 통해 [6, 12] 산출
# 짝수(number % 2 == 0)만 가져와서 * 3
# result_list = [number * 3 for number in number_list if number % 2 == 0]

# print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in Iterator]
# 위의 if 조건문과 아예 다름. 다른 언어의 삼항 연산자와 유사함
# [1, 6, 3, 12]
# number_list = [1, 2, 3, 4]

# 1. for number in number_list -> 이걸로 먼저 다 가져오고
# 2. number * 3 if number % 2 == 0 else number -> 각 요소를 조건에 따라 서로 다르게 연산
# result_list = [number * 3 if number % 2 == 0 else number for number in number_list]

# print(result_list)

# 1. 아래의 list에서 '양수'만 추출한 뒤 새로운 list에 담기
# number_list = [10, 20, 30, -20, -3, 50, -70]

# 조건에 맞는 요소들을 담을 새로운 리스트 생성
# new_list = []

# 양수(number > 0)만 추출하고, 새로운 변수에 해당 리스트 할당
# new_list = [number for number in number_list if number > 0]

# 리스트 출력
# print(new_list)

# 2. n개의 0으로만 채워진 list
# 0의 개수를 입력받음
# message = "원하는 0의 개수를 입력해주세요: "
# count = int(input(message))

# '0'들을 담을 list 생성
# zeros_list = []

# count 수만큼 '0'을 리스트에 추가
# zeros_list = [0 for i in range(count)]

# 리스트 출력
# print(zeros_list)


# 3. 제곱의 결과가 10보다 큰 요소만 담은 list
# number_list = [1, -2, 3, -4, 5]

# 분류된 요소들만 담을 새로운 리스트 생성
# refined_list = []

# 제곱이 10보다 큰(number ** 2 > 10) 요소만 반환해서 새로운 리스트에 할당
# refined_list = [number for number in number_list if number ** 2 > 10]

# 분류된 리스트 출력
# print(refined_list)


# 4. 0~9까지 중 3의 배수만 담은 list
# 0~9 중 0이 아니며, 3의 배수(i % 3 == 0)인 것들만 골라서 리스트 생성
num_list = [i for i in range(10) if i % 3 == 0 and i != 0]

# 리스트 출력
print(num_list)

