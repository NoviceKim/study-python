# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수
#
# coupon=40
# count=5
#
# 아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
# 40%쿠폰 5개
#
# 아래와 같은 상황은 없다.
# 10%쿠폰 1개, 20%쿠폰 2개

# 입력 예시1
# [2000, 4000, 5000]    -> 변수 따로 만들어서 저장
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]  -> 할인 로직이 적용된 인덱스만 출력?

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]


# 주문 금액(pay)
# 서로 다른 정수값(int)가 여러 개 들어있는 list?
# pay = []

# 함수 밖에서 위 방식대로 list 만들고, 함수에 전달할 때는 함수명(*pay) 형태로 전달?
# 함수에 전달될 변수(pay) 앞에 * 를 붙이면...
# 함수 로직에 전달하기 전, 안에 들어있는 내용물을 풀어놓는다 - unpacking

# 함수에서 위의 풀어진 내용물들을 받을 매개변수를 *args 라는 이름으로 지정
# 함수의 매개변수를 지정할 때, 매개변수 앞에 * 가 오면...
# 풀어진 데이터들(= 인자 여러 개)을 tuple 형태로 묶은 다음, args 변수에 할당 - packing
# 즉, 이렇게 만들어진 함수 내에서 사용하는 변수 args의 데이터 타입은 tuple


# 쿠폰 할인율과 개수(coupon, count)
# 함수에 전달할 때는 함수명(... , coupon=40, count=5) 의 형태로 전달하는 게 조건

# 함수에서 매개변수 **kwargs 를 지정
# 이 kwargs 앞에 **가 붙은 것은...
# 함수를 사용할 때 넣어준 coupon, count(키)와 각각의 값을 dict 데이터 타입(자료형)으로 저장
# 따라서 kwargs의 자료형은 dict
# print(kwargs)로 확인해보면, {'coupon': 40, 'count': 5} 가 kwargs 변수에 저장되어 있음


# kwargs 변수에 저장된 값들 - kwargs['coupon'], kwargs['count'] -> 40, 5
# 위의 값들을 사용해서 args 변수(list)의 각 인덱스에 저장된 데이터들을 수정
# 데이터 수정은 0번 인덱스 - args[0] 부터 반복해서 실행 -> for문 사용?
# 수정할 데이터의 개수 = count
# conprehension 사용 -> if문의 조건으로 i < count 를 쓰면?


# 일단 함수 이름을 지정하고, 매개 변수를 전달
def discount_total(*args, **kwargs):
    '''
    :param args: 함수 사용 시 받아온 pay를 한 번 분해하고, tuple 타입으로 재조립해서 할당
    :param kwargs: 함수 사용 시, coupon, count 값을 'coupon=30' 같은 형태로 입력받고,
                    dict 타입으로 만들어서 할당

    :return: args(튜플)에 kwargs(딕셔너리) 안 키의 값들을 사용해서,
              args의 각 인덱스에 연산을 실행하고 나온 list 타입의 값
    '''

    # 현재 args는 튜플이니, 아래의 로직에서 쓰기 편하게 리스트로 변환해서 새 변수에 할당
    # 원본 데이터(args)는 튜플이기 때문에, 다른 변수에 내용을 복사하더라도 원본은 변하지 않음
    price_list = list(args)

    # kwargs에 저장된 딕셔너리 데이터의 각 키에서 값을 추출해서 각각 다른 변수에 할당
    # 딕셔너리 타입이기 때문에 .values()로 값만 가져올 수 있음 - dict.values 타입
    # 리스트로 형변환 -> 각각 int 타입으로 변수에 저장
    rate, amount = list(kwargs.values())

    # 분기에 따른 결과값을 담을 새로운 리스트 선언
    result_list = []

    # 할인율 변수(rate)을 아래에서 쓰기 쉽도록 바꿔봅시다
    # ex) 할인율 30%(rate = 30) = 할인 이후 가격은 기존 가격의 70%(1 - (할인율 * 0.01))
    # 이렇게 나온 값(new_rate)을 가격에 곱해주면, 할인 이후의 가격이 나온다
    new_rate = 1 - rate * 0.01

    # 조건 2가지 -> 주문 개수 > 쿠폰 개수 | 주문 개수 <= 쿠폰 개수
    # if문으로 분기 처리
    # 주문 개수 > 쿠폰 개수 인 경우
    if len(price_list) > amount:
        # 앞쪽부터 amount(쿠폰 개수)개 만큼의 인덱스에만 할인 로직 실행
        # amount만큼만 반복 - i
        result_list = [int(price_list[i] * new_rate) for i in range(amount) if i < amount]

    # 주문 개수 <= 쿠폰 개수 인 경우
    else:
        # 가격 데이터의 길이(len(price_list))개 = 가격 데이터 리스트 전체에 할인 로직 실행(그래서 if 필요 없음)
        result_list = [int(price_list[i] * new_rate) for i in range(len(price_list))]

    # 각 분기에서 실행한 결과에 따른 값(리스트) 반환
    return result_list

# 함수에 전달할 주문 금액 데이터들을 list로 묶어서 변수화
pay = [5000, 6000, 3500, 2000, 8000]

# 함수 사용
# 위에서 만든 pay 변수 앞에 *(unpacking)를 붙여서 함수의 매개변수 *args에 전달
# coupon, count 값 넣어서 함수의 매개변수 **kwargs에 전달
# 함수 실행으로 나온 결과값(list)을 result 변수에 할당
result = discount_total(*pay, coupon=40, count=7)

# 출력
print(result)
