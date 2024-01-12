# 정렬
num_list = [5, 4, 6, 1, 3]

# 1. sort() 함수
# sort() 내에 아무것도 쓰지 않으면, 요소를 오름차순으로 재정렬함
# 함수 내 reverse를 True로 설정하면 내림차순으로 정렬
# 원본을 수정해버리는 함수라서 자주 쓰는 것은 좋지 않음
# num_list.sort(reverse=True)
# print(num_list)

# 2. sorted
# 리스트에서 제공하는 함수가 아니라서 리스트명.sorted() 형식이 아니라, 단독으로 쓰임
# 마찬가지로 reverse 옵션 있음
# 원본은 그대로 두고, 재정렬된 새로운 리스트를 생성함
sorted_list = sorted(num_list, reverse=True)

print(num_list)
print(sorted_list)

# 문자열에도 sorted 사용 가능
print(sorted("ABC", reverse=True))