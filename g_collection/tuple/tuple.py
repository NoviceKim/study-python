# mutable: 변할 수 있는 - list
# data_list1 = [1, 2, 3, 4]

# data_list1에 있는 내용을 data_list2에 복사
# data_list2 = data_list1

# data_list2의 0번 인덱스 값을 10으로 수정
# data_list2[0] = 10

# [10, 2, 3, 4]
# print(data_list2)

# [10, 2, 3, 4]...?
# 원인은 위의 복사 과정 때문
# data_list1을 data_list2로 복사하는 과정에서 리스트 내 데이터의 주소까지 같이 복사되기 때문에
# 두 리스트의 같은 인덱스에 있는 요소들은, 같은 주소를 가리키게 됨
# 따라서 어느 한 쪽의 데이터를 수정하면, 두 리스트의 데이터가 모두 수정되는 것
# print(data_list1)


# immutable: 변할 수 없는 - tuple
data_tuple1 = (1, 2, 3, 4)

# data_tuple1에 있는 걸 data_tuple2에 복사
data_tuple2 = data_tuple1

# data_tuple2의 0번 인덱스 값을 10으로 수정
# data_tuple2[0] = 10

# 오류 발생
# 'tuple' object does not support item assignment
# 튜플이라는 자료형은 내용 수정이 불가
# print(data_tuple2)

# data_tuple2의 자료형을 list로 변환
test = list(data_tuple2)

# 자료형이 list가 되었기 때문에 내용 수정 가능
test[0] = 10

print(test)

# 단, 기존 튜플 뒤에 데이터를 추가하는 것은 가능함
data_tuple2 = data_tuple1 + (5, 6)

print(data_tuple2)

# 그리고 복사한 튜플의 내용물이 바뀌어도 원본의 내용은 바뀌지 않음
print(data_tuple1)

# 튜플 선언은 소괄호 안 써도 됨
datas = 1, 2

print(type(datas))

print(datas[0])


# 콤마(,)로 끝나도 튜플로 취급. 이 코드 역시 소괄호가 생략된 상태
# 기업 컨벤션에서는 보통 상수를 대문자로 기재함
# 상수는 파이썬에서 따로 지원하지는 않지만, 개발자들이 상수로서 기능하게끔 튜플을 사용한 것
# 보통 바뀌면 안 되는 데이터를 튜플 형태로 선언하며
# 다른 개발자들이 어떤 목적으로 튜플을 썼는지 아는 게 중요하다는 점이 튜플을 배우는 이유다
ERROR_CODE = 1,

print(type(ERROR_CODE))