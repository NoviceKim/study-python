# for(i = 1; i < 11; i++)과 같은 의미
# for i in range(1, 11, 1):
#     print(f'{i + 1}. KGH')

# step(증가폭)이 1이면 생략 가능
# for i in range(1, 11):
#     print(f'{i}. 김광협')

# step을 음수로도 설정 가능
# for i in range(10, 0, -1):
#     print(f'{i}. kgh')

# inclusive start(시작 지점)가 0일 경우 역시 생략 가능
# for i in range(10):
#     print(f'{i + 1}')

# 시작 지점을 0으로 고정해도 규칙성이 있다면 그대로 사용
# for i in range(10):
#     print(f'{10 - i}')

# 1 ~ 10까지 중 3까지만 출력
# for i in range(10):
#     print(i + 1)
#     if i == 2:
#         break

# 1 ~ 10까지 중 4를 제외하고 출력
# continue를 만나면, 아래 코드를 실행하지 않고 다음 반복으로 넘어감
for i in range(10):
    if i == 3:
        continue
    print(i + 1)

