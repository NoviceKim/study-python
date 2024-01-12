# # 아래에서 쓸 데이터 리스트
#
# # user_info는 list 타입 -> 리스트 메서드 사용
# # 각 인덱스에 dict 데이터 들어있음 -> 리스트 메서드로 불러오고, 딕셔너리 메서드로 작업
# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
# # function_intermediate 파일에서 가져온 함수들을 set_user 함수 하나로 묶음
# def set_user():
#     # 추가
#     # 회원 번호는 자동 증가한다.
#     # 전역 변수로 기본값 생성
#     number = 5
#
#     # name(추가할 회원 이름)만 전달받으면 됨
#     # 번호는 전역변수 가져다 알아서 붙여줌
#     def insert(name):
#         # 전역변수 가져와서
#         global number
#
#         # 값 + 1 -> 해당 전역변수를 직접 수정
#         number += 1
#
#         # 리스트의 맨 뒤에 {'number': 전역변수(새 값), name: '입력한 이름'}를 저장(인덱스에 딕셔너리 데이터 들어감)
#         user_info.append({'number': number, 'name': name})
#
#     # 목록
#     def select_all():
#         # 현재 리스트 반환
#         return user_info
#
#     # 조회(번호로 조회)
#     # 조회하고 싶은 번호만 전달받음
#     def select(number):
#         # user_info 리스트를 [0]~끝까지 돌면서, 들어있는 값(딕셔너리 데이터)를 한 번씩 user에 넣어봄
#         for user in user_info:
#             # 만약 user가 현재 가지고 있는 데이터에서, 'number'의 값이 전달 값이랑 같으면
#             if user['number'] == number:
#                 # 현재 전달된 데이터(딕셔너리) 그대로 반환
#                 return user
#
#         # 만약 찾는 번호가 없다면 이 부분 실행
#         # 빈 딕셔너리 반환
#         return {}
#
#     # 수정(번호로 이름 수정)
#     # 함수 사용할 때, number=n, name='' 형태로 전달받음 -> 딕셔너리 타입으로 묶어서 kwargs에 할당
#     def update(**kwargs):
#         '''
#
#         :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#         '''
#         # 1. 전달된 데이터(함수에 전달된 걸 쓸 때 딕셔너리로 묶임)에서 'name' 키 안의 값(문자열)을 가져옴
#         # 2. 전달된 딕셔너리 데이터의 'number'에 해당하는 값(정수)를 가져옴
#         # 3. select() 함수를 사용해서 2번의 값을 가진 인덱스를 검색
#         # 4. 3번에서 찾은 인덱스 안 내용물(dict)의 'name' 키 의 값에
#         # 5. 1번에서 가져온 문자열(함수에 전달된, 새로 설정할 이름)을 재할당함
#         select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#     # 삭제(번호로 삭제)
#     # 삭제하고 싶은 번호를 전달받음
#     def delete(number):
#         # 1. 전달받은 번호값을 가진 인덱스를 user_info에서 찾음 -> 해당 인덱스(정수) 반환
#         # 2. user_info 내, 1번에서 얻은 인덱스 번호 안의 내용을 삭제함
#         del user_info[user_info.index(select(number))]
#
#     # set_user 함수의 리턴값 - dict 타입 데이터 = 내부 함수들(CRUD)
#     # 키: 함수 사용할 때 set_user.get()의 소괄호 안에 'insert' 같이 넣으면 나오는 아래의 값을 의미
#     # 값: set_user.get('') = ''에 대응하는 set_user 함수 안 함수들(CRUD)
#     return {'insert': insert, 'select': select, 'update': update, 'delete': delete}
#
# # 함수의 리턴(dict)에서 'insert'라는 키의 값을 가져옴 = insert() 함수 기능
# set_user().get('insert')
#
# # set_user().get('insert') == insert() 이므로
# # insert 함수의 매개변수, name에 넣을 값을 아래처럼 적는다
# set_user().get('insert')('KGH')


# 게시글 정보
# {번호: n, 제목: '', 내용: '', 첨부파일: '', 조회수: ''} 순서
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]


