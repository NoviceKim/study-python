# 부모 클래스: 책
# 인자 - 표지 색깔, 출판사, 페이지 수

# 자식 클래스: 만화책, 문제집

# 만화책
# 추가 인자 - 장르
# 메소드 - 챕터 수를 입력받고, 전체 페이지 수에 따른 챕터 하나 당 페이지 수 구하기
# 각 챕터의 페이지 수는 모두 같으며, 결과를 정수형으로 반환

# 문제집
# 추가 인자 - 과목
# 메소드 - 공부한 페이지 수를 입력받고, 남은 페이지 수 구하기
# 단, 남은 페이지 수는 다음에 이 메소드를 또 호출할 경우 이어서 적용됨
# 그리고 만약 끝까지 다 풀었을 경우, 과목 이름 + "~문제집을 다 풀었다!" 메세지 출력

# 책 클래스
class Book:
    def __init__(self, color: str, publisher: str, pages: int):
        self.color = color
        self.publisher = publisher
        self.pages = pages

# 만화책 클래스
class Comic(Book):
    # 생성자 선언
    def __init__(self, color, publisher, pages, genre: str):
        # 부모 클래스에 있었던 인자들은 그대로 받아오고, 새롭게 추가된 장르(genre) 인자는 따로 생성
        super().__init__(color, publisher, pages)
        self.genre = genre

    # 챕터 당 페이지 수 구하는 메소드 - 챕터 수를 추가로 입력받음
    # 원래 문제는 정수형으로 출력하는 것이였으나, 몫을 써도 될 것 같았음
    def pages_per_chapter(self, chapter_count: int):
        return self.pages // chapter_count

# 문제집 클래스
class Workbook(Book):
    # 마찬가지로 부모 클래스에 있는 건 그대로 가져다 쓰고, 추가되는 것만 따로 선언
    def __init__(self, color, publisher, pages, subject: str):
        super().__init__(color, publisher, pages)
        self.subject = subject

        # 그리고 남은 페이지 수를 저장할 변수를 따로 선언(초기값 = 전체 페이지 수)
        self.left_pages = self.pages

        # 만약 남은 페이지 수가 0보다 작아지면 다시 0으로 만듬
        if self.left_pages < 0:
            self.left_pages = 0

    # 현재 남은 페이지 수를 계산하는 메소드
    def calculate_left_pages(self, proceeded_pages: int):
        # 남은 페이지 수에서 공부한 페이지 수만큼 차감
        self.left_pages -= proceeded_pages

        # 만약 남은 페이지 수가 0보다 작아지면, 다시 0으로 만들어줌
        if self.left_pages < 0:
            self.left_pages = 0

        # 만약 남은 페이지 수가 0이 아니라면
        if self.left_pages != 0:
            # 일괄 처리를 위해 변수에 남은 페이지 수 할당
            result = self.left_pages

        # 만약 남은 페이지 수가 0이라면 문자열을 변수에 저장
        else:
            result = f"{self.subject} 문제집을 다 풀었다!"

        # 각 분기별 result 값 반환
        return result


# 책 클래스 테스트
book = Book("white", "한빛아카데미", 500)
print(book.color, book.publisher, book.pages, sep=', ')

# 만화책 클래스 테스트
comic = Comic('red', "마블", 155, '액션')
print(comic.color, comic.publisher, comic.pages, comic.genre, sep=", ")

# 만화책 메소드(챕터 별 페이지 수) 테스트
print(comic.pages_per_chapter(8))

# 문제집 클래스 테스트
workbook = Workbook("blue", "길벗알앤디", 550, "정보처리산업기사")
print(workbook.color, workbook.publisher, workbook.left_pages, workbook.subject, sep=', ')

# 문제집 메소드 테스트
print(workbook.calculate_left_pages(150))

# 메소드 실행 이후, 남은 페이지 수가 잘 저장되었는지 테스트
print(workbook.color, workbook.publisher, workbook.left_pages, workbook.subject, sep=', ')

print(workbook.calculate_left_pages(300))

# 문제집을 다 풀었을 때, 문자열이 잘 출력되는지 테스트
print(workbook.calculate_left_pages(150))

# 메소드 실행 이후 남은 페이지 수가 0이 되었는지 테스트
print(workbook.color, workbook.publisher, workbook.left_pages, workbook.subject, sep=', ')