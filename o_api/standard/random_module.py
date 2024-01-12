import random as r

# randint(시작, 끝)
# 1 ~ 10까지의 수들 중 하나가 랜덤으로 출력
# 기존에 쓰던 range()나 슬라이싱과는 다르게 마지막도 범위에 포함
# print(r.randint(1, 10))

# 확률
# 1. list 필요 - 몇 칸인지에 따라 확률의 단위가 달라짐
unit = 10   # 단위

# 1 -> 100, 10 -> 10
# 딕셔너리 활용
unit_dict = {1: 100, 10: 10}
rating = [0] * unit_dict[unit]  # 10을 넣었으니, [0] 10칸 반환
rate = 30   # 확률

# 2. 확률을 계산해서 해당 자리에 1 대입
# 확률 / 10의 몫 만큼 rating(list)의 내용물을 1로 바꿈
for i in range(rate // 10):
    rating[i] = 1

# 3. 10개 중 3개가 1 -> 1이 나올 확률은 30%
if rating[r.randint(0, len(rating) - 1)] == 1:
    print('당첨')
else:
    print('실패')