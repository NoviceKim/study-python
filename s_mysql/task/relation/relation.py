from crud_module import *
from field_trip import FieldTrip
from post import Post
import hashlib
from pet_clinic import PetClinic
from room import Room

if __name__ == '__main__':
    # 학부모 정보 추가
    # save_many_query = "insert into tbl_parent(name, age, gender, address, phone) \
    #                    values(%s, %s, %s, %s, %s)"
    # save_many_params = (
    #     ('한동석', 20, '남자', '경기도 남양주', '01012341234'),
    #     ('홍길동', 30, '여자', '서울시 강남구', '01033333333'),
    #     ('이순신', 40, '선택안함', '경기도 남양주', '01055555555')
    # )
    # save_many(save_many_query, save_many_params)

    # 아이 추가
    # find_by_id_query = "select id, name, age, gender, address, phone from tbl_parent where id = %s"
    # find_by_id_params = 1,
    # find_by_id_params = 3,
    # find_by_id_params = 2,
    # parent = find_by_id(find_by_id_query, find_by_id_params)
    # parent_id = parent.get("id")

    # save_many_query = "insert into tbl_child(name, age, gender, parent_id) \
    #               values(%s, %s, %s, %s)"
    # save_many_params = (
    #     ('둘리', 4, '남자', parent_id),
    #     ('또치', 9, '여자', parent_id),
    # )
    # save_many_params = (
    #     ('도너', 4, '남자', parent_id),
    # )
    # save_many_params = (
    #     ('마이콜', 11, '선택안함', parent_id),
    # )
    # save_many(save_many_query, save_many_params)

    # 체험학습 추가
    # save_many_query = "insert into tbl_field_trip (title, content, count) \
    #                    values(%s, %s, %s)"
    # save_many_params = (
    #     ('테스트 제목1', '테스트 내용1', 10),
    #     ('테스트 제목2', '테스트 내용2', 50),
    #     ('테스트 제목3', '테스트 내용3', 40),
    #     ('테스트 제목4', '테스트 내용4', 100)
    # )
    # save_many(save_many_query, save_many_params)

    # 첨부파일 추가
    # save_query = "insert into tbl_file(file_path, file_name) \
    #               values(%s, %s)"
    # save_params = ('2024/01/18', 'img002.png')
    # save(save_query, save_params)

    # find_all_query = "select id from tbl_file order by id desc"
    # file_id = find_all(find_all_query)[0].get("id")
    #
    # find_all_query = "select id from tbl_field_trip order by id desc"
    # field_trip_id = find_all(find_all_query)[0].get("id")
    #
    # save_query = "insert into tbl_field_trip_file(id, field_trip_id) \
    #               values (%s, %s)"
    # save_params = file_id, field_trip_id

    # save(save_query, save_params)

    # 체험학습 상세보기
    # find_by_id_query = "select id, title, content, count \
    #                     from tbl_field_trip \
    #                     where id = %s"
    # find_by_id_params = 4,
    # field_trip = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select f.id, f.file_path, f.file_name \
    #                     from tbl_file f join tbl_field_trip_file ft \
    #                     on ft.field_trip_id = %s and f.id = ft.id"
    #
    # files = find_all_by(find_all_by_query, find_by_id_params)
    #
    # field_trip = FieldTrip(field_trip.get("id"), field_trip.get("title"), field_trip.get("content"), field_trip.get("count"), *files)
    # print(field_trip.__dict__)
    # print(field_trip.get_full_path())

    # 회원가입
    ## save_query = "insert into tbl_user(user_id, password, name, address) \
    ##               values(%s, hex(aes_encrypt(%s, 'hello mysql')), %s, %s)"
    #
    # save_query = "insert into tbl_user(user_id, password, name, address) \
    #               values(%s, %s, %s, %s)"
    #
    # password = hashlib.sha256()
    # password.update('5555'.encode('utf-8'))
    # password = password.hexdigest()
    #
    # save_params = 'hgd9999', password, '홍길동', '서울시 강남구'
    # save(save_query, save_params)

    # 게시글 작성
    # find_by_id_query = "select id from tbl_user where id = %s"
    # find_by_params = 1,
    #
    # user = find_by_id(find_by_id_query,find_by_params)
    #
    # save_query = "insert into tbl_post (title, content, user_id) \
    #               values (%s, %s, %s)"
    # save_params = '테스트 제목1', '테스트 내용1', user.get("id")
    #
    # save(save_query,save_params)

    # 게시글 목록
    # find_all_query = "select p.id, title, content, created_on, u.name \
    #                   from tbl_user u join tbl_post p\
    #                   on u.id = p.user_id\
    #                   order by id desc"
    #
    # posts = find_all(find_all_query)
    #
    # for post in posts:
    #     print(post)

    # 게시글 상세보기
    # find_by_id_query = "select id from tbl_post where id = %s"
    # find_by_id_params = 1,
    #
    # post = find_by_id(find_by_id_query, find_by_id_params)
    # post_id = post.get("id")
    #
    # find_by_id_query = "select p.id, title, content, created_on, u.name \
    #                     from tbl_user u join tbl_post p \
    #                     on u.id = p.user_id\
    #                     where p.id = %s"
    # find_by_id_params = post_id,
    #
    # post = find_by_id(find_by_id_query, find_by_id_params)
    #
    # # 댓글 목록
    # find_all_by_query = "select r.id, name, content\
    #                from tbl_user u join tbl_comment r \
    #                on r.post_id = %s and u.id = r.user_id"
    #
    # find_all_by_params = post.get("id"),
    # replies = find_all_by(find_all_by_query, find_all_by_params)
    #
    # post = Post(post.get("id"), post.get("title"), post.get("content"), post.get("created_on"), post.get("name"),
    #             replies)
    # print(post.__dict__)

    # 댓글 작성
    # find_by_id_query = "select id from tbl_user where id = %s"
    # find_by_id_params = 2,
    # user = find_by_id(find_by_id_query, find_by_id_params)
    # user_id = user.get("id")
    #
    # find_by_id_query = "select id from tbl_post where id = %s"
    # find_by_id_params = 1,
    # post = find_by_id(find_by_id_query, find_by_id_params)
    # post_id = post.get("id")
    #
    # save_many_query = "insert into tbl_comment (content, user_id, post_id) \
    #                    values (%s, %s, %s)"
    #
    # save_many_params = (
    #     ('댓글 테스트1', user_id, post_id),
    #     ('댓글 테스트2', user_id, post_id),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # # 보호자 추가
    # save_many_query = "insert into tbl_owner (name, age, phone, address) \
    #               values(%s, %s, %s, %s)"
    #
    # save_many_params = (
    #     ('김광협', 27, '01086709568', '경기도 광주시'),
    #     ('홍길동', 42, '01012345678', '서울시 강남구'),
    #     ('허준', 45, '01090123456', '경기도 성남시')
    # )
    #
    # save_many(save_many_query, save_many_params)
    #
    #
    # # 반려동물 추가
    # # 추가하기 전에, 특정 id를 가진 주인의 정보를 가져옴
    # find_by_id_query = "select id from tbl_user where id = %s"
    # find_by_id_params = 2,
    #
    # # 위 쿼리문과 변수로 해당 주인의 정보를 가져와서(dict), "id" 값을 owner_id 변수에 저장
    # owner = find_by_id(find_by_id_query, find_by_id_params)
    # owner_id = owner.get("id")
    #
    # # 이제 반려동물 테이블에 한 번에 여러가지 정보 추가(save_many)
    # save_many_query = "insert into tbl_pet (name, ill_name, age, weight, owner_id) \
    #                    values(%s, %s, %s, %s, %s)"
    #
    # save_many_params = (
    #     ('삼색이', '감기', 7, 3.5, owner_id),
    #     ('치즈', '비염', 4, 2.7, owner_id - 1),
    # )
    #
    # save_many(save_many_query, save_many_params)
    #
    # # 전체 목록
    # find_all_query = "select id, name, age, phone, address from tbl_owner"
    #
    # owners = find_all(find_all_query)
    #
    # owner_with_pet = []
    #
    # for owner in owners:
    #     find_all_by_query = "select id, name, ill_name, age, weight, owner_id from tbl_pet \
    #                          where owner_id = %s"
    #
    #     find_all_by_params = owner.get("id")
    #
    #     pets = find_all_by(find_all_by_query, find_all_by_params)
    #
    #     owner_with_pet.append(PetClinic(owner.get("id"), owner.get("name"), owner.get("age"),owner.get("phone"),owner.get("address"), pets))
    #
    # for owner in owner_with_pet:
    #     print(owner.__dict__)

    # # 1. 회원가입
    # # DBMS에 보낼 insert 쿼리문 서식
    # save_many_query = "insert into tbl_client (email, password, name) values (%s, %s, %s)"
    #
    # # 비밀번호 암호화
    # password = hashlib.sha256()
    # password.update('1234'.encode('utf-8'))
    # password = password.hexdigest()
    #
    # # insert 쿼리문 서식에 넣을 데이터들
    # save_many_params = (
    #     ('kgh1234', password, '김광협'),
    #     ('hgd2345', password, '홍길동'),
    #     ('hj3456', password, '허준'),
    #     ('yjs4567', password, '유재석'),
    #     ('jdy5678', password, '장도연')
    # )
    #
    # # 위 데이터들로 쿼리문 완성해서 DBMS에 보내기
    # save_many(save_many_query, save_many_params)
    #
    #
    # # 2. 회사 추가
    # save_many_query = "insert into tbl_office (name, location) values (%s, %s)"
    #
    # save_many_params = (
    #     ('하나어패럴', '서울시 강남구'),
    #     ('두리물산', '경기도 용인시')
    # )
    #
    # save_many(save_many_query, save_many_params)
    #
    #
    # # 3. 회의실 추가
    # # 회의실 테이블의 office_id는 사무실 테이블의 id를 받아온 fk
    # # 따라서, 사무실 테이블에서 id를 먼저 받아와야 됨
    # find_by_id_query = "select id, name, location from tbl_office where id = %s"
    # find_by_id_params = 1,
    #
    # # 특정 id를 가진 사무실 데이터(dict)를 받아오고
    # office = find_by_id(find_by_id_query, find_by_id_params)
    #
    # # 'id'에 해당하는 키 값을 office_id 변수에 할당
    # office_id = office.get("id")
    #
    # # 회의실 테이블에 보낼 insert문 서식
    # save_many_query = "insert into tbl_conference_room (office_id) values (%s)"
    #
    # # office_id는 숫자값이라 연산이 가능
    # save_many_params = (
    #     office_id,
    #     office_id,
    #     (office_id + 1)
    # )
    #
    # save_many(save_many_query, save_many_params)
    #
    #
    # # 4. 회의실 별 이용 가능 시간 추가
    # # 회의실 테이블에서 특정 id를 가져옴
    # find_by_id_query = "select id from tbl_conference_room where id = %s"
    # find_by_id_params = 1
    #
    # # 해당 id 값 추출
    # conference = find_by_id(find_by_id_query, find_by_id_params)
    # conference_id = conference.get('id')
    #
    # # 가져온 id값을 기반으로 이용 가능 시간 테이블에 보낼 쿼리문 작성
    # save_many_query = "insert into tbl_part_time (time, conference_room_id) \
    #                    values (%s, %s)"
    #
    # save_many_params = (
    #     ("09:00:00", conference_id),
    #     ("11:00:00", conference_id),
    #     ("13:30:00", conference_id),
    #     ("15:00:00", conference_id),
    #     ("10:00:00", conference_id + 1),
    #     ("14:00:00", conference_id + 1),
    #     ("16:00:00", conference_id + 1),
    #     ("10:00:00", conference_id + 2),
    #     ("14:00:00", conference_id + 2)
    # )
    #
    # save_many(save_many_query, save_many_params)
    #
    #
    # 5. 예약 추가
    # 이메일로 로그인 - 회의실 검색 - 예약시간 선택 순으로 진행

    # 이메일 로그인
    sign_in_email = input("이메일을 입력해주세요: ")

    # 입력받은 이메일로 고객 테이블에 있는 데이터 조회
    find_by_id_query = "select * from tbl_client where email = %s"
    find_by_id_params = sign_in_email

    target_client = find_by_id(find_by_id_query, find_by_id_params)

    # 만약 어떤 데이터라도 찾았다면(= 입력한 이메일이 테이블에 있다면)
    if target_client:
        # 이번에는 비밀번호 검증 실행
        sign_in_password = input("비밀번호를 입력해주세요: ")

        # 입력한 비밀번호를 암호화해서, 다시 sign_in_password 변수에 할당
        encryption = hashlib.sha256()
        encryption.update(sign_in_password.encode('utf-8'))
        sign_in_password = encryption.hexdigest()

        # 비밀번호 인증까지 완료되면
        if sign_in_password:
            # 예약할 회의실 번호를 입력받음
            target_conference_room = input("예약할 회의실의 번호를 입력해주세요: ")

            # 이번에는 입력한 회의실 번호와 일치하는 데이터 전체가 필요하므로, find_all_by()를 사용
            # 단, 이후 과정에 회의실 별 예약 가능 시간에 대한 정보rk 필요하므로
            # 결국 예약 가능 시간 테이블과 조인해서, 해당 테이블에 있는 예약 가능 시간을 가져와야 된다
            find_all_by_query = "select pt.time from tbl_conference_room cr join tbl_part_time pt \
                                 on cr.id = pt.conference_room_id \
                                 and pt.conference_room_id = %s"

            find_by_id_params = target_conference_room,

            # 입력한 회의실의 예약 가능 시간을 가져옴
            available_time = find_all_by(find_by_id_query, find_by_id_params)

            # 사용자가 원하는 예약 시간을 입력받음
            target_time = input("원하는 예약 시간을 입력해주세요: ")

            # 위에서 입력받은 예약할 회의실, 예약할 시간을 바탕으로 예약 테이블에서 검색
            # 입력받은 데이터 두 가지를 모두(and) 가진 데이터가 있는지 조회하기 위함
            find_by_id_query = "select id, time, created_date, client_email, conference_room_id \
                                from tbl_reservation \
                                where conference_room_id = %s and time = %s"

            find_by_id_params = target_conference_room, target_time,

            reservation_request = find_by_id(find_by_id_query, find_by_id_params)

            # 만약 조회된 데이터가 없다면 = 같은 회의실을 같은 시간대에 예약한 건이 없다면
            # 해당 건은 예약이 가능하다는 의미이니, 예약 테이블에 insert 쿼리문 전송
            if not reservation_request:
                save_query = "insert into tbl_reservation (time, client_email, conference_room_id) \
                              values(%s, %s, %s)"

                save_params = target_time, sign_in_email, target_conference_room

                save(save_query, save_params)

            # 만약 같은 회의실을 같은 시간대에 예약한 건이 있다면, 예약 불가 메세지 출력
            else:
                print("해당 회의실은 예약하실 수 없습니다. 다시 시도해주세요.")

        # 만약 입력한 비밀번호가 고객 테이블에 있는 것과 다른 경우, 비밀번호 재확인 메세지 출력
        else:
            print("비밀번호가 일치하지 않습니다. 다시 확인해주세요.")

    # 만약 입력한 이메일이 고객 테이블에 없을 경우, '회원 없음' 메세지 출력
    else:
        print("해당 회원을 찾을 수 없습니다. 다시 입력해주세요.")

    # 6. 회의실 전체 내용 조회 - 단, 예약 완료 된 회의실은 조회하지 않음
    # 회의실 테이블 내용 전부 가져와서, target_rooms 변수에 할당(list 안 dict)
    find_all_query = "select id, office_id from tbl_conference_room"
    target_rooms = find_all(find_all_query)

    # 회의실 dict를 담을 빈 list 준비
    rooms_part = []

    # list 순회
    for room in target_rooms:

        # 특정 id를 가진
        find_all_by_query = "select id, time, conference_room_id from tbl_part_time where conference_room_id = %s"
        find_all_by_params = target_rooms.get("id"),
        part = find_all_by(find_all_by_query, find_all_by_params)
        rooms_part.append(
            Room(target_rooms.get("id"), target_rooms.get("office_id"), target_time))

    for room in rooms_part:
        print(target_rooms.__dict__)