# 마찬가지로 각 기능(함수)을 post_service 라는 하나의 함수로 묶는다
def post_service():
    # 추가(조회수는 전달받지 않고 기본값 0으로 설정)

    # 함수 선언
    # 여러 개의 값을, title='' 같은 형태로 전달해서 함수 내에서 dict 처럼 쓸 것이므로, kwargs 사용
    def add(**kwargs):
        # 현재 가장 끝 인덱스의 'number'를 가져와서, +1 한 값을 변수에 할당
        new_article_num = post_info[len(post_info) - 1]['number'] + 1

        # 기존 리스트(post_info)를 가져옴 - 안에 있는 '내용'을 수정하는 거라서 global, nonlocal 쓸 필요 없음
        # 가져온 리스트의 맨 뒤에 새로운 내용 붙임(.append) - 새로운 인덱스에 dict 데이터 한 개를 넣음
        # 현재 kwargs(딕셔너리)가 함수 내에서 쓰이므로, 그 안의 키(제목, 내용, 파일)의 값들을
        # kwargs.get()으로 불러와서 사용 가능
        post_info.append({'number': new_article_num,
                          'title': kwargs.get('title'),
                          'content': kwargs.get('content'),
                          'file': kwargs.get('file'),
                          'read_count': 0}
                         )


    # 목록(최신순으로 조회) - 슬라이싱을 이용해서 역순으로
    # 끝번 인덱스 = 리스트 길이 -1
    # 매개변수 필요 없음
    def select_all():
        # 현재 post_info 리스트의 끝번 인덱스(길이 - 1) ~ -1번 인덱스 직전(0번 인덱스)까지의 순서로 반환
        # 끝번 인덱스(len(post_info) - 1):(공란):-1(역순) -> 끝부터 처음까지 역순으로 출력
        return post_info[len(post_info) - 1::-1]


    # 검색
    # 조회, 수정, 삭제 함수에서 사용
    def select(number):
        # post_info를 끝까지 돌면서, 각 인덱스 안 내용물(dict)을 post 변수에 돌아가면서 할당
        for post in post_info:
            # 만약 내용물의 'number' 키와 전달된 값이 같다면
            if post['number'] == number:
                # 해당 데이터(dict) 출력
                return post

        # for문이 끝날 때까지 찾지 못하면 빈 딕셔너리 반환
        return {}

    # 조회(번호로 조회, 조회수 1 증가)
    # 번호를 받아서 해당 번호를 찾음
    def read(number):
        # 검색 함수(select(number)) 로직 가져와서 번호 넣고 변수에 할당(dict 타입)
        post = select(number)

        # 해당 데이터의 'read_count'에 +1 하고 재할당
        post['read_count'] += 1

        # 조회수 +1 된 해당 항목 반환
        return post


    # 수정(번호로 정보 수정)
    def update(**kwargs):
        # 함수 사용할 때 입력한 'number' 값에 맞는 데이터(post, dict 타입) 가져와서 변수에 할당
        post = select(kwargs.get('number'))

        # post의 각 키에 입력한 데이터 할당(기존 데이터 수정)
        post['title'] = kwargs.get('title')
        post['content'] = kwargs.get('content')
        post['file'] = kwargs.get('file')

        # 수정된 데이터 반환
        return post


    # 삭제(번호로 삭제)
    # 원본 데이터(post_info)의 내용(특정 인덱스)을 다이렉트로 건드리고 삭제하는 거라 리턴 필요 없음
    def delete(number):
        # 검색으로 dict 데이터 가져오고
        # 해당 데이터를 가진 인덱스 번호를 가져옴
        # 그 번호 안에 있는 내용 삭제
        del post_info[post_info.index(select(number))]

    # 이번에도 dict 타입으로 리턴
    return {'add': add,
            'select_all': select_all,
            'select': select,
            'read': read,
            'update': update,
            'delete': delete}

# post_service() 함수의 리턴값(dict)을 post_request 변수에 할당
# 따라서 post_request.get() 을 쓰면, 내부 함수에 접근 가능
post_request = post_service()

# 일단은 select_all 잘 되는지 테스트 - 리스트 역순으로 출력
# select_all 함수는 매개변수를 따로 받지 않으니, 소괄호 하나만 붙여준다
# 함수에서 값을 가져만 오는거라 print는 따로
print(post_request.get('select_all')())

# add(추가) 테스트
# add() 는 **kwargs를 매개변수로 설정함 - 뒤쪽 소괄호에 title='' 같이 전달해줘야 됨
# 사용자가 추가해야 되는 것: title, content, file
# 나머지는 add() 함수 내부에서 알아서 넣어줌
post_request.get('add')(title='add 테스트', content='추가 성공', file='file/add/success')

# 위 add가 잘 됐는지 출력해보자
print(post_request.get('select_all')())

# 다음은 select(검색)
# 이 다음에 나올 기능들의 일부로 들어가지만, 그 기능들이랑 따로 쓰는 것도 가능
# 넣어야 되는 것: 찾고 싶은 데이터(dict)의 'number' 키의 값 - add로 넣었던 6번 데이터 호출
# 성공했다면 number = 6인 dict가 반환될 것임
# 역시 print는 따로
print(post_request.get('select')(6))

# read(조회)
# select 함수 기능 + 조회수('read_count' 키의 값) 1 증가
print(post_request.get('read')(6))

# update(수정)
# 넣어야 되는 것: number, title, content, file
# 잘 되었는지 확인해보기 위해 read 기능을 print해서 사용(조회수도 +1)
post_request.get('update')(number=6, title='update 테스트', content='수정 성공', file='file/update/success')
print(post_request.get('read')(6))

# delete(삭제)
# 넣어야 되는 것: 삭제하고 싶은 데이터(dict)의 'number' 키의 값 - 6번 데이터 삭제
# 삭제가 잘 되었는지 알아보기 위해, select_all 로 전체 리스트 출력
post_request.get('delete')(6)
print(post_request.get('select_all')())