# str 타입(문자열)도 여러 개의 문자로 이루어진 list의 일종
# 따라서 list에서 쓰던 메서드 사용 가능

# for i in "Apple":
#     print(i, end=" ")

# upper(), lower()
# 모든 영문자를 대문자/소문자로 변환
# print("Apple123!@#".upper())
# print("Apple123!@#".lower())

# split()
# maxsplit 옵션 = 앞에서부터 n개까지만 분리
# data = "사과, 바나나, 파인애플, 포도, 복숭아"
# print(data.split(',', maxsplit=2))

# 공백으로 구분하고 싶다면 split()안에 아무것도 입력하지 않으면 됨
# print("A B C D E F".split())

# split()안을 공란으로 두는 것과 " "을 쓰는 것은 차이가 있음
# 후자는 공백 하나하나를 요소로 취급함
# print("A          B".split())
# print("A   B".split(" "))

# join()
# 각각의 요소를 원하는 구분점으로 연결
# 구분점을 따로 지정하지 않고 빈 문자열을 전달하면 전부 붙어서 출력됨
# print(':'.join(['a', 'b', 'c']))
# print(''.join(['a', 'b', 'c']))

# replace('기존 값', '새로운 값')
# 기존 값을 새로운 값으로 변경

# 공백(" ")을 빈 문자('')로 변경하면 전부 붙어서 출력
# print('A b C d'.replace(" ", ''))

# print("안녕! 반가워~?".replace("!", "?"))

# strip(), lstrip(), rstrip(): 보통 앞 뒤의 공백을 제거할 때 사용한다
# 사이의 공백은 완전히 제거 불가. 이럴 때는 replace를 사용하는 게 좋다
# print('a   b   c     '.strip())
# print('a   b   c     '.strip(" "))

# 기본적으로 양 옆의 특정 글자를 제거함
# lstrip(), rstrip()은 각각 맨 왼쪽/오른쪽의 특정 글자를 제거함
# print('apple'.strip('a'))

# index()
# 없는 요소를 찾으려고 하면 오류 발생
# print('ABC'.index("A"))
# print('ABC'.index("Z"))   # 오류

# find()
# 찾으려고 하는 값이 없으면 -1을 반환
# print('ABC'.find("B"))
# print('ABC'.find("Z"))

# in
# 값의 유무를 검사하고, T/F의 불린 값 반환
# print("A" in "ABC")
# print("Z" in "ABC")

# count()
# 문자열 내에 특정 값이 몇 개 있는지 검사
# print("fdsndbosfdsjpfdspnsdkapfjsda".count("f"))

# list에서 나온 문제 다시 풀어보기
# 아래 문자열에서 숫자만 분리
s = '189,000 원'

# 1. for문으로 순회하는 방식
# for i in s:
    # 조건식 내에서 '정수' 형태의 문자열 사용 시, 연산 과정에서 일시적으로 정수형으로 변환
    # 연산 과정에서만 바뀌기 때문에, 조건식에서는 문자열 형태로 넣어줘야 됨
    # if '0' <= i <= '9':
    #     print(i)


# 2. Comprehension 사용 예시
# .join() 함수는 순서가 있는 것이라면 전부 적용 가능함
# i for i in s if "0" <= i <= '9' -> 리스트로 감싸지 않아도, 그 자체로 순서가 있음
# 따라서 리스트를 나타내는 [] 없이 그냥 ()안에만 써도, join()이 알아서 풀어서 써줌
print("". join(i for i in s if "0" <= i <= '9'))