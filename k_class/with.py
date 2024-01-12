class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('delete')


# with 를 사용해서 객체화부터 자동으로 close 까지 전부 실행
# 실행되는 순서를 보자
with NameCard() as name_card:
    name_card.print_info('KGH')