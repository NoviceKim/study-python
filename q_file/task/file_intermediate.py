# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# 알파벳 걸러내기
# 전부 소문자로 변경
# 글자 수 2개 이상인 것만 골라내기
# 빈도 수 세서 100번 이상인 것들만

# alice.txt 읽어오기
with open('alice.txt', 'r', encoding='utf-8') as alice:
    # 알파벳 하나하나 담을 리스트 선언
    temp = []

    # 파일 전체를 '하나의' 문자열로 읽어와서
    # 전부 소문자로 바꾼 다음, content 변수에 할당 -> 현재 하나의 문자열로 이루어진 상태
    content = alice.read().lower()

    # 숫자랑 특수기호 제거하고, 알파벳만 분리 - list -> str
    # content 문자열에서 글자 하나하나를 검사
    for char in content:
        # 만약 알파벳이면
        if 'a' <= char <= 'z':
            # 리스트에 해당 글자(알파벳 하나) 추가
            temp.append(char)
        # 만약 알파벳이 아니면
        else:
            # 공백을 추가 - 아래에서 .split()으로 공백을 기준점으로 해서 단어별로 분리하기 위함
            temp.append(" ")

    # content 변수에 알파벳 리스트 내용(공백 포함)을 하나하나 붙여서 재할당 -> 숫자랑 특수기호가 없어진 하나의 문자열
    content = "".join(temp)

    # 두 글자 이상인 단어만 분리 - list
    # 문자열을 공백을 기준으로 쪼개서 list로 만들고
    # 이렇게 만들어진 list의 각 인덱스 순회 -> 각각의 인덱스에는 단어가 담겨있는 상태
    # 단어의 길이가 1보다 큰 것들만 분류해서 만든 새로운 list를 words 변수에 할당
    words = [word for word in content.split()
                if len(word) > 1]

# 비어있는 딕셔너리 result를 선언
result = {}

# 각 단어의 등장 횟수 기록 - dict
# 길이가 2 이상인 단어들만 들어있는 리스트(words)의 각 인덱스(단어) 검사
for word in words:
    # result 딕셔너리에서 해당 단어가 key로 존재하는지 검색
    if result.get(word) is not None:
        # 만약 있다면, 해당 단어의 value +1
        result[word] += 1

    # 만약 기존에 없었다면, 해당 단어를 key로 만들고, value는 1로 설정
    else:
        result[word] = 1

    # 여기까지 했으면 {특정 단어 : 등장 횟수, ... }으로 구성된 딕셔너리(result)가 만들어져 있을 것

# 또 다른 딕셔너리 result_final을 생성
result_final = {
    # result 딕셔너리를 돌면서 value가 100 이상인 key(word)만 분류해서
    # {단어 : 등장 횟수, ... } 로 이루어진 딕셔너리를 만든다
    word: result[word] for word in result if result[word] >= 100
}

# result_final.get(각 단어 별 등장 횟수)의 값으로 result_final(단어)를
# 내림차순(reverse=True) 정렬 -> 딕셔너리 재정렬해서 sorted_key 변수에 할당
sorted_key = sorted(result_final, key=result_final.get, reverse=True)

# 정렬된 딕셔너리를 단어 : 등장 횟수 형식으로 각 줄에 반환
for key in sorted_key:
    print(key, result_final[key])