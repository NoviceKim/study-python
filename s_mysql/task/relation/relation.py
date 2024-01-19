from crud_module import *
from field_trip import FieldTrip
from post import Post
import hashlib
from pet_clinic import PetClinic
from office import Office
from conference_room import ConferenceRoom
from part_time import PartTime

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
    # # 5. 예약 추가
    # find_all_query = "select id, name, location from tbl_office"
    #
    # offices = find_all(find_all_query)
    #
    # office_list = []
    #
    # for office in offices:
    #     find_all_by_query = "select id from tbl_conference_room where office_id = %s"
    #     find_all_by_params = office.get("id")
    #
    #     conference_rooms = find_all_by(find_all_by_query, find_all_by_params)
    #
    #     conference_room_list = []
    #
    #     for conference_room in conference_rooms:
    #         find_all_by_query = "select id, time from tbl_part_time where conference_room_id = %s"
    #         find_all_by_params = conference_room.get("id")
    #
    #         part_times = find_all_by(find_all_by_query, find_all_by_params)
    #
    #         part_time_list = []
    #
    #         for part_time in part_times:
    #             part_time_list.append(PartTime(part_time.get("id"), part_time.get("time")))
    #
    #         part_times = tuple(part_time_list)
    #         conference_room_list.append(ConferenceRoom(conference_room.get("id"), part_times))
    #
    #     conference_rooms = tuple(conference_room_list)
    #     office_list.append(Office(office.get("id"), office.get("name"), office.get("location"), conference_rooms))
    #
    # offices = tuple(office_list)
    #
    # message = ""
    #
    # for office in offices:
    #     message += f"{office.id}, {office.name}, {office.location}\n"
    #
    # office_choice = int(input(message))
    # office = offices[office_choice - 1]
    #
    # message = f"회의실 번호를 입력해주세요\n{office.__str__()}"
    # room_choice = int(input(message))
    # conference_room = office.conference_rooms[room_choice - 1]
    #
    # find_all_by_query = "select time from tbl_reservation where conference_room_id = %s"
    # find_all_by_params = conference_room.id,
    #
    # reservations = find_all_by(find_all_by_query, find_all_by_params)
    #
    # conference_room.reservations = reservations
    #
    # time_choice = int(input(conference_room.__str__()))
    # part_time = conference_room.part_times[time_choice - 1]
    #
    # if part_time.status:
    #     find_by_id_query = "select email from tbl_client where email = %s"
    #     find_by_id_params = "kgh1234"
    #     client = find_by_id(find_by_id_query, find_by_id_params)
    #
    #     save_query = "insert into tbl_reservation (time, client_email, conference_room_id) \
    #                   values (%s, %s, %s)"
    #
    #     save_params = part_time.__str__(), client.get("email"), conference_room.id
    #     save(save_query, save_params)
    #
    # else:
    #     print("해당 회의실은 예약하실 수 없습니다.")


    # 6. 회의실 전체 내용 조회 - 단, 예약 완료 된 회의실은 조회하지 않음
    find_all_query = "select o.id, o.name, o.location, c.id, p.time, ifnull(r.time, '예약가능') 'r.time' \
                      from tbl_office o join tbl_conference_room c \
                      on o.id = c.office_id \
                      join tbl_part_time p \
                      on p.conference_room_id = c.id \
                      left outer join tbl_reservation r \
                      on r.conference_room_id = c.id \
                      and p.time = r.time \
                      where r.time is Null"

    offices = find_all(find_all_query)

    for office in offices:
        print(f"{office.get('name')}, {office.get('location')}, {office.get('c.id')}번 회의실, {str(office.get('time'))}, {str(office.get('r.time'))}")
