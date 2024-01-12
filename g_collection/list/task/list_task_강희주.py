# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.

name_list = []
price_list = []

title = "카페 메뉴"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

# 제목 출력
print(title)
# 무제한 반복
while True:
    # 메뉴의 숫자를 입력하는 변수
    choice = int(input(menu))
    # 추가
    # 메뉴에 1을 입력하였을 때
    if choice == 1:
        # 사용자에게 상품 이름과 가격을 한번에 입력받은 후 이름과 가격으로 나누어 각각의 변수에 담기
        name, price = input(append_message+"\n").split()
        # 입력받은 상품명이 리스트에 없다면(새로운 입력이라면)
        if name not in name_list:
            # 상품명을 이름 리스트에 추가
            name_list.append(name)
            # 가격을 가격 리스트에 추가
            price_list.append(int(price))
            # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
            continue
        # 입력받은 상품명이 중복이라면 에러 메세지 출력
        else:
            result_message = append_error_message
    # 수정
    # 메뉴에 2를 입력하였을 때
    elif choice == 2:
        # 수정할 상품명을 입력 받음
        modify = input(search_name_message_for_update+"\n")
        # 수정할 상품명이 이름 리스트에 있다면
        if modify in name_list:
            # 수정할 상품명과 가격을 나누어 각각의 변수에 담음
            new_name, new_price = input(update_message+'\n').split()
            # 만약 수정할 상품명이 리스트에 없다면
            if new_name not in name_list:
                # 수정할 상품명과 가격을 기존 리스트에서 찾아서 변경
                index = name_list.index(modify)
                name_list[index], price_list[index] = new_name, new_price
                # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                continue
            # 수정할 상품명이 리스트에 있다면 에러메세지 출력
            else:
                result_message = update_error_message2
        # 수정할 상품명이 이름 리스트에 없다면 에러메세지 출력
        else:
            result_message = update_error_message1
    # 삭제
    # 3번을 눌러 삭제 메뉴
    elif choice == 3:
        # 삭제할 상품명을 입력받음
        delete = input(delete_message+"\n")
        # 삭제할 상품명이 이름 리스트에 있다면
        if delete in name_list:
            # 해당 가격과 상품명의 인덱스를 선언(추후 수정을 해도 변하지 않도록)
            index = name_list.index(delete)
            # 상품명에 해당 하는 가격 삭제
            del price_list[index]
            # 해당 상품명 삭제
            del name_list[index]
            # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
            continue
        # 삭제할 상품명이 이름 리스트에 없다면 오류메세지 출력
        else:
            result_message = delete_error_message
    # 검색
    # 4번을 눌러 검색 메뉴
    elif choice == 4:
        # 검색할 메뉴를 선택하기 위해 입력받은 문자열을 정수로 변환하여 선언
        search_choice = int(input(search_menu+"\n"))
        # 검색할 메뉴 선택
        if search_choice == 1:
            # 검색한 상품명을 변수에 담음
            name_for_search = input(search_name_message+'\n')
            # 만약 상품명이 이름 리스트에 있다면
            if name_for_search in name_list:
                # 상품명의 해당하는 인덱스 번호를 먼저 선언
                index = name_list.index(name_for_search)
                # 각 인덱스 번호에 해당하는 상품명과 가격의 값을 출력
                print(f'{name_list[index]},{price_list[index]}')
                # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                continue
            # 상품명이 이름 리스트에 없다면 에러 메세지 출력
            else:
                result_message = search_name_error_message
        # 검색할 메뉴 선택 2
        elif search_choice == 2:
            # 가격을 검색하는 경우에는 가격을 입력 받아 정수로 변환하여 변수로 선언
            price_for_search = int(input(search_price_message+"\n"))
            # 최소 값 선언 (-50%)
            min = price_for_search * 0.5
            # 최대 값 선언 (+50%)
            max = price_for_search * 1.5
            # 검색하는 가격이 최솟값에서 최대값 사이에 있는 경우, 해당 가격을 출력하고, 해당 가격을 담은 리스트의 인덱값을 출력하여 결과 인덱스에 담음
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price_for_search <= max]]
            # 만약 값이 하나라도 있다면
            if len(result_index) != 0:
                # 인덱스 값에 해당 하는 상품명과 가격을 출력
                for i in result_index:
                    print(f'{name_list[i]},{price_list[i]}')
                    # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                    continue
        # 검색 메뉴의 1,2를 입력하지 않은 경우 오류메세지 출력
        else:
            result_message = search_error_message

    # 목록
    # 5번을 입력하여 목록메뉴
    elif choice == 5:
        # 이름 리스트에 값이 없는 경우 (입력한 상품명이 없는경우)
        if len(name_list) == 0:
            # 에러 메세지 출력
            result_message = no_item_message
        # 이름 리스트에 값이 있는 경우 (입력한 상품명이 있는 경우)
        else:
            # 입력한 상품명의 갯수만큼 목록 출력
            for i in range(len(name_list)):
                print(f'{name_list[i]},{price_list[i]}')
                # 오류 메세지를 출력하지 않기 위해 다음 문장 생략
                continue
    # 나가기
    # 6번을 눌러 나가기 메뉴
    elif choice == 6:
        # 전체 반복에서 나가기
        break
    # 그 외
    # 메뉴 선택시 1~6 이외의 값을 넣은 경우
    else:
        # 오류 메세지 출력
        result_message = error_message
    # 결과 값 출력
    print(result_message)
