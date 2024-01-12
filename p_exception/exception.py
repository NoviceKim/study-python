# try:
#     number = int(input('정수를 입력하세요: '))      # 여기에 숫자 이외의 것들을 입력하면 ValueError 발생
#
# # try 문에서 ValueError 발생 시, 해당 에러(클래스)의 주소가 변수 e에 담긴다
# # 주소를 저장할 수 있는 공간(메모리)이 생겼기 때문에, 요류가 발생하더라도 강제종료 되지 않는다
# # 단, 이 케이스는 ValueError 이외의 에러를 잡을 수 없다
# except ValueError as e:
#     print('정수만 입력해주시기 바랍니다.')
#
# print('이 문장은 반드시 실행됩니다.')

# try:
#     print(10 / 0)   # 수학적으로 불가능한 0으로 나누기 실행(ZeroDivisionError)
#
# # 에러를 객체에 담고 출력하면, 해당 에러의 메세지를 문자열로 출력할 수 있다
# # 따라서, 모든 에러(클래스)는 __str__을 재정의 했다는 것을 알 수 있다
# except ZeroDivisionError as e:
#     print(e)
#
# # Exception 클래스는 모든 에러의 부모 클래스 - 생략 가능
# # 보통 가장 아래에 쓴다
# except Exception:
#     print("Something went wrong")

# datas = [1, 2, 3]
#
# try:
#     print(datas[2])    # 위 list에 3번 인덱스가 없기 때문에 IndexError 발생
#     print('오류 없음!')     # 위 문장에 오류가 없다면 당연히 실행되지만, 오류가 뜨면 실행되지 않는다
#
# # 위 에러는 ValueError가 아니기 때문에 여기서 잡아낼 수 없음
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스 제대로 확인하셨나요?')
#
# # 오류 발생 여부와 상관없이 실행
# finally:
#     print('이 문장은 반드시 실행됩니다.')

# nickname = input('닉네임을 입력해주세요: ')
#
# # 만약 '모지리' 입력 시, 런타임 에러를 강제로 발생시킴
# if nickname == '모지리':
#     raise RuntimeError

# Exception을 상속받는 순간, 해당 클래스는 에러 클래스가 된다
class BadWordError(Exception):
    def __str__(self):
        return "Bad Word Detected"

def check_bad_word(message):
    if '모지리' in message:
        raise BadWordError

chat = input('채팅: ')

try:
    check_bad_word(chat)    # '모지리' 가 있는지 검사 - 있다면 에러 발생
    print(chat)     # 없다면 입력한 거 그대로 출력

except BadWordError as e:   # 만약 BadWordError 발생 시, 에러 메세지 출력
    print(e)