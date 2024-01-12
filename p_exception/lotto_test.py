import random as r

# 당첨 번호 지정
win_num = [r.randint(1, 45) for i in range(7)]

# 로또 추첨 횟수
roll_count = 10

# 각 추첨 별 당첨 횟수를 기록할 리스트 선언
result = []

# [1~45까지의 랜덤 번호 7개] * 추첨 횟수 로 이루어진 리스트 반환 - 리스트 안 리스트
lotto_row = [[r.randint(1, 45) for j in range(7)] for k in range(roll_count)]


# lotto_row의 길이 = 추첨 횟수 만큼 반복
for i in range(len(lotto_row)):
    # 각 추첨 별 맞힌 번호의 개수(초기값 0) - 매 반복마다 초기화
    win_count = 0

    # 각 추첨 별 번호를 하나씩 조회
    for j in lotto_row[i]:
        # 만약 해당 번호가 당첨 번호 중에 있으면
        if j in win_num:
            # 맞힌 번호 개수 +1
            win_count += 1

    # 추첨 한 번의 검사가 끝날 때마다 결과 리스트에 맞힌 개수 추가
    result.append(win_count)

print(f'당첨 번호: {win_num}')
print(f'내 추첨: \n{lotto_row}')
print(f'\n결과: {result}')