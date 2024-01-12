# lambda - 익명 함수
# lambda 매개변수, ... : 리턴값
# '익명' 함수기 때문에, 이름이 따로 없다
# 이름이 없기 때문에, 따로 호출할 수 없음
# 1회용으로 쓰고 싶은 함수는 이렇게

# 두 정수의 덧셈
# 일반 함수
# def add(num1, num2):
#     return num1 + num2
#
# # 람다 식으로 구현
# lambda num1, num2 : num1 + num2

# 리스트를 처리할 별도의 함수(일회용)를 람다 식으로 map()의 첫번째 인자에 넣어줌
# 어차피 한 번 쓰고 말건데, 굳이 선언할 필요가 있을까?
# print(list(map(lambda num : num + 2, [1, 2, 3, 4])))

# 실습
# 아래 list의 각 요소에 2를 곱해서 변경 - map()
# datas = [2, 4, 6, 8]
# multis = [1, 3, 5, 7]

# 1. map 함수의 첫번째 인자(두번째 인자를 어떻게 처리할 것인가)에 람다 함수를 넘겨줌
# 2. 1의 람다 함수는, 두번째 인자로 들어온 리스트 요소들을 0번 인덱스부터 매개변수 num에 넣어보면서, 각 값에 2를 곱함(num: num * 2)
# 3. 2에서 반환된 값을 list로 형변환하고, 그걸 print로 출력
# print(list(map(lambda num: num * 2, datas)))

# datas[0] * times[0], datas[1] * times[1], ...
# print(list(map(lambda num, times: num * times, datas, multis)))


# 각 경로 앞에 '/app'를 붙여준다.
# '/app/game', '/app/news', '/app/fashion', '/app/ranking'
urls = ['/game', '/news', '/fashion', '/ranking']

# 문자열 + 문자열을 하면 두 개가 붙어서 나온다 - '/app' + url
# formatting 써도 됨
new_urls = list(map(lambda url: f'/app{url}', urls))

print(new_urls)


# filter(함수, 순서 있는 데이터 값들)
# 문제: 1~10까지 중 짝수만 출력
filtered_list = list(filter(lambda num: num % 2 == 0 and num != 0, [i for i in range(10)]))

print(filtered_list)


# ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
# 'game' 서비스를 제공하는 경로 찾기 - filter
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']

target_route = list(filter(lambda url: url.split('/')[-1] == 'game', urls))

print(target_route)