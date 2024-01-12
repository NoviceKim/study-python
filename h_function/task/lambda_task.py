# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경 - 문자열.lower()
# subjects = ['aPPle', 'BananA', 'meLON']
#
# # 각 요소에 대하여 .lower()로 소문자 변환
# result = list(map(lambda el: el.lower(), subjects))
#
# print(result)

# 입력받은 한글을 정수로 변경 - input으로 데이터 하나만 입력?
# 입력 예: 삼오일구
# 출력 예: 3519

# 람다 함수가 하는 것: 삼 -> 3, 오 -> 5 같이, 특정 글자를 숫자로 바꿔줌
# input으로 입력 - 문자열 하나
# 문자열[0] = 맨 앞글자 -> 문자열에 바로 인덱스 때릴 수 있음 = 일종의 리스트로 취급 -> 자체로도 map이 가능
# print('삼오일구'[0])

# 람다 함수에서의 비교를 위한 문자열(list) 생성
hangul = '공일이삼사오육칠팔구'

# 그럼 문자열을 입력받아봅시다
# target_kor = input('한글 입력하면 숫자로 변환: ')

# res에 저장되는 것 = 숫자(int)
# 1. 입력받은 문자열(target_kor)에 map을 사용, 처음부터 끝까지 순회 -> 문자 하나하나 떼서 람다 함수에서 사용
# 2. 각 문자(el)에 대해 샘플 문자열(hangul)에서 해당 문자가 있는 곳의 위치(인덱스) 검색
# 3. 문자 한글로 만든 거 = 인덱스(예: 공 = 0번 인덱스)이므로, 원하는 문자가 나올 것
# 4. 하나하나 다 돌면 숫자가 여러 개 나오죠?
# 5. 이제 그걸 다 붙여야 되는데, 인덱스 번호는 숫자라서 + 를 쓰면 덧셈으로 연산이 되어버림
# 6. 그래서 문자열(str)로 잠시 바꾸고, 그걸 list 형태로 모아놓음
# 7. 아무것도 없던 문자열('')에 6의 문자 리스트([문자열, 문자열, ...])를 순서대로 붙임
# 8. 그러면 숫자들이 붙어있는 형태(str 타입)가 나올텐데, 그걸 다시 int로 바꾸면 됨
# res = int(''.join(list(map(lambda el: str(hangul.index(el)), target_kor))))

# 위에서 만든 거(숫자) 출력
# print(res)


# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
# 람다 함수 연산을 위한 한글 문자열은 위에 있는 거(hangul) 가져다 씁시다

# 이번에는 숫자를 입력받아봐요
# 정보: input으로 뭐라도 입력받으면... 그 값은 str(문자열) 타입
# 그리고 아래의 map() 함수를 쓰기 위해서는 순회 가능한 데이터를 넘겨줘야 됩니다
# 문자열은 순회 가능 = map() 사용 가능!
# 어차피 그냥 input()만 써도 map 할 수 있는 거, 굳이 int로 바꿀 필요가 있나?
# 그러니까... ex) 1234 입력 -> '1234'(문자열) 되는 데, 그대로 갖다 쓰자
target_num = input('숫자 입력하면 한글로 변환: ')

# 이번에도 한 단계씩 접근해봅시다
# res_kor에 저장되는 거 = 문자열(str)
# 1. 입력받은 숫자(target_num, 현재 str 타입)에 대하여 map()을 가지고 처음부터 끝까지, 한 글자씩 뜯어볼 거에요
# 2. 한 글자씩 살펴보면서, 각각의 글자들에 람다 함수로 연산 실행
# 3. 람다 함수가 하는 거: 글자(1개) 받음 -> int(숫자)로 바꿈 -> 그거랑 같은 인덱스를 한글 문자열(hangul)에서 찾아서 반환
# 4. 그런 식으로 다 돌다 보면, 각 글자에 해당하는 문자들이 하나하나 나오겠죠?
# 5. 그 글자들을 모아 list로 만듭니다
# 6. 빈 문자열("")에 join을 써서 5 안에 있는 문자들(한글)을 순서대로 갖다 붙임
# 7. 결국 얻어야 되는 건 문자열 - 6에서 나온 게 문자열이니 그대로 res_kor 라는 변수에 저장
res_kor = "".join(list(map(lambda el: hangul[int(el)], target_num)))

# 위에서 만든 거(문자열) 출력
print(res_kor)

# 아래의 람다 함수는 숫자(0~9)별 아스키 코드를 활용한 예시
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))


# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
url_list = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']

# 1. 서비스명(user, post, order)으로 변경(map)
# url_list의 각 요소에 대하여 .split('/')으로 /의 앞뒤를 분리(list형)
# 위 과정으로 나온 list의 0번 인덱스만 모아서, 새로운 list 생성(형변환) -> services
services = list(map(lambda url: url.split('/')[0], url_list))

print(services)

# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# 이번에도 각 요소를 split으로 분리하고 시작합시다
# 조건식: split으로 분리하고 나온 [앞, 뒤] 리스트의 '앞'(0번 인덱스) 부분이 'user' 가 아닌가?
# 위 조건식에 맞는 요소만 걸러내서(filter)
# 해당 요소들을, 넣었을 때 형태 그대로 모아놓고 list로 묶음(형변환)
not_user = list(filter(lambda url: url.split('/')[0] != 'user', url_list))

print(not_user)