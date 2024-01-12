# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
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

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다. (구분점은 공백문자_split 사용)
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지않는다면. (없다면)
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위하여 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존상품과 중복되었다면
            # 알맞은 메세지를  result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 사용자에게 수정할 상품명을 입력받아 name에 담는다.
        name = input(search_name_message_for_update)

        # 입력받은 상품명(수정할 상품명)이 name_list에 있는지 검사.(있다면)
        if name in name_list:
            # 새로 수정할 상품명과 가격을 사용자에게 입력받는다. (구분점은 공백문자 - split 사용)
            # 입력받은 값(새로 수정할 상품명과 가격)을 각각의 변수에 담는다. new_name, new_price
            new_name, new_price = input(update_message).split()

            # 새로 수정할 상품명이 name_list에 없으면(새로 수정해야한다면)
            if new_name not in name_list:
                # 수정 전의 상품명(name)을 name_list의 index번호를 받아와 index 변수에 넣어준다. (위치탐색)
                # why? 그 자리에 새로 수정할 new_name을 넣어줘야하니까.
                index = name_list.index(name)
                #name_list의 [index]번호 위치와 price_list[index]번호 위치에 각각 새로 수정할 값 new_name, new_price를 넣어준다.
                name_list[index], price_list[index] = new_name, new_price
                # 수정이 완료되었으면 아래 코드를 실행할 필요 없으므로  continue 입력
                continue

            # 새로 수정할 상품명이 name_list에 있다면 (중복되기 때문에 수정 실패 메세지 출력)
            else:
                result_message = update_error_message2
        # 입력받은 상품명(기존 상품명 name)이 name_list에 없다면, (존재하지않는 상품이기때문에 수정실패 메세지 출력)
        else:
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 사용자에게 삭제할 상품명을 입력받아 name 변수에 할당.
        name = input(delete_message)
        # 입력받은 상품명이 name_list에 있다면 (삭제가능하므로)
        if name in name_list:
            # name_list안에 index번호로 삭제할 상품(name)위치 받아와 index라는 변수에 넣어주기
            index = name_list.index(name)
            # name_list의 [index]번호(받아온 위치 값)을 del 해줌
            del name_list[index]
            # 가격도 삭제해야하므로, price_list의 [index]번호(받아온 위치 값)을 del 해줌
            del price_list[index]
            # 수정이 완료되었으면 아래 코드를 실행할 필요 없으므로  continue 입력
            continue
        
        # 사용자가 입력한 상품명이 name_list에 없다면 존재하지않는 상품명이므로 (삭제불가하므로) 삭제실패 메세지 출력.
        else:
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 사용자가 검색할 메뉴 입력받아 choice에 할당,(옵션은 2가지 이므로 (1. 상품명 검색 /  2. 가격으로 검색)  int로 형변환
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 사용자가 입력한 상품명을  name이라는 변수에 할당.
            name = input(search_name_message)
            # 입력한 상품명(name)이 name_list에 있다면, (찾을 수 있으므로)
            if name in name_list:
                # 입력한 상품명의 위치를 찾아오기위해 name_list의 index번호를 불러오고, 그 값을 index 변수에 담아준다.
                index = name_list.index(name)

                # formatting을 통해 name_list의 [index] 값 = 해당 검색한 상품명과
                # price_list의 [index] 값 = 검색한 상품의 가격을 출력한다.
                print(f'{name_list[index]}, {price_list[index]}')
                # 수정이 완료되었으면 아래 코드를 실행할 필요 없으므로  continue 입력
                continue

            # 검색할 상품명이 name_list에 없다면, 출력할 수 없으므로 result_message에 검색실패(존재하지않는 상품명)오류메세지 할당.
            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 사용자가 가격으로 검색했을 경우, 사용자가 입력한 가격을 int로 형변환하여 받아온다.
            price = int(input(search_price_message))
            # 가격 검색 시 오차 범위는 ±50%로 설정한다. -> 이 조건을 추가하기위해 50% == 0.5 이므로 각각 min, max를 아래와같이 설정.
            min = price * 0.5
            max = price * 1.5
            # price_list에서 검색한 사용자가 검색한 가격이 if조건식(최솟값과 최대값사이)에 부합할 경우 price에 담아 list형식으로 만든다.
            # price_list의 인덱스로 담아 result_index 변수에 할당.
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]

            # 만약 가격으로 검색해서 list로 담은 result_index의 길이가 0이 아닌경우 (값이 있는 경우)
            # for문을 사용해서 result_index에 있는 값을 i에 담아 name_list[i] 상품명, prcie_list[i] 가격을 각각 출력한다.
            if len(result_index) != 0:
                for i in result_index:
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue
            # 사용자가 입력한 검색옵션 (1,2번이 아닐 경우)
            # result_message에 "검색 실패' 오류메세지 할당.
            else:
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 만약 name_list(상품명리스트)길이가 0인경우 == 상품이 담겨있지않는 경우
        # reusult_message에 상품이 없다는 no_item_message 할당.
        if len(name_list) == 0:
            result_message = no_item_message

        # 그렇지않은 경우 (상품리스트에 상품이 담겨있는 경우)
        else:
            # name_list(상품리스트) 길이만큼 for문으로 돌아 각 값을 i에 담아 name_list[i] 출력 == (상품리스트에 담긴 상품, 즉 목록 출력)
            for i in range(len(name_list)):
                print(f'{name_list[i]}')
                continue

    # 나가기
    # 사용자가 6번 나가기 선택 시, break문을 통해 반복문 탈출
    elif choice == 6:
        break

    # 그 외
    # 1~6번이 아닌 다른 번호 입력 시 result_message에 error_message 할당
    else:
        result_message = error_message

    print(result_message)
    result = "" # 오류메세지의 출력을 막기위해 혹시몰라 초기화

# print(name_list, price_list, sep='\n')





