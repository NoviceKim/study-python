# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여, 발생 시 안내 메세지까지 출력하기

# NickNameError 라는 에러 클래스 생성하고, str 재정의
class NickNameError(Exception):
    def __str__(self):
        return "닉네임에 비속어나 '운영자' 를 사용하실 수 없습니다"


# 비속어 리스트 생성
bad_nicknames = ['바보', '멍게', '해삼', '운영자']


# 닉네임 체크 함수
def check_nickname(name):
    for i in bad_nicknames:             # 비속어 리스트의 각 인덱스 순회
        if i in name:                   # 만약 입력값에 비속어 리스트 내의 문자열이 있다면
            raise NickNameError         # 강제로 NickNameError 발생


# 닉네임 입력받고
nickname = input('닉네임을 입력해주세요: ')

try:
    check_nickname(nickname)            # 닉네임 검사 함수로 입력한 문자열 검사
    print(f'어서오세요 {nickname}님!')                     # 이상이 없다면 입력한 문자열 그대로 출력

except NickNameError as e:              # 만약 비속어 리스트 내 단어가 있을 경우
    print(e)                            # NickNameError의 에러 메세지 출력
