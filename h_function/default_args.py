# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value로 작성한다
def sub(num1, num2, num3, num4=0):
    return num1 - num2 - num3 - num4


result = sub(1, 2, 3)

print(result)


# 실습
# 이름을 전달받지 못하면 '익명' 으로 대체
# 나이를 전달하지 못하면 0 으로 대체

# 매개변수 선언 시 기본값 설정
# 이 값은 함수 내 로직으로 바뀔 수 있음
# 둘 다 반드시 받을 필요는 없기 때문에, 배치 순서는 상관 없음
def get_info(name='익명', age=0):
    # 리턴 값은 dict 타입
    # 이름: 'name', 나이: 'age'
    return {'이름': name, '나이': age}

print(get_info('김광협', 25))

