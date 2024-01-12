# # 클로저 사용을 위한 함수 선언
# def set_key(key):
#     formatting = ''
#
#     # 이 함수가 바로 클로저
#     # set_key 함수를 사용해야 이 함수도 사용가능
#     def set_value(value):
#         # 'formatting' 변수가 set_value에 소속된 지역변수가 아니라는 것을 알려줌
#         nonlocal formatting
#
#         # set_value(여기) 밖에 있는 formatting 변수의 값을 수정
#         formatting = f'{key} : {value}'
#
#         # 위에서 수정한 formatting 변수를 리턴
#         return formatting
#
#     # 위에 있는 set_value 함수 기능을 리턴
#     return set_value
#
# # 우선 set_key 함수를 사용해서 그 값(set_value 함수 기능)을 변수에 할당
# set_name = set_key('이름')
#
# # 현재 set_name은 set_value() 의 기능을 가지고 있기 때문에, 함수처럼 사용할 수 있음
# # 따라서 set_name 뒤의 ()에는 set_value 함수로 전달된 값이 들어있는 것
# formatting_name = set_name('KGH')
#
# # 위 과정으로 얻은 값('이름' : 'KGH') 출력
# print(formatting_name)
#
# # 같은 방법으로 나이도 만들어서 출력
# set_age = set_key('나이')
#
# formatting_age = set_age(27)
#
# print(formatting_age)


# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다. -> 함수1, 2는 각각 변환한 걸 리턴
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

# 함수1, 함수2에 구분점 받는 매개변수 설정하고, 디폴트 값을 ', '로
# 사용할 때는 print(... ,sep=매개변수) 식으로?

# 함수1, 2의 기능을 set_topic 함수 안에 넣음
# set_topic 사용할 때 name=''를 전달 -> 함수1 로
# 'name' 없음 -> 함수2 로
# 위 분기에 따라 set_topic이 리턴하는 값은 함수1/함수2로 달라짐
def set_topic(**kwargs):
    # kwargs(딕셔너리) 데이터를 따로 담아둘까? - 각 함수에서 kwargs 그대로 가져다 쓰면?
    # 딕셔너리 데이터는 함수1, 2에 모두 쓰이는 구분점 정보(함수 쓸 때 sep='' 로 전달 된 거)를 포함!!

    # 만약 'name' 이 들어오면 함수1 생성
    # 함수1의 매개변수: 'sep' 키의 값(구분점) - 기본값 ', '
    # 만든 함수는 set_topic()() 형태로 씀 - 뒤쪽 소괄호에 넣은 값이 매개변수 sep 에 들어감
    if 'name' in kwargs:
        def set_name(sep=', '):
            # kwargs에 있는 'name' 키 값 다이렉트로 가져다 씀
            return f'name{sep}{kwargs.get("name")}'

        # 아래에서 할 일괄처리를 위해 변수에 담아놓음
        result = set_name

    else:
        # 함수2의 매개변수: 마찬가지로 sep
        # 역시 topic, summary 값은 kwargs에서 바로 가져옴
        def set_summary(sep=', '):
            return f'{kwargs.get("topic")}{sep}{kwargs.get("summary")}'

        result = set_summary

    # 각 분기(함수) 별 결과값(result) 반환
    return result


# 함수1에서 처리
print(set_topic(name='KGH')(': '))

# 함수2에서 처리
print(set_topic(topic='제목', summary='내용입니다')('\n'))


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

# set_product 함수 - 상품명: 가격을 dict 타입 데이터로 저장?
# 먼저 함수3을 분리하기 위한 분기 - if args[-1] == 'call'?

# 나머지 함수1, 2는 else로 이동 = 맨 마지막 값이 call은 아님. 'call' 하나만 쓰더라도 if문에 들어가서 함수3 실행
# else문 안에서 한 번 더 if문 분기 - args[0]이 dict 데이터의 키에 있는가? -> if args[0] in (딕셔너리명)
# 있음 - 함수2. 해당 키의 값 수정
# 없음 - 함수1. dict에 새로운 키 추가
def set_product(*args):
    # 자동 증가할 번호를 담을 변수의 초기값 지정
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1

        # 튜플은 튜플과만 연결할 수 있기 때문에, 뒤에 콤마를 붙여 튜플 타입으로 만들어 줌
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},

    def update(**kwargs):
        for prod in args:
            if prod['number'] == kwargs.get('number'):
                prod['name'] == kwargs.get('name')
                prod['price'] = kwargs.get('price')
                break

    def select_all():
        return args

    return {'insert': insert, 'update': update, 'select_all': select_all}

# set_product 함수에 전달할 데이터
# 타입 - list, 각 인덱스 내용물 - dict
products = [
    {'name': '키보드', 'price': 55000},
    {'name': '마우스', 'price': 40000}
]

# set_product 함수에 위에서 만든 list 전달
# set_product 함수의 매개변수 - *args = 풀린 데이터를 받으면, 그걸 set_product 자체에서 tuple로 다시 묶는다
# 근데 set_product에 전달한 product는 list(= 묶음)
# 함수가 풀린 데이터만 받기 때문에, 이거 그대로 넣으면 리스트 하나를 통째로 튜플 한 칸에 넣어버림
# 그래서 함수에 전달하기 직전에 풀어줘야 됨 - 그게 함수 사용할 때 붙이는 *(언패킹)
# 위 과정으로 만든 데이터를 가지고 set_product 함수가 연산한 다음 나온 리턴값(내부 함수)을 prod_service에 할당
prod_service = set_product(*products)

prod_service.get('insert')(name='모니터', price=120000)

print(prod_service.get('select_all')())

prod_service.get('update')(name='본체', price=105000, number=3)

print(prod_service.get('select_all')())
