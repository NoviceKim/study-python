import os
import psutil

process_object = psutil.Process(os.getpid())
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i ** 2 for i in range(100)]
print(data_list)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')

print( f'\n{"#" * 50}\n' )

memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i ** 2 for i in range(100))

# 그대로 출력하면 객체 형태로 출력됨
print(data_generator)

# 그래서 next로 한 번 감싸줘야 하나씩 나온다
print(next(data_generator))

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')


# 제너레이터 함수
def increase(number: int = 0):
    # 무한 루프 돌면서 +1 씩
    while True:
        number += 1
        # yield는 return과 같지만, 여기서의 반환은 next로만 호출 가능함
        # 즉, yield를 썼다면, 그 함수는 제너레이터 객체다
        yield number
