# 기본 내장된 기능이라 따로 import 할 필요 없이
# json 관련 기능을 자동완성하면 import 역시 자동으로 해준다
import json

# 큰 수(int)를 쓸 때 3자리마다 쓰는 콤마(,) 대신 언더바(_)를 쓰면
# 실행할 때에는 그 언더바 부분이 생략된다
data = {'name': "책", 'price': 25_000, 'stock': 55}

# print(data)

# dict 형식의 데이터를 .json 으로 만들어서 변수에 저장
# '책' 글자가 "\ucc45" 가 되는 건 유니코드(\u)에 의한 것
# ensure_ascii - False로 설정하면 한글을 유니코드가 아닌 원본으로 출력
# indent - 보기 좋게 바꿔주며, 전달한 값은 들여쓰기의 공백 개수
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# 출력해보면 키가 쌍따옴표("")로 감싸진 것을 볼 수 있음
print(json_data)

# json을 dict로 변환
print(json.loads(json_data))