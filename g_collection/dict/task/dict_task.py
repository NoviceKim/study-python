# 추가, 수정, 삭제, 검색, 목록

# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.

# dict_task 추가
# 기존의 list 자료 2개 -> dict 자료 하나로 변경
# 그에 따라 기존 name_list, price_list로 찾았던 것들(해당 변수 썼던 부분들)을
# list_dict['name'] 같은 식으로 수정
# 위 코드는 list_dict['name']의 value = 리스트 자료를 나타내므로, list에서 썼던 메서드 사용 가능
list_dict = {
    'name': [],
    'price': []
}

# list_dict 안의 데이터들을 위와 같은 형태가 아닌
# 'name' : 'price(int형)' 형태로, 그러니까 '사과' : 3000 같은 식으로 저장했다면?
# list에서 썼던 메서드들은 못 쓰게 되더라도, dict에서 썼던 메서드들을 쓸 수 있지 않았을까?


# 제목
title = "* 상품 검색 프로그램 *"

# 일괄 처리를 위한 메세지 변수 선언
result_message = ''


# 각 상황 별로 출력할 메세지들
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격\n'
search_name_message_for_update = '수정하실 상품명을 입력하세요.\n'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격\n'
delete_message = '삭제하실 상품명을 입력하세요.\n'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(같은 상품 존재)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."


