# 실제 로또 규칙

# 1~45 까지의 번호 중 무작위 6개로 이루어진 리스트가 추첨 한 번
# 한 번의 추첨 내에서는 중복되는 숫자가 없으며, 번호는 오름차순으로 정렬됨

# 당첨 번호 역시 1~45 까지의 중복 없는 무작위 숫자 7개
# 당첨 번호는 오름차순 정렬을 따로 하지 않음
# 그리고 당첨 번호의 마지막(7번째)은 보너스 숫자로 취급

# 내 추첨 한 번과 당첨 번호를 비교해서 몇 개 맞혔는지를 계산하고
# 각 추첨 별 맞힌 개수를 리스트에 담아서 출력
# 그리고 그 결과에 따라 아래 조건 중 가장 높은 등수가 출력
'''
    1등: 6개 번호 전부 일치
    2등: 보너스 번호 일치 + 나머지 번호 중 5개 일치
    3등: 보너스 번호 제외한 나머지 번호 중 5개 일치
    4등: 보너스 번호 제외한 나머지 번호 중 4개 일치
    5등: 보너스 번호 제외한 나머지 번호 중 3개 일치

    나머지는 낙첨
'''

# 위 규칙대로 만든 여러 번의 추첨(리스트)으로 이루어진 최종 추첨 리스트... 를 만들어주는 함수를 만들 것
# 단, 추첨 횟수는 사용자 입력에 따라 설정
# 그리고 예외 상황 발생 시(숫자 말고 다른 걸 입력한다던가...), exception으로 처리

# 출력은 당첨 번호 리스트 먼저 보여주고,
# 내가 추첨한 번호 리스트를 그 다음에 보여줌 - 각 리스트가 끝날때마다 줄바꿈
# 그 밑에 맞힌 개수로 이루어진 리스트를 출력하고
# 마지막에 가장 높은 등수를 출력

# 목표: 함수 구현
# 나중에는 클래스랑 모듈화도...?
# + 오늘(1/12) git 배웠으니 수정 사항 생길 때마다 Github에 올리기

# 무작위 추첨 기능을 만들기 위한 random 라이브러리 import
import random


# 로또 추첨 함수
def lotto_draw(num: int):
    # 각 추첨 별 당첨 횟수를 기록하기 위한 리스트 생성
    result = []
    
    # 당첨 번호 생성 - 일단 빈 문자열로 만들고 내용물(숫자)은 아래의 while문으로 생성
    win_num = []

    # 당첨 번호 + 보너스 번호 리스트 생성
    # 숫자는 7개지만, 중복되는 경우의 수 때문에 반복 횟수 예상 불가 - while문
    while len(win_num) < 7:
        # 1~45 사이의 무작위 숫자를 ran_num 변수에 할당
        ran_num = random.randint(1, 45)

        # 만약 그 숫자가 기존 당첨 번호 리스트에 없는 경우
        if ran_num not in win_num:
            # 당첨 번호 리스트에 추가
            win_num.append(ran_num)

    # while문 끝나면 당첨 번호 + 보너스 번호 출력
    print(f'당첨 번호: {win_num[0:6]}    보너스 번호: {win_num[6]}')

    # 내 추첨번호 생성 - 1~45 까지의 숫자 중, 중복 없는 6개로 이루어진 리스트 num개
    # 내 추첨 리스트(my_draw) 안에 비어있는 리스트 num(입력값)개 생성
    my_draw = [[] for i in range(num)]

    # 우선 추첨 1번에 대한 리스트 순회
    for j in range(num):

        # 랜덤 번호 생성 + 중복 검사는 당첨 번호 때와 같음
        while len(my_draw[j]) < 6:
            ran_my_num = random.randint(1, 45)

            if ran_my_num not in my_draw[j]:
                my_draw[j].append(ran_my_num)

        # 만들어진 추첨 번호 리스트를 오름차순 정렬
        my_draw[j].sort()

    # 완성된 전체 추첨 리스트를 각 줄에 순서대로 출력
    print('내 추첨 번호')

    for el in range(len(my_draw)):
        print(my_draw[el])

    # 남은 것들
    # 당첨 번호와 내 추첨 비교해서, 당첨 개수 + 보너스 일치 여부를 dict 형태로 출력
    # {'맞힌 개수': n, '보너스': '일치/불일치'}
    # 전체 추첨 리스트 - 각 추첨 순회
    for i in range(len(my_draw)):
        # 맞힌 개수와 보너스 일치 여부의 초기값을 0으로 지정 - 추첨 한 번 검사할 때마다 초기화
        correct = 0
        bonus = 0

        # 추첨 리스트 하나에 대하여 처음 ~ 끝까지 순회
        for j in range(len(my_draw[i])):
            # 만약 당첨 번호(win_num[0:6]) 안에 있는 숫자가 내 추첨에도 있다면
            if my_draw[i][j] in win_num[0:6]:
                # 맞힌 개수 +1
                correct += 1

            # 만약 보너스 번호가 있다면, 보너스 여부 +1(True)
            if my_draw[i][j] == win_num[6]:
                bonus += 1

        # 여기까지 진행했으면, 추첨 하나에 대한 결과가 나왔을 것
        # 각 추첨 분석 끝날 때마다 리스트(result)에 dict 형태로 추첨 결과 추가
        result.append({'맞힌 개수': correct, '보너스': '일치' if bonus == 1 else '불일치'})

    # 각 추첨에 대한 결과 출력
    print('\n추첨 결과')

    for i in range(len(result)):
        print(result[i])

    # 1/15 이슈 - 보너스 숫자가 맞힌 개수에도 포함되는 현상 발견
    # 보너스 숫자 일치 여부를 먼저 판단하고, 나머지 숫자들로만 맞힌 개수 판별할 방법을 찾아야 할 듯

    # 위 결과에 따라 가장 높은 등수 출력
    # 이건 6(개수) in '딕셔너리 키값' 식으로 가장 높은 거 찾아서 출력하면 될 듯



# 함수 사용 - print는 함수 안에서 해주니, 여기서는 따로 쓸 필요 없음
lotto_draw(7)
