# 실습 1
# 정수 2개를 변수에 담기
num1 = 2
num2 = 5
total = num1 + num2

# 두 정수의 합을 아래 형식으로 출력하기
# 예시 - 1 + 3 = 4
# 다음 메세지와의 구분을 위해 \n으로 줄 바꿈
print('\n%d + %d = %d\n' % (num1, num2, total))



# 실습 2
# 아래 메세지를 .format 함수를 이용해서 출력한다
# Hello 파이썬, Python is Fantastic!
# Hello 장고, Django is Fantastic!
# Hello 리액트, React is Fantastic!

# format에서 사용할 변수 선언
python_kor = '파이썬'
django_kor = '장고'
react_kor = '리액트'

python_eng = 'Python'
django_eng = 'Django'
react_eng = 'React'

# 각 format에 적용
python_format = 'Hello {}, {} is Fantastic!'.format(python_kor, python_eng)
django_format = 'Hello {0}, {1} is Fantastic!'.format(django_kor, django_eng)
react_format = 'Hello {kor}, {eng} is Fantastic!'.format(kor=react_kor, eng=react_eng)

# print로 출력
print(python_format)
print(django_format)
print(react_format)