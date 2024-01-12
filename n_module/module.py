# calc_add.py 파일안 내용물을 import
import calc_add

# 만약 패키지 안에 있는 모듈을 가져오고 싶을 때는, 해당 폴더명부터 출발하면 된다(구분점은 . 표시)
# 이런 식으로 패키지를 통해 접근했을 때에는 as을 사용한 별칭을 모듈에 붙여주는 것이 좋다
import calc.calc_sub as sub

# calc 폴더 안 calc_sub.py에서 sub(함수)를 가져옴
from calc.calc_sub import sub

# calc.py 안에 있는 모든 것을 가져옴
from calc.calc import *

import os
import sys

# 시스템 경로
print(sys.path)

# 현재 작업 중인 파일의 경로
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == '__main__' 이 있는 파일이 실행파일이다
if __name__ == '__main__':
    # calc_add에서 가져온 add 함수를 사용
    print(calc_add.add(2, 3))
    # print(sub.sub(10, 5))

    # from을 통해 import 한 경우에는 해당 필드명을 바로 입력해도 된다
    # 이미 그 필드가 어디서 왔는지 알고 있기 때문
    print(sub(10, 5))

    # 구분선
    print('=' * 20)

    c = Calculator(10, 5)
    print(c.add())
    print(c.sub())
