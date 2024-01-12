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

# 강사님 예시
# 데이터 몇 개 들어올 지 모르니, 매개변수 앞에 * 를 붙여서, 풀어진 형태로 전달된 데이터 packing(튜플)
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: coupon - 할인율, count - 쿠폰 개수
    :return: 할인율이 적용된 금액들
    '''

    # 함수에 전달된 값 중, 'coupon' 이 있는지부터 확인
    if 'coupon' in kwargs:
        # 현재 로직은 조건부에 따라 range() 값이 바뀌는 형식
        # 컴프리헨션 안의 range() 안에서 삼항 연산(if 조건문에 따라 if 앞, else 뒤의 연산 실행)

        # 'count'가 pay 리스트의 길이보다 작거나 같다면(쿠폰이 더 적음) - range는 'count' 수만큼
        # 반대로 더 크다면(리스트가 더 적음), pay 리스트 길이만큼 -> 반환될 리스트의 길이를 의미
        # pay 리스트의 각 인덱스에 들어있는 데이터(정수)에 대하여
        # 할인율이 적용된 금액을 연산해서
        # 그 결과값으로 이루어진 리스트를 반환
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])  # 할인율이 적용된 금액
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    # 'coupon' 값이 전달되지 않았을 경우, None 반환
    return None

result = use_coupon(1000, 2000, 3000, coupon=50, count=1)

# result 값이 있을 때
if result:
    # 리스트 출력
    print(result)
# result 값이 없을 때(None이 반환된 경우 = 함수 사용할 때 'coupon' 을 전달하지 않았을 경우)
else:
    print('쿠폰이 없습니다')