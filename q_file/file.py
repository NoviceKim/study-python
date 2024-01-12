# 절대 경로
# 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# C:a/b, D:/user/kgh/... 등

# 상대 경로
# 현재 위치에 따라 바뀌는 경로
# ./ - 현재 경로(생략 가능), ../ - 이전 경로(뒤로 가기)
# ./src/images, ../../a/b, src/images 등

# # 파일 생성('w')
# # 없다면 만들고, 있다면 덮어씌운다
# # 단 encoding='utf-8' 을 쓰지 않으면 글자가 깨져서 보임
# file = open('food.txt', 'w', encoding='utf-8')
# file.write('불고기\n')
# file.write('돈까스\n')
#
# # 사용한 파일은 반드시 .close() 로 닫기
# # 닫지 않으면 나중에 수정이나 삭제가 불가능해짐
# file.close()
#
# 내용 추가
# 위에서 food.txt 를 만들었으니, 새로 생성하지 않음
# file = open('food.txt', 'a', encoding='utf-8')
# file.write('피자\n')
# file.close()

# # 파일 읽기
# # 마찬가지로 인코더(utf-8)가 필요함
# file = open('food.txt', 'r', encoding='utf-8')
# line = None
# 
# while line != '':
#     line = file.readline()
#     print(line, end='')
# 
# file.close()
#
# # with 문을 쓰면 콜론 안에 들여쓰기 한 문장만 실행하고
# # 끝나면 자동으로 close까지 해준다
# with open('food.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines())

# 수정
content = ''        # 읽어온 문자열들을 담을 변수

with open('food.txt', 'r', encoding='utf-8') as file:
    line = None

    while line != '':
        line = file.readline()
        # 만약 '햄버거' 를 발견했으면, '치킨' 을 대신 content에 추가
        if line == '햄버거\n':
            content += '치킨'
            continue
        # '햄버거' 가 아닌 나머지 문자열은 그대로 content에 추가
        content += line

    # 수정 완료된 문자열 확인
    print(content)

with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

with open('food.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))