# 반복문 내에서 break문을 만나기 전까지, 반복문을 계속해서 실행
while True:
    # 원하는 메뉴에 따른 번호를 입력 받아 int형으로 변환 후, answer 변수에 저장
    answer = int(input(title + '\n' + menu))

    # 추가(1번)
    if answer == 1:
        # 추가할 상품명, 가격을 묻는 메세지 출력
        # '상품명 가격'을 입력받고, 공백으로 분리(.split())해서 각각 new_name, new_price에 저장
        new_name, new_price = input(append_message).split()
        
        # 만약 추가할 상품명이 기존 name_list에 없다면
        if new_name not in list_dict['name']:
            # 새로운 상품의 이름과 그 가격을 각각 name_list와 price_list의 맨 뒤에 저장(.append())
            # 추가할 가격 데이터(new_price)는 int(정수)로 형 변환해서 append
            list_dict['name'].append(new_name)
            list_dict['price'].append(int(new_price))

            # 아래의 에러 메세지를 띄우지 않고, 다음 반복으로 넘어가기 위해 continue 사용
            continue

        # 만약 새로 추가하려는 상품명(new_name)이 기존 name_list에 있다면
        else:
            # '중복으로 인한 추가 실패' 에러 메세지 출력
            result_message = append_error_message

    # 수정(2번)
    elif answer == 2:
        # 수정할 상품명을 묻는 검색창 출력 -> name 변수에 입력한 값 저장
        name = input(search_name_message_for_update)

        # 만약 입력한 상품명(name)이 기존 name_list에 있다면
        if name in list_dict['name']:
            # 그 상품이 있었던 자리(인덱스)에 넣을 이름과 가격을 입력받음
            # 입력받은 '상품명 가격'을 .split()을 사용해 공백 제거 후 new_name, new_price에 할당
            new_name, new_price = input(update_message).split()

            # 새롭게 입력한 상품명(new_name)이 기존 리스트에 없다면
            if new_name not in list_dict['name']:
                # 원래 상품명(name)의 인덱스 번호를 가져와서 index 변수에 저장
                index = list_dict['name'].index(name)

                # 위에서 가져온 인덱스 번호에 있는 이름과 가격을 새로운 것으로 재할당
                list_dict['name'][index], list_dict['price'][index] = new_name, new_price

                # 아래의 에러 메세지를 띄우지 않기 위함
                continue

            # 아래의 에러 메세지를 띄우지 않기 위함
            else:
                result_message = update_error_message2

        # 만약 수정하려고 하는 상품이 없다면 '상품 없음' 메세지 출력
        else:
            result_message = update_error_message1

    # 삭제(3번)
    elif answer == 3:
        # 삭제하고자 하는 상품의 이름을 입력받고, name 변수에 저장
        name = input(delete_message)

        # 만약 기존 name_list에 해당 상품(name)이 있다면
        if name in list_dict['name']:
            # 해당 상품의 인덱스 번호를 변수에 저장
            index = list_dict['name'].index(name)

            # 위에서 저장한 인덱스 번호(index)에 있는 값 제거
            del list_dict['name'][index]
            del list_dict['price'][index]

            # 아래의 에러 메세지를 띄우지 않기 위함
            continue

        # 만약 위 if문에 걸리지 않았다면 = 삭제하려는 상품이 없다면
        # '삭제 실패' 에러 메세지 출력
        result_message = delete_error_message

    # 검색(4번)
    elif answer == 4:
        # 원하는 메뉴의 번호를 한 번 더 입력 받음
        # 1. 상품명으로 검색 / 2. 이름으로 검색
        choice = int(input(search_menu))

        # 상품명으로 검색(4-1번)
        if choice == 1:
            # 찾으려는 상품명을 입력받아 name 변수에 저장
            name = input(search_name_message)

            # 만약 해당 상품(name)이 기존 name_list에 있다면
            if name in list_dict['name']:
                # 해당 상품의 인덱스 번호를 가져와서 index 변수에 저장
                index = list_dict['name'].index(name)

                # name_list, price_list에서 해당 인덱스에 들어있는 값을 가져오고,
                # 해당 값(이름과 가격) 출력
                print(f'{list_dict["name"][index]}, {list_dict["price"][index]}')

                # 아래의 에러 메세지를 띄우지 않기 위함
                continue

            # 만약 찾으려는 상품이 name_list에 없다면 '검색 실패' 메세지 출력
            else:
                result_message = search_name_error_message

        # 가격(오차 범위 ±50%)으로 검색(4-2번)
        elif choice == 2:
            # 가격을 입력받아 int형으로 변환하고, price 변수에 저장
            # 이는 아래의 오차 범위를 계산하는데 쓰기 위함
            price = int(input(search_price_message))

            # price 변수를 사용해서 최대, 최소 오차 값을 저장할 새로운 변수들 생성
            min = price * 0.5
            max = price * 1.5

            # 안쪽 리스트는 오차 범위 내에 있는 상품들의 가격 값을 가져와서 list 형태로 만든다.
            # 바깥쪽 리스트는 위에서 얻은 값들의 위치(인덱스 번호)를 price_list 내에서 검색 한 뒤에,
            # result_index에 해당 인덱스 번호(정수)만 골라 list 형태로 추가한다.

            # dict_task 추가
            # 기존에 있던 list를 dict 형태로 묶어서 변환하는 과정에서...
            # 안쪽 리스트 조건식(min <= price <= max)의 price가 int형이 아닌, str형(문자열)이라서 오류 발생
            # 이는 list_dict['price']에 저장된 가격 값들이 기본 str 타입이고,
            # 그걸 price라는 변수(안쪽 리스트의 comprehension에서만 사용하는 지역변수)에 그대로 넣어, 문자열과 숫자를 비교하는 상황이 되어 발생함
            # 따라서 조건식에 들어가는 price를 int로 형변환해줬고, 그에 따라 숫자끼리의 연산이 되어 오류 해결
            result_index = [list_dict['price'].index(i) for i in [price for price in list_dict['price'] if min <= int(price) <= max]]

            # 만약 result_index의 길이가 0이 아니라면 = 오차 범위 내에 해당하는 결과가 하나라도 있다면
            if len(result_index) != 0:
                # result_index에 저장된 정수에 해당하는 인덱스를 name_list, price_list에서 가져오고
                for i in result_index:
                    # 그 인덱스 번호에 해당하는 데이터(상품명과 가격) 출력
                    print(f'{list_dict["name"][i]}, {list_dict["price"][i]}')

                    # 아래의 에러 메세지를 띄우지 않기 위함
                    continue

            # 만약 오차 범위 내에 해당하는 가격 값이 없다면(len(result_index) == 0)
            # '검색 결과 없음' 에러 출력
            else:
                result_message = search_error_message

        # 없는 메뉴(1, 2번 이외의 번호)를 찾으면 '다시 입력' 에러 출력
        else:
            result_message = error_message

    # 목록보기(5번)
    elif answer == 5:
        # 만약 name_list의 현재 길이가 0이라면 = 요소가 없다면
        if len(list_dict['name']) == 0:
            # '목록 없음' 메세지 출력
            result_message = no_item_message

        # 만약 name_list의 길이가 0이 아니라면 = 요소가 하나라도 있다면
        else:
            # 현재 name_list와 price_list에 있는 데이터를 각 리스트의 0번 인덱스부터 끝까지 출력
            # 출력문의 반복 횟수는 name_list의 길이와 같음
            for i in range(len(list_dict['name'])):
                print(f'{list_dict["name"][i]}, {list_dict["price"][i]}')

                # 아래의 에러 메세지를 띄우지 않기 위해 사용
                continue

    # 나가기
    elif answer == 6:
        # 반복문 탈출
        break

    # 에러 상황
    # 1 ~ 6번 이외의 번호를 입력받았을 경우
    else:
        # '다시 입력' 에러 메세지 출력
        result_message = error_message

    # 위에서 받은 에러 메세지를 일괄 처리
    print(result_message)

    # 처리 이후 메세지 초기화
    result_message = ''
