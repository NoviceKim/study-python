# # 인덱스 슬라이싱
# # 반복문 없이도 원하는 부분만 추출
# animals = ['dog', 'dog', 'cat', 'bird', 'fish']
#
# print(animals[0])
#
# # 대괄호 안에서 콜론 (:)을 사용하여 슬라이싱 가능
# # 콜론 왼쪽에 있는 인덱스는 포함 ~ 오른쪽에 있는 인덱스는 포함 안 함
# # 해당 결과 값을 새로운 리스트로 반환
# # 따라서 아래 코드는 0번 ~ 2번 인덱스까지 들어있는 새로운 리스트가 반환됨
# print(animals[0:3])
# print(animals[1:4])
#
# # 만약 0번 인덱스부터 출력하고 싶다면 아래처럼 생략 가능
# print(animals[:2])
#
# # 만약 마지막 인덱스까지 출력하고 싶을 때에도 생략 가능
# print(animals[2:])
#
#
# food = ['noodle', 'meat', 'bread', 'chicken']
#
# # list[inclusive_start = 0 : exclusive_end=len(list) : step=1] -> 새로운 list
# # 처음부터 2번 인덱스까지 2칸 건너뛰어서 출력
# # food[0:3:2]
# print(food[:3:2])
#
# # food[2:last:2]
# print(food[2::2])
#
# # 역순 출력
# # step이 음수면 역순으로 출력된다
# print(food[::-1])

# 리스트 안에 range를 그대로 쓰면, range 그대로 요소에 들어감
# number_list = [range(1, 11)]

# 만약 range를 사용해서 리스트를 생성하고 싶다면, list()로 형변환을 해줘야 됨
# number_list = list(range(1, 11))
# # print(number_list)
#
# # 실습 - 위 number_list를 슬라이싱 해보기
# # 1. [1, 3, 5, 7, 9]
# # 0번 인덱스부터 끝까지 출력, 2칸씩 건너뛰기
# print(number_list[::2])
#
# # 2. [6, 5, 4, 3, 2]
# # 역순으로 출력할 때는 step이 -1
# # 시작 인덱스(5번)에서부터 마지막 인덱스(0번) '직전까지' 거꾸로 감(-1)
# print(number_list[5:0:-1])
#
# # 3. [2, 4, 6]
# # 1번 인덱스(두번째 칸!)부터 6번 인덱스 직전까지 2칸씩 건너뛰어 출력
# print(number_list[1:6:2])
#
# # 4. [2, 3, 4, 5, 6, 7]
# # 1번 인덱스부터 7번 인덱스 직전까지 순서대로 출력
# print(number_list[1:7])

# 슬라이싱을 저장공간으로 사용
# animals = ['dog', 'dog', 'cat', 'bird']
# zoo = ['panda', 'giraffe']
#
# # 1번 인덱스에 zoo 안의 리스트 대입
# # 원래 요소 뒤에 있던 요소들은 한 칸 씩 오른쪽으로 밀림
# animals[1:2] = zoo
# print(animals)
#
# # insert 사용 시, 해당 자리에 요소 삽입
# animals.insert(animals.index('dog') + 1, 'giraffe')
# print(animals)
#
# # 만약 insert로 리스트를 넣으면, 해당 인덱스에는 리스트가 요소로 들어감
# animals.insert(animals.index('dog') + 1, zoo)
# print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']

# 'cat' 제거
del animals[animals.index('cat')]

# -2번 인덱스에 'whale' 삽입
animals[-2:-3:-1] = ['whale']

# 첫번째 'dog' 뒤에 'hamster', 'fish' 삽입
animals.insert(animals.index('dog') + 1, 'fish')
animals.insert(animals.index('dog') + 1, 'hamster')

# 1~2번 인덱스 내용을 아래의 것으로 재할당
animals[1:3] = ['hamster', 'fish', 'dog']

print(animals)

