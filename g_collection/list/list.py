# # animals = ['dog', 'cat', 'bird', 'fish']
# # #
# # # # print(animals)
# # #
# # # # list class로 출력
# # # # print(type(animals))
# # #
# # # # 인덱스로 접근
# # # # 인덱스는 시작 주소를 담고 있기 때문에, 0번부터 시작하는 것에 유의
# # # # print(animals[1])
# # # # print(animals[2])
# # #
# # # # 음수 인덱스(가장 마지막에서부터 앞쪽으로 순서대로 이동)
# # # # 이 경우, 자체적으로 if문을 실행, 해당 리스트의 길이(len) - (입력한 음수 인덱스 번호)를 연산하고 반환
# # # # 가장 마지막 인덱스 번호는 -1
# # # # print(animals[-1])
# # # # print(animals[-2])
# # #
# # # # len()
# # # # print(len(animals))
# # #
# # # # append()
# # # animals.append('hamster')
# # #
# # # print(len(animals))
# # # print(animals)
# # #
# # # # list는 값 중복을 신경쓰지 않음
# # # # 따라서 같은 값이 여러 번 들어갈 수 있다
# # # animals.append('cat')
# # # print(animals)
# # #
# # # # insert()
# # # animals.insert(1, 'dog')
# # # print(animals)
# # #
# # # # remove()
# # # # 삭제할 값을 지정
# # # animals.remove('fish')
# # # print(animals)
# # #
# # # # del()
# # # # 중복되는 값이 있을 때, 그 중 원하는 걸 골라서 제거할 수 있음
# # # # del(animals[1])
# # # del animals[1]
# # # print(animals)
# # #
# # # # clear()
# # # # 전체 삭제
# # # # animals.clear()
# # # # print(animals)
# # #
# # # # index()
# # # # 특정 값의 인덱스 번호(위치)를 반환
# # # print(animals.index('bird'))
# # #
# # # # 없는 값을 찾으려고 하면 에러 발생
# # # # print(animals.index('tiger'))
# # #
# # # # 수정
# # # # []안에는 인덱스 번호(숫자)만 들어갈 수 있음
# # # # 아래 코드는 animals.index('bird') -> 'bird'라는 값이 들어 있는 인덱스 번호를 검색하고
# # # # 해당 인덱스에 'lion' 이라는 값을 새로 할당함
# # # index = animals.index('bird')
# # # animals[index] = 'lion'
# # # print(animals)
# # #
# # # # etc
# # # # 곱셈 기호 사용 시, 해당 횟수 만큼 리스트 반복(새로운 리스트 하나)
# # # animals = ['dog', 'cat', 'bird', 'fish']
# # # print(animals * 2)
# # #
# # # # in 절로 특정 요소 검색
# # # # 해당 요소의 유무에 따라 T/F 출력
# # # print('dog' in animals)
# # # print('tiger' in animals)
# # #
# # # # for문을 사용하면 리스트 내 0번 인덱스부터 차례대로 출력(각각 다른 줄에)
# # # for animal in animals:
# # #     print(animal)
#
# # 실습
# # 1. 1~90까지 list에 담고 출력
#
# # list 초기값 생성
# list = []
#
# # 1~90 까지 순차적으로 추가
# # i의 기본 값은 0이기에, i + 1을 추가함
# for i in range (90):
#     list.append(i + 1)
#
# # list 출력
# print(list)
#
#
# # 2. 1~100까지 짝수만 list에 담고 출력
#
# # list 초기값 생성
# list = []
#
# # 1~100까지의 짝수는 50개
# # 따라서 50번만 반복함
# for i in range (50):
#     list.append((i + 1) * 2)
#
# # 아예 처음부터 50칸짜리 리스트를 만들어놓을 거라면 다음과 같이 할 수 있음
# # 처음부터 길이를 정해놨기 때문에 len() 함수 사용 가능
# # list = [0] * 50
#
# # for i in range(len(list)):
# #     list[i] = (i + 1) * 2
#
# # list 출력
# print(list)
#
#
# # 3. 1~10까지 list에 담은 후, 짝수만 출력
# # 기본 리스트와 짝수만 담을 리스트의 초기값 생성
# list = []
# even_list = []
#
#
# # 기본 리스트에 1~10까지 추가
# for i in range(10):
#     list.append(i + 1)
#
# # even_list = [0] * (len(list()) / 2)
#
# # 기존 리스트에서 짝수 요소만 검색, 짝수 리스트에 추가
# # list[인덱스 번호] = 해당 인덱스에 들어있는 값
# for num in list:
#     if num % 2 == 0:
#         even_list.append(num)
#
# # 짝수 리스트 출력
# print(even_list)
#
#
# # 4. 4명의 회원정보를 list에 담고, 2번째 회원 이름 변경하고 마지막 회원 삭제
# # 회원 정보 리스트 생성
# member_list = ['박보검', '수지', '유재석', '신민아']
#
# # 2번째 회원 이름 변경
# update = member_list.index('수지')
# member_list[update] = '한가인'
#
# # 맨 마지막 회원 삭제
# # 맨 마지막 인덱스는 -1로도 쓸 수 있음
# del member_list[-1]
#
# # 최종 회원 리스트 출력
# print(member_list)
#
#
# # 번외
# # 문자열 '189,000 원'을 189000으로 변경
# # 제너레이터를 사용해볼 것
#
# # 원래 데이터와 숫자만 담을 데이터 초기값 생성
# data = '189,000 원'
# refined_data = ''
#
# # 문자열을 순회하면서 숫자 데이터(0 <= i <= 9)만 refined_data 에 추가
# # 단, 데이터 타입은 아직 str(문자열)임에 주의
# for i in data:
#     if '0' <= i <= '9':
#         refined_data += i
#
# # int 형태로 변환해서 재할당
# refined_data = int(refined_data)
#
# # 데이터 출력
# print(refined_data)
# print(type(refined_data))

# list 안의 list
number_list = [[1, 3, 5], [2, 4, 6]]

# 0번 인덱스 안 요소(또 다른 list)의 0번 인덱스
# number_list[0][0]

# number_list의 길이 = 2, number_list의 0번 인덱스의 길이 = 3
# length = len(number_list) * len(number_list[0])

# 변수 하나 = for문 하나로 [0][0] ~ [1][2]까지 출력
# for i in range(length):
    # number_list[i / 3의 몫][i / 3의 나머지]
    # print(number_list[i // 3][i % 3])

# for문 2번 = 변수 2개로 [0][0] ~ [1][2]까지 출력
# 안쪽 for문(j)이 끝나면 바깥쪽 for문(i) 실행
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])