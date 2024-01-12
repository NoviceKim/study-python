data = 10

# 2진수로 출력
print(bin(data))

# 8진수로 출력
print(oct(data))

# 16진수로 출력
print(hex(data))

# 실수 형태로 출력
print(float(data))

data = 10.93

# 정수 형태로 출력(소수점 이하 버림)
print(int(data))

# 문자열로 출력
print(type(str(data)))
print(str(data))

# boolean 형태로 출력
# 숫자 값을 넣었을 때 - 0은 False, 나머지는 True
print(bool(0))
print(bool(1204))
print(bool(1))

# 문자열을 넣었을 때 - 비어있으면 False, 뭐라도 들어있으면 True
print(bool(""))
print(bool("A"))
