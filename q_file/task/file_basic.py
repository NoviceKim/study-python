# fish.txt 파일을 하나 만들고
# 사용자에게 입력받은 물고기를 fish.txt 에 작성한다.
# 사용자가 q를 입력하면, fish.txt 안 내용 전체를 삭제한다
# 사용자가 r을 입력하면 fish.txt 안 내용 전체를 출력한다

# # 조건부 무한 반복
# while True:
#     # 일단 없으면 만들고, 있으면 연다
#     with open('fish.txt', 'a', encoding='utf-8') as file:
#         # 입력받음
#         fish = input('물고기를 입력해주세요: ')
#
#         # 만약 'q'를 입력받았다면
#         if fish == 'q':
#             # 'w'를 사용해서 내용 초기화하고 반복문 탈출
#             with open('fish.txt', 'w', encoding='utf-8'):
#                 break
#
#         # 만약 'c'를 입력받았다면 초기화하지 않고 반복문 탈출
#         if fish == 'c':
#             break
#
#         # 만약 'r'을 입력받았다면
#         if fish == 'r':
#             # fish.txt 파일 읽어오고
#             with open('fish.txt', 'r', encoding='utf-8') as read_file:
#                 # 아래 while문에서 문자열 비교할 때 쓸 변수 생성(초기값 None)
#                 line = None
#
#                 # 빈 문자열이 나올 때까지 반복 실행
#                 # 만약 문자열이 비어있지 않으면 = 뭐라도 있으면
#                 while line != '':
#                     # fish.txt에서 한 줄 읽어서 line 변수에 할당하고, 다음 줄로 커서 이동
#                     line = read_file.readline()
#                     # 읽어온 문자열 출력
#                     print(line, end='')
#                 # 더 이상 읽어올 문자열이 없으면, 다음 줄 무시하고 다음 반복으로
#                 continue
#
#         # 'q' 나 'r', 'c' 를 입력하지 않았다면 여기로 옴
#         # 만약 위의 세 가지를 입력하지 않았다면, fish.txt에 입력한 문자열 + 줄바꿈 추가
#         file.write(f'{fish}\n')

# '고등어' 를 '참치' 로 변경
# 수정 완료 후 문자열을 저장할 변수 선언
content = ''

# 일단 읽어온 다음
with open('fish.txt', 'r', encoding='utf-8') as file:
    # 읽어올 문자열 하나하나를 담을 변수 선언
    line = None

    # 읽어온 문자열이 비어있지 않으면
    while line != '':
        # line 변수에 해당 문자열 할당
        line = file.readline()

        # 만약 '고등어\n' 를 읽어왔다면
        if line == '고등어\n':
            # '고등어' 대신 '참치' 를 content에 추가
            content += '참치\n'
            # 아래 줄 무시하고 다음 반복으로
            continue

        # 만약 '고등어' 이외의 다른 것을 읽어왔다면, 그대로 content 에 추가
        content += line

    # 수정 완료 후 문자열이 잘 만들어졌는지 확인
    print(content)

# fish.txt 읽어온 다음 내용 초기화
with open('fish.txt', 'w', encoding='utf-8') as file:
    # content 에 저장된 문자열을 fish.txt에 추가 -> 파일 닫음
    file.write(content)

# fish.txt 다시 읽어옴
with open('fish.txt', 'r', encoding='utf-8') as file:
    # 빈 문자열 뒤에 읽어온 문자열 추가
    # 각 문자열에 \n 이 있었기 때문에 줄바꿈 적용됨
    print("".join(file.readlines()))