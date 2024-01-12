# # keyword arguments - **
# # 함수의 매개변수에 **이 있다면
# # a = b 같은 형태로 전달해줘야 됨.
# # 이 데이터를 함수에서 풀면, 함수 내부에서는 풀린 데이터를 dict 형태로 취급함
# def introduce(**intro):
#     print(type(intro))
#
#     # 가지고 온 데이터는 함수 내부에서 dict 형태로 취급
#     # 따라서 해당 데이터는 함수 안에서 dict 데이터처럼 활용 가능
#     print(f'name: {intro["name"]}')
#
#
# introduce(name='KGH')
#
# # 아래 코드 검증을 위한 dict 데이터 생성
# info_dict = {
#     'name': 'KGH'
# }
#
# introduce(**info_dict)


# 주문 가격과 주문한 회원의 정보을 출력하는 함수
# def order_info(*prices, **user_info):
#     total = 0
#
#     # 총 주문 가격
#     for i in prices:
#         total += i
#
#     #
#     print(f'{user_info["name"]}님의 총 주문 가격은 {total}원 입니다.')
#
#
# # 앞에는 *prices로 받을 가격 데이터들을 선언하고
# # 마지막에는 **user_info로 받을 데이터를 name='' 형태로 선언해서
# # 해당 데이터들을 함수의 매개변수로서 전달한다
# order_info(35000, 12000, 3000, name='김광협')


# 국어, 영어, 수학 점수의 평균 구하기
# kwargs를 사용

# 데이터 전달 형식
# 함수명(국어="", 수학="", 영어="")

# def average_score(**score_info):
#     kor = score_info["kor"]
#     math = score_info["math"]
#     eng = score_info["eng"]
#
#     return (kor + math + eng) / 3

# 함수에 전달하기 위한 dict 데이터 생성
# score_dict = {
#     'kor': 90,
#     'math': 80,
#     'eng': 70
# }

# 함수에 dict 타입 데이터를 그대로 전달할 때는 앞에 **을 붙임
# 안 하면, packing 때 list 데이터를 * 안 붙이고 그대로 전달했을 때와 같은 오류 발생
# print(average_score(**score_dict))


# 위 예제에 추가로, 사용자에게서 자리 수도 전달받음
# 이 때 전달받은 자리 수(round_data)에서 반올림
# 자리 수를 받지 않았다면, 기본값을 리턴한다.


def average_score_round(**score_info):
    print(score_info)
    # 각 변수에 dict 데이터의 키에 해당하는 값 저장
    kor = score_info["kor"]
    math = score_info["math"]
    eng = score_info["eng"]
    
    # 3과목의 평균을 변수화
    avg = (kor + math + eng) / 3

    # dict에서 특정 key(= round_data)가 있는지 검사
    if 'round_data' in score_info:
        # 있다면 해당 자리수(score_info['round_data'])에서 반올림)
        return round(avg, score_info['round_data'])
    
    # 'round_data'가 없다면 아래 코드 실행(기본값 반환)
    return avg

# 함수에서 쓸 dict 타입 데이터 선언
score_dict = {
    'kor': 92,
    'math': 79,
    'eng': 83,
    'round_data': 2
}

print(average_score_round(kor=90, math=80, eng=100))

# key를 반드시 함께 사용해야 할 때는
# 함수를 선언할 때 매개변수의 맨 앞에 *을 전달해준다
# def average(*, kor, eng, math):
#     return (kor + eng + math) / 3
#
#
# print(average(kor=100, eng=30, math=22))
