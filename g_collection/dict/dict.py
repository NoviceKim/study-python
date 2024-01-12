# dict 선언
# student = {
#     'name' : '김광협',
#     'email' : 'ghk495892@gmail.com'
# }

# 둘 다 'name' 키에 있는 값('김광협')을 가져옴
# print(student['name'])
# print(student.get('name'))

# 대괄호를 사용해 없는 키를 찾으려고 하면 오류 발생
# print(student['phone'])

# 만약 .get을 사용해서 없는 키를 찾으려고 하면, 오류 대신 None이 출력됨
# print(student.get('phone'))

# 그리고 .get() 함수 내에서 (키, 값) 식으로 기재하면
# 키를 찾지 못했을 때, 같이 적은 값이 default가 됨
# print(student.get('phone', '01086709568'))

# 수정
# 'name' 이라는 키가 이미 있기 때문에, 아래 코드는 기존 값을 수정하는 것이 됨
# student['name'] = 'KGH'

# 추가
# 기존에 'phone'이라는 키가 없었기 때문에, 아래의 코드는 새로운 데이터를 추가하는 것이 됨
# student['phone'] = '01086709568'


# if문에서의 활용 - 기존에 해당 키가 있었는지에 따른 분기
# 만약 student에 'email' 키가 있다면
# if 'email' in student:
    # student['email'] = 'kgh1234@gmail.com'  # 수정
# else:
    # student['email'] = 'kgh1234@gmail.com'  # 없다면 추가

# my_dict = {
#     1 : '김광협',
#     'two' : '25살',
#     False : [10, 20, 30],
#     "row" : [
#         {"name": "ted", "age": 40},
#         {"name": "jack", "age": 30},
#         {"name": "john", "age": 20}
#     ]
# }

# row에 있는 회원 3명의 정보를 모두 출력
# 아래의 정보를 for문으로 반복 돌려서 출력?

# my_dict의 'row' 키 - my_dict['row']
# 'row'의 값은 list 형태 - my_dict['row'][0] ~ my_dict['row'][2]
# 각 인덱스 안 데이터는 dict(key : value 형태) -> 이 중에서 value가 필요함
# my_dict['row'][0]['name'] 형태로 쓰면 value만 가져올 수 있음

# 'row' 키가 있는지 확인
# if 'row' in my_dict:
    # my_dict['row'] -> 'row'의 value인 list = 순회 가능
    # for data in my_dict['row']:
        # 각 인덱스의 'name', 'age' 키에 해당하는 값 출력
        # print(f'{data["name"]}, {data["age"]}')


# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.

# '홀수' : [1, 3, 5, 7, 9]
# '짝수' : [2, 4, 6, 8, 10]
# 위 2개를 중괄호로 묶음(dict)

# 숫자를 그냥 넣어도 되지만, comprehension 배웠으니 응용해보자
# 홀수 - (0~4) * 2 + 1 == 1 ~ 9
# 짝수 - ((0~4) + 1) * 2 == 2 ~ 10
# num_dict = {
#     '홀수' : [i * 2 + 1 for i in range(5)],
#     '짝수' : [(i + 1) * 2 for i in range(5)]
# }

# 사용자에게서 문자열(홀수 or 짝수)을 입력받고 - 입력값을 변수 따로 만들어서 저장
# 입력받은 것과 똑같은 키를 찾기 - .get(변수) -> 이것도 변수 따로 만들어서 저장
# 제어문 사용 x?

# 사용자에게 홀수/짝수 문자열(str)값을 입력받음
# 이 때 입력한 문자열은 아래에서 num_dict 내의 key를 찾는데 사용
# even_or_odd = input("홀수 or 짝수 : ")

# 입력값과 같은 key를 num_dict 내에서 찾고, 해당 key의 value를 result 변수에 저장
# result = num_dict.get(even_or_odd)

# 값(숫자 list) 출력
# print(result)


student = {
    'name' : '김광협',
    'email' : 'ghk495892@gmail.com'
}

# key 분리 - .keys()
# key들을 list로 묶어서 출력
# 묶지 않으면 'dict_keys'라는 자료형으로 묶여서 출력됨
print(list(student.keys()))

# value 분리 - .values()
print(list(student.values()))

# item 분리 - .items()
# key, value가 한 쌍으로 묶여서 출력
# 기본 데이터 타입은 'dict_items'
print(student.items())

# for문에서의 사용 예시
for key, value in student.items():
    print(key, value, sep=', ')