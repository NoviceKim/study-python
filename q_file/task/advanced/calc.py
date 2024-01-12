# 사용하는 메인 모듈을 기준으로 경로를 작성해야 한다.
from q_file.task.advanced.log import log_time


class Calculator:
    def __init__(self, num):
        # self.operation 변수 초기화 - 원하는 연산 기호를 담기위한 준비
        self.operation = None

        # 연산에 쓸 첫번째 변수
        self.num = num

    # 입력받은 기호에 따라 서로 다른 연산 실행하게 하기
    def calc(self, other, operation, error_code=""):
        '''

        :param other: 연산할 두 번째 정수
        :param operation: 연산에 쓸 연산 기호
        :param error_code: 오류 발생 시에 출력할 문자열
        :return: 결과값(연산결과 또는 None)
        '''

        # 전달받은 연산 기호마다 알맞은 번호를 설정
        operation_num = {'+': 0, '-': 1, '*': 2, '/': 3}

        # 전달받은 연산 기호를 self.operation 에 담아줌
        self.operation = operation

        # 실행 가능한 함수들을 list에 저장
        operations = [self.__add__, self.__sub__, self.__mul__, self.__floordiv__, self.write_error]

        # error_code 가 없을 경우, 전달받은 연산자에 따른 함수 실행
        # error_code 가 있을 경우, error_code에 맞는 함수 실행
        return operations[operation_num[operation] if not error_code else 4](other, error_code=error_code)

    @log_time
    # self, other는 *args에 전달
    # error_code는 **kwargs에 전달
    def __add__(self, other, **kwargs):
        return self.num + other

    @log_time
    def __sub__(self, other, **kwargs):
        return self.num - other

    @log_time
    def __mul__(self, other, **kwargs):
        return self.num * other

    # 나누기는 몫, 나머지 모두 리턴(튜플형) -> log_time의 *args에서 받기 위함
    @log_time
    def __floordiv__(self, other, **kwargs):
        return self.num // other, self.num % other

    # error_code 가 있을 때, log에 에러를 기록할 수 있게 도와주는 메소드
    # 즉, log_time을 실행하기 위해 제작된 함수
    @log_time
    def write_error(self, other, **kwargs):
        pass
