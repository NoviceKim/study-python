import datetime


# calc.py의 매직 메소드 4개를 인자로 받음
def log_time(original_function):

    def logging(*args, **kwargs):
        self, other = args
        error_code = kwargs.get('error_code')

        with open('log.txt', 'a', encoding='utf-8') as file:
            # 만약 **kwargs 에서 error_code 를 받지 않은 경우(에러가 없는 경우)
            if not error_code:
                # 원래 함수 실행하고, 현재 시간을 알맞은 형식으로 변환해서 변수에 담는다
                result = original_function(*args, **kwargs)
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                # 만약 나눗셈 기호를 입력했다면
                if self.operation == '/':
                    # 몫과 나머지를 따로 담고
                    value, rest = result
                    # 아래 방식으로 로그 내역 작성
                    file.write(f'{self.number} {self.operation} {other} = {value}, {rest}\tKST{now}\n')

                # 나눗셈 이외는 다른 방식으로 로그 내역 작성
                else:
                    file.write(f'{self.number} {self.operation} {other} = {result}\tKST{now}\n')

                # 연산 결과 리턴
                return result

            # 만약 **kwargs에서 error_code를 받은 경우
            else:
                # 아래 형식으로 로그 내역 작성
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                file.write(f'{error_code}\tKST{now}\n')

        # 에러가 없을 때 None을 리턴
        return None

    # 최종적으로 위에서 만든 logging 함수(클로저) 기능을 리턴한다 - 데코레이터 문법
    return logging