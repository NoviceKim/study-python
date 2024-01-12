from typing import List, Dict, Set, Tuple, Union, Final

# Final - 이 값은 더 이상 변경하면 안 된다는 것을 알려주는 지표
data: Final[int] = 10

# 변경하면 안 된다는 것을 알려만 주는 거지, 변경하는 것을 막지는 못하므로 주의
data = 20
print(data)

class A:
    pass

class B:
    # Union - 대괄호 안의 다양한 자료형을 허용
    # 뒤에 있는 or 기호(|) 역시 같은 기능을 함(파이썬 3.10 버전부터 사용 가능)
    # 맨 뒤에 있는 화살표: 화살표 뒤에 있는 타입의 자료(여기서는 int형)가 출력된다

    # 위의 Final과 마찬가지로 각 인자 뒤에 지정한 타입은 주석의 기능만 하는 것이고
    # 실제로는 해당 타입 이외의 데이터를 넣는 것을 막지는 못한다(JS의 TypeScript랑 다름)
    def __init__(self):
        pass

    @staticmethod
    def test(data: Union[int, str], number: int | float, data1: int, datas: List[int], data_dict: Dict[int]) -> int:
        return 10

b = B()
b.test()