# import datetime
#
# def log_time(origin_func):
#     print('log_time 들어옴')
#
#     # origin_func 함수 사용할 때 들어온 값이 args에 전달됨
#     def logging(*args):
#         print(args)
#
#         # 현재 시간 출력
#         print(datetime.datetime.now())
#
#         print('logging 함수 종료')
#
#         return origin_func(*args)
#
#     print('log_time 함수 종료')
#
#     return logging
#
# # 위에서 만든 데코레이터(log_time 함수) 사용
# # @'데코레이터 이름'을 붙임 - add 함수가 log_time 함수의 매개변수로 전달됨
# @log_time
# def add(*args):
#     total = 0
#
#     for i in args:
#         total += i
#
#     return total
#
# result = add(1, 2, 3)
#
# # log_time 실행 - logging(클로저) 함수 반환
# # logging에 매개변수로 add 함수에 들어간 값이 들어감 - add 함수 사용
# # logging 함수 실행 - add 함수에다가 add 함수에 전달된 값(1, 2, 3) 넣어서 반환
# # add 함수 실행
# print(result)


# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)

        # 단일 데이터는 len(길이) 없음 = 0
        # 길이가 있다는 건, 원래 함수(set_datas)의 매개변수로 여러 개의 데이터가 들어왔다는 것(args로)
        # 여기서 나온 걸 다시 원래 함수가 받을 수 있게 만들어줘야 되니, 값 여러 개를 반환?
        if count != 0:
            # 우선 합계값 담을 변수 선언
            total = 0

            # 원래 함수에 들어온 각 요소를 전부 더해서 평균
            for i in args:
                total += i

        else:
            total = kwargs.get('total')
            count = kwargs.get('count')

        print(f'평균: {total/count}')

        return original_function(*args, **kwargs)

    return operate

# 실행해보면, @average가 먼저 실행됨
@average
def set_datas(*args, **kwargs):
    total = 0

    for i in args:
        total += i

    # total = 0 이다 - for문을 못 돌아서 초기값(0)이 그대로 들어왔다는 것이고
    # **kwargs 가 받을 수 있는 데이터가 들어온 것이다
    print(f'총 합계: {total if total != 0 else kwargs.get("total")}')


set_datas(1, 2, 3, 4, 5)
# set_datas(total=100, count=5)

