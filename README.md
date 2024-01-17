Python - 프로그래밍 언어의 일종

컴퓨터와 소통하기 위해 사용하는 언어이며,

소스코드
    - 명령어를 작성해 놓은 것
      개발자와 컴퓨터가 소통할 것을 글로 작성해놓은 것

소스파일
    - 소스코드가 작성되어 있는 파일

컴파일
    - 사람의 언어를 컴퓨터의 언어(0과 1)로 바꿔주는 작업

컴파일러
    - 컴파일 해주는 프로그램 또는 명령어

인터프리터
    - 인터프리트를 해주는 프로그램 또는 명령어

    ※ 파이썬은 인터프리터 안에 컴파일러를 내장하고 있다.
      인터프리터는 매번 소스코드를 한 줄 씩 해석해서 실행하므로(개별 처리),
      전체 프로그램의 퍼포먼스에 큰 손해를 본다.

      파이썬은 소스코드를 바이트 코드로 컴파일한 뒤,
      이를 변역기가 돌려주는 방식으로 실행된다.

      따라서 컴파일 언어인지, 인터프리터 언어인지를 구분하는 것이 아니라
      어떻게 구현하였는지로 판단해야 된다.

프로그램
    - 소스코드로 잘 짜여진 틀


1. 일반 프로그램

    프로그램
    OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할
    하드웨어

    - 일반 프로그램은 이식성이 좋지 않다


2. Python 프로그램

    프로그램
    - PVM: Python 가상 운영체제. Python 프로그램을 OS에 맞게 번역한다
    OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할
    하드웨어

    - Python 프로그램은 이식성이 좋다


콘솔
    - 개발자가 내 컴퓨터(로컬)과 직접 소통할 수 있는 입출력장치(입력: 키보드, 출력: 모니터)

터미널
    - 내 컴퓨터(로컬)뿐만 아니라, 다른 컴퓨터에도 원격으로 접속할 수 있는 콘솔을 구현한 프로그램

쉘
    - 명령어 해석기


* 정리

    1. 개발자가 터미널에 명령어 입력
    2. 쉘이 명령어를 받아 해석 및 수행
    3. 터미널은 쉘에게 받은 결과를 화면에 출력
 
변수 - 저장공간
    변수는 값을 담는 저장공간이다
    x = 10, x라는 이름의 저장공간이 RAM(메모리)에 만들어지고, 10이라는 값이 들어간다

    ※ 여기서의 =(등호)는 대입 연산자로, 오른쪽에 있는 걸 왼쪽에 넣으라는 의미다


자료형(Type) - 저장공간의 종류
    동적 바인딩: 값에 따라 자료형이 정해진다

    자료형(type)       값
    정수(int)       0, 10, -187, ...
    실수(float)       0.0, 10.58, -77.568, ...
    문자열(str)       '0', "0.0", """한동석""", '''Python''', ...
    리스트(list)       [1, 2, 3], [0], [3,], ...
    튜플(tuple)       (1, 2), (), 1, 2, 3, (1,), ...
    딕셔너리(dict)   {key:value,}, ...
    집합(set)       {1, 2, 3}, {1}, ...
    불린(bool)       True, False


변수명 주의사항
    문자로 시작해야 한다.
    특수문자는 사용할 수 없다. 단, _는 허용한다.
    소문자로 시작한다.
    공백을 사용할 수 없다.
    되도록 한글은 사용하지 않는다.
    명사로 사용한다.
    뜻이 있는 단어를 사용한다.
        - a, b, c, d, e, ... (X)
        - data, number, age, name, ...(O)


변수의 선언과 사용

    1. 선언: 대입 연산자가 있다면 선언이다. 값으로 봐서는 안 된다!
    2. 사용: 대입 연산자가 없다면 사용이다. 이 경우, 반드시 값으로 봐야한다.


표기법
    * 파스칼 표기법(클래스명, 오류명)
        대문자로 시작하고, 이어지는 단어의 시작은 대문자로 작성한다
        PascalCase

    카멜 표기법(Java 등에서 사용, 파이썬에서는 안 씀!)
        소문자로 시작하고, 이어지는 단어의 시작은 대문자로 작성한다
        camelCase

    * 스네이크 표기법
        단어 사이에 언더스코어(_)를 작성한다
        snake_case

    케밥 표기법(HTML, CSS, URL 등에서 사용)
        kebab-case

서식문자
    - 따옴표 안에서 변수나 값을 사용해야 할 때 작성한다
    반드시 따옴표 안에서 작성한다

    ------------------------------------
    서식문자 설명
    ------------------------------------
        %d - 10진수 정수
        %f - 실수 표현
        %s - 문자열 표현
    ------------------------------------


변수를 사용하는 이유

    1. 반복되는 값을 쉽게 관리하고자 할 때
    2. 값에 의미를 부여할 때 (자료구조)


알고리즘과 자료구조

    1. 알고리즘이란, 문제가 발생했을 떄 해결할 수 있는 절차

        예) 3과 1을 더해서 결과를 출력하시오.
            1. 두 정수를 담을 변수 선언
            2. 두 정수의 합을 담을 변수 선언
            3. 형식에 맞게 작성할 문자열 값을 담을 변수 선언
            4. 형식 출력

    2. 자료구조란, 의미 없는 값을 하나의 정보로 변환하고, 이는 저장 공간의 종류를 의미한다.

        예) 3개의 정수가 있을 때, 이를 빠르게 가져오는 서비스를 제작해야 한다.
            빠르게 가져올 때는 list에 담아주는 것이 효과적이다.


형변환
    - bin(), oct(), hex(), int(), float(), str(), bool()


연산자 - 기능이 있는 특수문자

    1. 산술 연산자

        ----------------------------------
        연산자   예시   설명
        ----------------------------------
        +       3 + 5   더하기
        -       3 - 5   빼기
        *       3 * 5   곱하기
        /       3 / 5   나누기
        **       3 ** 5   제곱
        //       3 // 5   몫
        %       3 % 5   나머지
        ----------------------------------


    2. 대입(allocation) 연산자

        -------------------------------------------
        연산자   예시           설명
        -------------------------------------------
        =       data = 10       좌항에 우항을 대입
        +=       data += 10       data = data + 10
        -=       data -= 10       data = data - 10
        *=       data *= 10       data = data * 10
        /=       data /= 10       data = data / 10
        **=       data **= 10       data = data ** 10
        //=       data //= 10       data = data // 10
        -------------------------------------------

    3. 비교 연산자

        ※ 조건식 - 참 또는 거짓, 둘 중 하나가 나오는 식
        ※ 조건식은 항상 값으로 본다(True 또는 False)

        ----------------------------------------------------------------
        연산자   예시                   설명
        ----------------------------------------------------------------
        ==       data == 10               같으면 True, 같지 않으면 False
        !=, <>   data != 10, data <> 10   같지 않으면 True, 같으면 False
        >       3 > 5                   보다 크다
        <       3 < 5                   보다 작다
        >=       3 >= 5                   이상
        <=       3 <= 5                   이하
        ----------------------------------------------------------------

    4. 논리 연산자

        ----------------------------------------------------------------
        연산자   예시               설명
        ----------------------------------------------------------------
        and       a == b and c == d   조건식 둘 다 True일 경우 True
        or       a == b or c == d   조건식 둘 중 하나라도 True일 경우 True
        not       not (a == b)       True를 False로 False를 True로 변경
        ----------------------------------------------------------------

    5. 멤버 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                   설명
        -----------------------------------------------------------------------------------------------------
        in       "a" in "abc", 2 in [1, 2, 3]           좌항이 우항에 포함되었다면 True 아니면 False
        not in   "a" not in "abc", 2 not in [1, 2, 3]   좌항이 우항에 포함되어 있지 않다면 True 포함되면 False
        -----------------------------------------------------------------------------------------------------

    6. 식별 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                       설명
        -----------------------------------------------------------------------------------------------------
        is       a = 10; b = a; a is b                       두 객체 모두 같은 주소일 경우 True 아니면 False
        is not   a = [1, 2, 3]; b = [1, 2, 3]; a is not b   두 객체 모두 같은 주소일 경우 True 아니면 False
        -----------------------------------------------------------------------------------------------------


제어문
    컴파일러의 방향을(위->아래, 좌->우 가 기본) 제어할 수 있는 문법으로,
    건너뛰기, 되돌아가기 등이 있다


조건문
    if문

        1. 모든 if 조건식을 검사.
        이전 if문의 결과가 어떻게 되든 상관 없이 다음 if문 실행.

            if 조건식:
                실행할 문장
            if 조건식:
                실행할 문장
            if 조건식:
                실행할 문장
            ...

        2. if 조건식이 거짓이라면 아래의 elif 조건식 검사.
            if 조건식이 참이라면 아래의 문장 싹 다 무시.

            if 조건식:
                실행할 문장
            elif 조건식:
                실행할 문장
            ...
            else:
                실행할 문장

반복문
    for문

        반복 횟수가 명확할 떄 사용한다.
        다른 언어의 for 문이랑 형식 다르니 주의!

        for 변수명 in range(inclusive_start, exclusive_end, step):
            실행할 문장

        -> in절 뒤의 요소를 순서대로 변수에 담고, 다음 값이 더 이상 없을 경우 종료


    while문

        조건식이 True일 때 동안 반복하고, False일 때 탈출한다.
        반복 횟수가 얼마나 될지 모를 때 사용한다.

            while 조건식:
                실행할 문장


list
    여러 개의 저장공간이 나열되어 있는 것
        -> 데이터가 들어 있는 칸(데이터 하나 = 저장공간 하나)이 '여러 개' 나열되어 있는 형태


        list명 = [값1, 값2, ...] 같은 형태로 list 생성 시,
        RAM에서 list명이라는 이름의 공간 하나와
        그와 별개로 해당 list의 값이 들어 있는 칸들(데이터 당 하나)이 일렬로 생성된다.

        여기서 'list명'은 기본적으로 list의 0번 인덱스의 주소를 참조하며,
        이는 *list명(0) 으로 나타낼 수 있다.
        파이썬은 C언어 기반이므로, *는 주소 값을 의미한다.

        다른 인덱스의 주소를 참고하고 싶다면 *list명(0 + i)의 형태로 쓸 수 있다.

        유의할 점은, 각 칸 별로 다른 주소값이 생성되기 때문에,
        주소값이 저장되어 있는 칸도 해당 데이터 수만큼 생성된다는 것이다.

        하지만, 여기서 * (+ i)를 축약할 수 있는데,
        바로 *list명(0 + i) 를 list명[i] 형식으로
        대괄호를 사용하는 것이다.

        데이터의 흐름을 파악하도록 하자.


    사용 목적
        1. 여러 번 선언하지 않고 한 번만 선언하기 위해서 사용
        2. 규칙성 없는 칸에 규칙성을 부여하기 위해서 사용


list 선언 방식
    1. list명 = [값1, 값2, ...]
        -> 어떤 값을 넣어야 할 지 알고 있을 때

    2. list명 = [값] * 칸 수
        -> 어떤 값을 넣어야 할 지 모르지만, 몇 칸이 필요한 지는 알 때

    3. list명 = [] * 칸 수
        -> 어떤 값을 넣을 지도, 몇 칸이 필요한 지도 모를 때

    4. list명 = list(range(start, end, step))
        -> range 타입으로 생성 후, list 타입으로 형 변환


list의 길이
    len(list명)
        -> 해당 list의 길이


list의 사용
    data_list = [1, 2, 3]

    - 값 넣기

        - 추가
            list명.append(값)

                ex) data_list.append(4) -> [1, 2, 3, 4]
                    -> 기존 list를 복사한 다음, 해당 값을 복사한 list의 맨 마지막에 붙임
                        복사 이전의 list는 메모리에서 삭제.
                        쓸 때마다 복사/삭제가 이루어지기 때문에, 자주 쓰면 성능이 떨어질 수 있음


        - 삽입
            list명.insert(인덱스 번호, 값)

                ex) data_list.insert(1, 1.5) -> [1, 1.5, 2, 3, 4]
                    -> 해당 인덱스에 값을 추가하고,
                        기존에 해당 인덱스에 있던 값과 그 뒤쪽 칸의 값들은 한 칸씩 오른쪽으로 밀림


    - 값 삭제
        list명.remove(값)
            - 값 중복 시 먼저 나온(인덱스 번호가 낮은) 값이 삭제

        del(list명[인덱스 번호])
        del list명[인덱스 번호]
            - 해당 인덱스에 있는 값 삭제

        list명.clear
            - 해당 list의 모든 값 삭제


    - 값 검색
        list명.index(값)
            해당 값이 들어있는 저장공간의 인덱스 번호를 검색
            값이 중복된다면, 먼저 나온(인덱스 번호가 낮은)값의 번호를 반환


    - 값 수정
        list명[인덱스 번호] = 새로운 값
            해당 인덱스에 새로운 값 할당


dict

    dictionary - 사전

    사전이 단어 - 뜻이 한 쌍을 이루어 표기하듯이,
    데이터를 한 쌍으로 저장하여 관리한다.

    len()을 사용하면 데이터 한 쌍을 1로 취급한다.

    키 값(list의 인덱스 번호 같은 것)은 중복될 수 없지만,
    그 키 내부의 값(value)은 중복이 가능하다.

    키를 주면 그 키에 해당하는 값을 가지고 온다.

    키(set)와 값(순서가 있는 자료구조의 일종)의 자료구조는 다름.
    따라서, dict는 두 가지 자료구조가 서로 연결된 형태다.


dict 선언

    dict명 = {키: 값, 키: 값, ... }


dict 사용

    - 추가, 수정

        dict명[키] = 값

            해당 키가 기존에 있었다면 수정,
            없었다면 추가가 된다.

    - 삭제

        del dict명[키]


    - 검사
        키 in dict명: 해당 키가 있으면 True
        키 not in dict명: 해당 키가 없으면 True

.json() 형식의 파일은 내부 데이터가 dict 타입.
json은 서버와의 통신을 주고받을 때 사용되는 파일인 만큼,
dict 타입에 대해 아는 만큼 통신에 대해 배울 때 수월해진다.


list: 각 데이터 칸마다 인덱스라는 고유 번호가 있고,
      각 칸에 데이터가 하나씩 들어있음

tuple: 순서를 변경할 수 없음

set: 정해진 순서가 없고, 이에 따른 검색도 불가

dict: 키-값이 한 쌍으로 들어있음


함수 - 이름 뒤에 소괄호()
      * 작성된 코드의 주소값을 담고 있는 저장공간

    f(x) = 2x+1
        -> 수학에서 보던 유형의 함수
            이 함수의 이름은, 소괄호 앞에 있는 'f'


    f           (x)        =      2x+1
    함수명      매개변수             리턴값

    - 매개변수: 외부의 값과 내부의 로직을 연결(매개체)


함수 선언

    def 함수명 (매개변수, ...):
        실행할 문장
        return 리턴값

        - 파이썬에서의 함수 선언은 앞에 무조건 'def'가 붙음


함수 사용

    함수명 (값1, ...)

        - 앞에 'def'가 없으면 사용


함수를 쓰는 이유

    1. 재사용
        반복되는 로직이 있을 떼, 그 부분을 함수로 빼놓고 원할 때마다 호출할 수 있음.
        * 단, 절대 특정성을 부여해서는 안 된다.

    2. 간결화


함수 선언 순서
    문제) 두 정수를 더하는 함수 구현

    1. 함수명을 생각한다.
        def add():

    2. 매개변수를 생각한다.
        def add(number1, number2):

    3. 실행할 문장을 생각한다.
        def add(number1, number2):
            result = number1 + number2

    4. 리턴값을 생각한다.
        def add(number1, number2):
            result = number1 + number2
            return result


매개변수 선언 방법
    1. packing(args)
        여러 개의 값을 마구잡이로 잡을 때 사용한다

    2. kwargs
        여러 개의 값을 key=value 형식으로 받는다

    3. 언패킹
        함수의 매개변수 칸이 *로 시작하면, kwargs 형식과 동일하게 받아야 하고,
        매개변수만 나열되어 있으면 값만 전달해도 된다.


packing(args) 함수 사용 방법
    1. 여러 개의 값을 콤마(,)로 구분해서 전달
    2. 여러 개의 값을 묶은 뒤, 앞에 *을 작성해서 전달

kwargs 함수 사용 방법
    1. 여러 개의 값을 콤마로 구분해서, key=value 형식으로 전달
    2. dict 형식으로 정보를 담은 뒤 앞에 **을 붙여서 전달


클로저(closure, 폐쇄): 함수 안에 함수, 모듈화
    close(닫다)에서 파생된 단어

    함수가 정의된 시점에서 변수를 기억하고,
    이 변수를 나중에 참조 또는 변경이 가능하도록 해준다.

    내부 영역에 선언된 변수는 외부에서 접근이 불가능하기 때문에 데이터 은닉을 할 수 있으며,
    함수가 종료된 이후에도 지역변수에 접근할 수 있기 때문에 데이터 지속성도 가지고 있다.

        -> 지역변수처럼 밖에서 볼 수는 없지만,
            전역변수처럼 메모리에 남기 때문에 계속 호출해서 쓸 수 있다?


    또한, 다른 함수를 인자로 받거나 리턴할 수 있는 함수형 프로그래밍이 가능해진다.

        -> 함수 안에 함수가 있는 코드가 있다고 생각해봅시다.

            바깥쪽에 해당하는 함수를 사용하면, 그 리턴으로 안쪽 함수가 나온다고 가정.

            그러면 그 아랫줄부터 바깥쪽 함수에 대한 값을 사용할 수 있을 것이고,
            이 때, 안쪽 함수에 대한 것도 사용이 가능해지는 것.
            안쪽 함수만 따로 불러서 쓸 수도 있고.

            but, 바깥쪽 함수를 아직 쓰지도 않았는데 안쪽 함수만 따로 불러서 쓰는 건 당연히 안 됨.


    하지만 코드 복잡성이 증가하고, 지역변수에 대한 정보가 메모리에 남기 때문에
    메모리 사용량이 늘어날 수 있다.


클로저 구현 코드

    def out(arg):
        local_variable = 값

        def inner(arg):
            # read local_variable   -> inner 함수 밖의 값을 읽어올 수 있다는 의미
            value = 암거나 연산

            return value    -> 없을 수도 있음

        return inner    -> inner() 함수를 리턴했고, 이 함수를 값처럼 쓸 수 있음


* 앞으로의 과정
Git(기초), Github

DBMS  

파이썬 - DBMS 연동  

HTML  

CSS  

클론 코딩  

Javascript  

클론 코딩  

파이썬 웹 개발(Django 프레임워크)  

데이터 분석 in 파이썬(numpy, pandas 라이브러리)  

머신러닝(분류, 회귀, 군집)  

딥러닝(이미지, 영상 분석)  


- 데코레이터(장식)

    좋은 개발 환경에서는 개발자가 메인 로직(비즈니스 로직)에만 집중할 수 있게 한다.

    보안이나 로그, 트랜잭션, 예외 처리와 같이 비즈니스 로직은 아니지만,
    반드시 처리가 필요한 부분을 '주변 로직' 이라고 한다.

    주변 로직을 다른 함수에 분리시킨 뒤,
    메인 로직이 실행될 때 같이 실행되게 할 수 있다.


- 데코레이터 동작 코드

    1.
        def 데코레이터 이름(원래 함수):

            def 주변 로직 함수(원래 함수의 매개변수):

                완성 코드 = 주변 로직

                원래 함수(완성 코드)

            return 주변 로직 함수


    2.
        def 데코레이터 이름(원래 함수):

            def 주변 로직 함수(원래 함수의 매개변수):

                주변 로직

                원래 함수(원래 함수의 매개변수)

            return 주변 로직 함수


- 클래스(class, 반)
    공통 요소를 딱 한 번만 선언 -> 이게 목적

    1. 타입이다 = 기존에 쓰던 int, str 같은 것
        클래스 안에 선언된 변수와 메소드(함수)를 쓰고 싶다면,
        해당 클래스 타입으로 변수를 선언해야 한다.

    2. 주어다
        ex) 원숭이가 바나나를 먹는다.
            -> 여기서의 주어는 '원숭이'

        - Monkey.eat("바나나")
            -> 클래스 이름은 무조건 대문자로 시작한다.


- 클래스 선언 방식

    class 클래스명:
        필드(변수, 메소드) - 클래스 안에 있는 모든 것들의 총칭


- 클래스의 필드를 사용하는 방법
    1. 객체화(instance)
        추상적인 개념을 구체화하는 작업
        객체(instance variable)를 만드는 작업

        ex) 도형 - 추상적 개념
            세모 - 구체적 개념
            -> '도형' 이라는 추상적 개념에서
                '세모' 라는 구체적인 개념을 여러 가지 고유 특징을 통해 구체화

    2.

- 생성자
    클래스 이름 뒤에 소괄호가 있는 형태
    메소드와 기능은 쪽같지만, 엄밀히 따지면 메소드가 아님.

    메소드랑 다 똑같은데, 딱 한 가지가 다르기 때문.
    바로 return 기능이 없다는 것.

    생성자는 할당한 필드의 주소를 자동으로 리턴하기 때문에
    선언할 때 리턴 기능을 사용할 수 없다.

- 기본 생성자
    매개변수가 없는 생성자
    클래스 선언 시 자동으로 선언됨.

    만약 사용자가 직접 생성자를 선언하게 되면, 기본 생성자가 자동 생성되지 않는다


- self
    필드에 접근한 객체가 누구인지 알아야, 해당 객체의 필드에 접근할 수 있다.
    이 때, 접근한 객체가 가지고 있는 필드의 '주소값'이 self 라는 변수에 자동으로 담긴다.


- 상속(inheritance)
    1. 기존에 선언된 클래스의 필드를, 새롭게 만들 클래스의 필드로 사용하려고 할 때
    2. 여러 클래스를 선언하면서 공통되는 필드가 있을 경우,
        부모 클래스를 선언한 뒤 겹치는 필드를 구성하고, 각 자식 클래스에 상속해준다(추상화)

- 상속 문법
    class A:
        A 필드

    class B(A):
        A + B 필드


    A: 부모 클래스, 상위 클래스, 슈퍼 클래스, 기반 클래스
    B: 자식 클래스, 하위 클래스, 서브 클래스, 파생 클래스

- super().__init__() - 부모 생성자
    자식 객체로 부모 필드에 접근할 수 있다
    하지만 개발자가 직접 호출하는 것은 자식 생성자 뿐이기 때문에, 자식 생성자만 메모리에 할당된다고 생각할 수 있음

    사실 자식 생성자는 위 메소드(super().__init__())로 항상 부모 생성자를 먼저 호출하기 때문에,
    자식 생성자를 호출하면 부모와 자식이 모두 메모리에 할당된다.

    super().__init__() 을 직접 작성하지 않더라도, 컴파일러가 알아서 넣어준다.


- 오버라이딩(재정의, 무시)
    부모 필드에서 선언한 메소드를 자식 필드에서 수정하려면, 재정의를 해야된다.
    이는 자식에서 부모 필드의 메소드를 같은 이름으로 선언하는 문법을 의미한다.


- 종합 실습 -

    은행 - 예금주, 계좌번호(중복 x), 핸드폰 번호(중복 없음), 비밀번호, 통장잔고

    신한 - 입금 시 수수료 50%

    국민 - 출금 시 수수료 50%

    카카오 - 잔액조회 재산 반토막

    은행은 3개를 선언한다.
    모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
    모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
    화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.


- 매직 메소드
    클래스 안에 '재정의' 할 수 있는 스페셜 메소드


연산자     메소드                         설명
───────────────────────────────────────────────────────
 +      __add__(self, other)            덧셈

 *      __mul__(self, other)            곱셈

 -      __sub__(self, other)            뺄셈

 /      __truediv__(self, other)        나눗셈

 //     __floordiv__(self, other)       몫

 %       __mod__(self, other)           나머지

 **      __pow__(self, other[, modulo]) 제곱

 >>      __lshift__(self, other)        우쉬프트

 <<      __rshift__(self, other)        좌쉬프트

 &       __and__(self, other)           논리곱

 ^      __xor__(self, other)            배타논리합

 |      __or__(self, other)             논리합

+=      __iadd__(self, other)           누적 더하기

-=      __isub__(self, other)           누적 빼기

*=      __imul__(self, other)           누적 곱하기

/=      __idiv__(self, other)           누적 나누기

//=     __ifloordiv__(self, other)      누적 몫

%=      __imod__(self, other)           누적 나머지

**=     __ipow__(self, other)           누적 제곱

>>=     __irshift__(self, other)        누적 우쉬프트

<<=     __ilshift__(self, other)        누적 좌쉬프트

&=      __iand__(self, other)           누적 논리합

^=      __ixor__(self, other)           누적 배타논리합

|=      __ior__(self, other)            누적 논리합

 <      __lt__(self, other)             작다(미만)

 <=     __le__(self, other)             작거나 같다(이하)

 ==     __eq__(self, other)             같다

 !=     __ne__(self, other)             같지 않다

 >      __gt__(self, other)             크다(초과)

 >=     __ge__(self, other)             크거나 같다(이상)

 [i]    __getitem__(self, index)        인덱스 연산자

 in     __contains__(self, value)       멤버 확인

 len    __len__(self)                   요소 길이

 str    __str__(self)                   문자열 표현

        __init__                       생성자
        
	      __del__                        소멸자

        __new__                        할당자

        __repr__(self)              __str__을 정의하지 않을 경우, __repr__이 대신 쓰인다, 객체를 표현(객체의 주소)하는 목적으로 사용한다


- 모듈(부품) -
    변수, 함수, 클래스 등을 모아놓은 파이썬 파일


- 모듈 사용 -
    import [모듈명]
        사용할 함수의 소속을 직접 코드에 작성하고, 모든 필드를 사용하고자 할 때

    import [모듈명] as [사용할 이름]
        모듈명이 길거나 복잡할 때, 원하는 이름으로 설정해서 사용

    from [모듈명] import [필드명, ...]
        모듈명을 직접 코드에 작성하지 않고, 필드를 바로 사용하고자 할 때

    from [모듈명] import *
        모듈 안에 있는 모든 필드(*)를 바로 사용하고자 할 때

    - 실제 사용할 때 대괄호는 쓰는 거 아님!
    - 항상 결론은 import 다


- 패키지 -
    폴더를 생성해서 .py 또는 .ipynb 파일을 관리하고자 할 때, 해당 폴더를 패키지라고 함

    __init__.py 파일을 생성해야 패키지로 인식되지만,
    상위 버전(3.3 이상)에서는 __init__.py 없이도 패키지로 인식된다.

    하지만, 3.3 미만의 하위 버전에서는 패키지로 인식되기 위해 직접 생성해놓는 것이 좋다.


- API(Application Programming Interface) -
    선배 개발자들이 미리 작성해놓은 틀(소스 코드)

    1. 내부 API
        파이썬 설치 시 다운로드 된 모듈
        바로 사용할 수 있는 API

    2. 외부 API
        해당 기업에서 배포한 코드를 다운로드 받은 뒤에 사용할 수 있는 모듈
        기본으로 제공되지 않는 API


* 주의 사항 *
    모듈을 사용할 파일의 이름이 모듈과 같으면 절대 못 쓴다


- 예외 처리 -
    프로그램 실행 중 오류 발생 시 강제 종료되기 때문에
    이를 막기 위해서 예외 처리를 작성한다.

    제어문으로 오류를 막을 수 없다면 반드시 예외 처리를 작성해야 한다.


- try, except -

    1.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류 as 오류객체:        -> '오류객체' 라는 건, 여기서 발생한 오류는 '클래스' 라는 의미다.
            오류 발생 시 실행할 문장

        ...


    2.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류:              -> 객체의 주소가 어딘가에 담겨있지만, 그 안을 확인할 필요가 없을 때
            오류 발생 시 실행할 문장

        ...


    3.
        try:
            오류가 발생할 수 있는 문장

        except:                     -> 어떤 유형(클래스)의 오류가 발생하더라도 여기에 들어온다.
            오류 발생 시 실행할 문장

        ...

        finally:
            오류 발생 여부와 관계없이 실행       -> 에러를 잡아도 실행되고,
                                               에러가 떠서 강제종료 되더라도 실행된다.


- 예외 발생시키기 -
    목적 1. 심각한 오류가 발생하기 전, 일부러 프로그램을 강제종료 시킬 때
    목적 2. 예외를 한 곳에 묶어서 처리하기 위해(상위 과정에서 다룰 예정)

    raise 발생오류


- 예외 만들기 -
    class 오류명(Exception):
        def __str__(self):
            return "오류 메세지"



- 파일 -
    외부에 파일을 생성하거나 내용을 작성할 수 있으며,
    기존의 내용도 읽어올 수 있다.

- 파일 생성 -
    파일을 열고 작성할 때 사용
    'w'를 작성해서 운정체제에게 파일을 여는 목적(write)을 알려줘야 된다

    open(path, 'w')     -> 열린 파일 객체


- 내용 추가 -
    기존의 내용을 없애지 않고, 그 이래에 내용을 추가한다
    이 때, 추가(add) 모드라는 뜻의 'a'를 사용한다

    open(path, 'a')


- 파일 읽기 -
    기존 네용을 한 줄씩 읽어올 때 'r'을 사용해서 읽기(read) 모드로 파일을 열어준다
    open(path, 'r')


- 제너레이터 -
    한 번에 하나씩 구성요소를 반환해주는 객체
    대용량 데이터 및 많은 반복이 필요한 코드에서도 메모리를 적게 쓰게 해주는 고성능 방법
    필요할 때마다 하나씩 가져오기 때문에, 무거운 객체를 다룰 때 사용한다.


- 기존의 list comprehension -
    [결과값 for 변수 in range(끝값)]


- 제너레이터 사용 예시 -
    (결과값 for 변수 in range(끝값))


버전 관리 시스템

	원하는 시스템(버전)으로 이동할 수 있으며,
	각 버전별로 여러 개발자가 협업할 수 있는 최적의 환경을 제공하는 시스템


SVN

	작업 내역 커밋 시 변경사항과 히스토리가 서버로 즉시 전송되기 때문에 관리가 용이함
	또한, 간단한 설치와 사용방법으로 별도의 교육 없읻 초보자도 쉽게 사용할 수 있다.
	
	하지만, 항상 원격 저장소(SVN 서버)를 필요로 하며, 서버 간 버전 관리도 힘들다.


Git - 분산형 버전 관리 시스템

	SVN이 가지고 있던 클라이언트-서버 간 버전 관리 문제를 보완한 시스템
	
	서버 뿐만 아니라, 로컬에서도 버전 관리 가능
	로컬이 서버가 될 수도 있고, 반대로 서버가 로컬이 될 수도 있다.
	
	브랜치라는 개념을 사용하여 개발자 마음대로 로컬 환경에서도 커밋과 버전 관리가 가능하다.


------------------------------------------------------------------------------------------------------------------------------------------------------


git init									- 해당 파일에 git 실행

git add .									- 해당 파일에 있는 모든 내용(.)을 로컬 서버에 올림

git status									- 현재 git 상태(로컬 서버에 올라간 내역 등) 확인

git commit -m "메세지"						- add 로 올린 내역 커밋 실행

git log --pretty=oneline						- git log를 한 줄로 이쁘게 출력

git checkout [커밋명 또는 브랜치명]				- 해당 커밋 시점/브랜치로 이동. 커밋명은 앞에서부터 7자리 입력

git checkout -b [브랜치명]						- 해당 [브랜치명]을 새로운 브랜치로 생성하고, 그 브랜치로 이동

git branch									- 현재 브랜치 목록 확인

git branch -d [브랜치명]						- [브랜치명] 브랜치 삭제

git merge [브랜치명]							- 현재 브랜치에 [브랜치명] 브랜치 내용을 가져와서 병합

git remote add [원격 저장소 이름] [서버 경로]

git remote -v

git remote remove [원격 저장소 이름]

git push [원격 저장소 이름] [원격 저장소 브랜치명]


------------------------------------------------------------------------------------------------------------------------------------------------------


- DB (데이터 베이스) -

데이터가 모여있는 기지(base)
데이터 베이스 자체는 추상적인 개념


- DBMS (Database Management System) -

데이터 베이스를 관리할 수 있는 구체적인 시스템
오라클, MySQL, MariaDB, MS-SQL, Mongo-DB 등...


- MySQL -

 웹 사이트와 다양한 앱에서 사용되는 DBMS

오라클은 관리 비용이 비싸지만, MySQL은 관리 비용이 저렴함
문법이 간결하고 쉬우며, 메모리 사용량이 현저히 낮아서 부담없아 사용 가능


- DBMS 소통 방식 -

--------------------------------------------------------------------------
        			    사용자
--------------------------------------------------------------------------
  	     ↕              				  ↕
고객 관리 응용프로그램      ↕     주문 관리 응용프로그램
   	     ↕               				  ↕
--------------------------------------------------------------------------
         			    DBMS
--------------------------------------------------------------------------




- RDBMS (관계형 DBMS) -

테이블끼리 서로 관계를 맺음

ex)

   Table A (TBL_USER)               			Table B (TBL_ORDER)
   번호(PK)   이름   나이   아이디(UK)         	주문번호(PK)      번호(FK)  	    날짜        	상품수량
   1   		이기영   20   lky1234         		20240114001     	   2   	  	20240114      	   5
   2   		장상화   21   jsh5555         		20240114002     	   2        	20240114      	   20
   3   		조은종   22   jej9999          		20240114003     	   1       	20240114      	   100
   4   		서경덕   45   sgd7777        		20240115001     	   4        	20240115     	   1
   5   		문우람   78   mor4444       		20240115002    	   3        	20240115      	   45
 

이러한 구조를 가지는 것을 Table 이라고 부른다.


- COLUMN (열, 속성, 필드)
공통된 값들의 주제

- ROW (행, 레코드, 튜플)
하나의 정보

- PK (Primary Key)
고유한 값, 테이블 당 하나씩만 존재
각 정보의 구분점으로 사용된다.
값의 중복이 없고, NULL(파이썬에서의 None) 값을 허용하지 않는다.

- FK (Foreign Key)
다른 테이블에서의 PK를 의미
보통 테이블끼리의 관계를 맺을 때 사용한다.
값의 중복이 가능하고, NULL도 허용한다.

- UK (Unique Key)
NULL은 허용하지만, 중복은 허용하지 않음


- SQL문 (쿼리문) -

스크립트 언어 (인터프리터 언어)
DBMS와 소통하는 언어
DDL, DML, DCL, TCL 이 있다.


- MySQL 기본 세팅 -

1) 로그인
	> mysql -u root -p
	> 12345678 (root 계정)
	
	> mysql -u mysql -p
	> 1234 (mysql 계정)

2) 기본 DB 선택
	> use mysql;

3) 로컬에서만 접근 가능한 계정 생성
	> create user 'userid'@localhost identified by '비밀번호';


4) 원격으로도 접근 가능한 계정 생성
	> create user 'userid'@'%' identified by '비밀번호';

5) DB 생성
	> create database [데이터베이스 이름];

6) DB 사용
	> use [데이터베이스 이름];

7) DB 삭제
	> drop database [데이터베이스 이름];

8) 사용자 비밀번호 변경
	> set password for 'userid'@'%' = '새로운 비밀번호';

9) 사용자 삭제
	> drop user 'userid'@'%';

10) 연결 권한
	> grant all privileges on *.* to 'userid'@'%' with grant option;

11) 권한 관련 명령어 확정
	> flush privileges;


- 자료형 -

   - 정수
      tinyint
      smallint
      mediumint
      int
      bigint

   - 실수
      decimal(m, d) : m자리 정수, d자리 소수점으로 표현

   - 날짜
      date : 1000-01-01 ~ 9999-12-31(3byte)
      time : -838:59:59 ~ 838:59:59(3byte)
      datetime : 1000-01-01 00:00:00 ~ 9999-12-31 23:59:59(8byte)

   - 문자
      char(m) : 고정 길이 문자열(0~255)
      varchar(m) : 가변 길이 문자열(0~65535)

   - boolean
	MySQL에서는 tinyint를 쓰는 것이 가장 좋다.
	bit(1) 로 설정해도 어차피 데이터는 byte 단위로 저장되고,
	bool이나 boolean으로 설덩해도 어차피 tinyint로 변경된다.
	
	만약 값에 의미부여를 하고 싶다면, varchar로 설정한 뒤,
	check 제약조건으로 이상 데이터의 삽입을 막아준다.

	enum을 사용하면 정규화를 위반하게 되며, 설정해놓은 데이터의 수집이 어렵고,
	다른 DBMS로 이관 할 경우, MySQL에만 존재하는 enum을 모두 다른 타입으로 변경해야 한다.

	만약 enum을 사용하고 싶다면, 정규화 위반이 가능하도록 약속되었고, 유일하고, 변하지 않는 값이며,
	값이 2~10개인 경우에만 사용한다.
	


- DDL (데이터 정의어) -

테이블을 조작하거나 제어할 수 있는 쿼리문

	1. create: 테이블 생성
		create table [테이블명] ([컬럼명] [자료형(용량)] [제약조건], ...);

	2. drop: 테이블 자체를 삭제
		drop table [테이블명];

	3. alter: 테이블 수정
		종류가 매우 많으니 구글링해서 사용

	4. truncate: 테이블 내용만 전체 삭제
		truncate table [테이블명];

=====================================================================================


- 무결성 -

	데이터의 정확성, 일관성, 유효성이 유지되는 것

	정확성: 데이터는 애매하지 않아야 한다.
	일관성: 각 사용자가 일관된 데이터를 볼 수 있어야 한다.
	유효성: 실제로 존재하는 데이터여야 한다.

	1. 개체 무결성: 모든 테이블은 PK로 선택된 컬럼을 가져야 한다.
	2. 참조 무결성: 두 테이블의 데이터가 항상 일관된 값을 가지도록 유지한다.
	3. 도메인 무결성: 컬럼의 타입, NULL 값의 허용 등에 대한 사항을 정의하고, 올바른 데이터가 입력되었는지 확인하는 것


=====================================================================================


- 모델링 (기획) -

추상적인 주제를 DB에 맞게 설계하는 것

1. 요구사항 분석

	회원, 주문, 상품 - 이 3가지를 관리하려 한다고 가정


2. 개념적 설계

	회원			주문			상품
	----------------------------------------------	
	번호			번호			번호
	----------------------------------------------
	아이디		날짜			이름
	비밀번호		회원번호		가격
	이름			상품번호		재고
	주소
	이메일
	생일


3. 논리적 설계

	회원				주문				상품
	-----------------------------------------------------------------	
	번호(PK)			번호(PK)			번호(PK)
	-----------------------------------------------------------------
	아이디(U, NN)		날짜(NN)			이름(NN)
	비밀번호(NN)		회원번호(FK, NN)		가격(default=0)
	이름(NN)			상품번호(FK, NN)		재고(default=0)
	주소(NN)
	이메일
	생일


4. 물리적 설계 (물리 모델링)
	
	tbl_user
	--------------------------------------------
	id: bigint primary key
	--------------------------------------------
	user_id: varchar(255) unique not null
	password: varchar(255) not null
	name: varchar(255) not null
	address: varchar(255) not null
	email: varchar(255) not null
	birthday: date
	--------------------------------------------
	 

5. 구현
	

=====================================================================================


- 정규화 -

삽입, 수정, 삭제의 이상현상을 제거하기 위한 작업,
데이터 중복을 최소화하는 데 목적을 두고 있다.
5차 정규화까지 있으나, 실무에서는 3차 정규화까지 진행한다.


- 1차 정규화

	같은 성격과 내용의 컬럼이 연속적으로 나타나거나,
	하나의 컬럼에 여러 값이 연속적으로 나타날 경우

	상품명
   	와이셔츠1, 와이셔츠2, 와이셔츠3

   	상품명1   상품명2   상품명3
   	와이셔츠1   와이셔츠2   와이셔츠3

   	* 조회가 힘들다.


   	▶ 1차 정규화 진행
   
      		상품명
      		와이셔츠1
      		와이셔츠2
      		와이셔츠3


- 2차 정규화

	조합키(복합키)로 구성되었을 때, 조합키의 일부분에만 종속되는 속성이 있는 경우(부분 종속)

	꽃
   	이름   	색상   	꽃말   	과
   	해바라기    노란색   	행운   	국화
   	장미   	빨간색   	사랑   	장미

   	"과" 속성(컬럼)은 부분종속이다.


   	▶ 2차 정규화 진행
   
      		꽃
      		이름   	색상   	꽃말
      		해바라기    노란색   	행운
      		장미   	빨간색   	사랑

      		과
      		이름   	과
      		해바라기   국화
      		장미   	장미


- 3차 정규화

	PK가 아닌 컬럼이 다른 컬럼을 결정하는 경우, 이행함수의 종속(종속이 2번 생기는 경우)을 제거

	회원번호   	이름   	시   		구   		동	   	우편번호
   	1   		한동석   	경기도   	남양주   	화도   	12345
   	2   		홍길동   	서울   	강남   	역삼   	56466

   * 우편번호로 시, 구, 동을 알 수 있다.
   * 중복된 데이터가 생길 가능성이 있다.

   
   ▶ 3차 정규화 진행

      회원번호   	이름   	우편번호
      1   		한동석   	12345
      2   		홍길동   	56466

      우편번호   	시   		구   		동
      12345   	경기도   	남양주   	화도
      56466   	서울   	강남   	역삼

- 데이터베이스에서 정규화가 필요한 이유 -

데이터베이스를 잘못 설계하면 불필요한 데이터 중복으로 인해 공간이 낭비된다.
이런 현상을 이상(Anomaly)현상이라고 한다.

회원번호와 프로젝트코드 두 컬럼의 조합키로 설정되어 있는 테이블이고
한 사람은 하나의 부서만 가질 수 있다.

   회원번호      이름   	부서   	프로젝트코드   	급여   부서별 명수
   22080101   한동석   개발팀   	ABC0001      	3000   4
   22080101   한동석   개발팀   	DEF1112      	2000   4
   22080101   한동석   개발팀   	CBA9474      	4000   4
   22080104   홍길동   기획팀   	EFG0881      	5000   2
   22081106   이순신   디자인팀   	GHI9991      	6000   3


- 이상 현상의 종류 -

- 삽입 이상

      새 데이터를 삽입하기 위해 불필요한 데이터도 삽입해야하는 문제
   
      담당 프로젝트가 정해지지 않은 사원이 있다면,
      프로젝트 코드에 NULL을 작성할 수 없으므로 이 사원은 테이블에 추가될 수 없다.
      따라서 '미정'이라는 프로젝트 코드를 따로 만들어서 삽입해야 한다.


- 갱신 이상

      중복 행 중에서 일부만 변경하여 데이터가 불일치하게 되는 모순의 문제

      한 명의 사원은 반드시 하나의 부서에만 속할 수 있다.
      만약 "한동석"이 보안팀으로 부서를 옮길 시 3개 모두 갱신해주지 않는다면
      개발팀인지 보안팀인지 알 수 없다.


- 삭제 이상

      행을 삭제하면 꼭 필요한 데이터까지 함께 삭제되는 문제
   
      "이순신"이 담당한 프로젝트를 박살내서 드랍된다면 "이순신" 행을 모두 삭제하게 된다.
      따라서 프로젝트에서 드랍되면 정보를 모두 드랍하게 된다.


	▶ 2차 정규화

      		회원번호      	프로젝트코드   	급여
      		22080101   	ABC0001      	3000
      		22080101   	DEF1112      	2000
      		22080101   	CBA9474      	4000
      		22080104   	EFG0881      	5000
      		22081106   	GHI9991      	6000


      		회원번호      	이름   	부서   	부서별 명수
      		22080101   	한동석   	개발팀   	4
      		22080104   	홍길동   	기획팀   	2
      		22081106   	이순신   	디자인팀   	3


	▶ 3차 정규화 진행

      		회원번호      	이름   	부서   
      		22080101   	한동석   	개발팀   
      		22080104   	홍길동   	기획팀   
      		22081106   	이순신   	디자인팀   
      		22080103   	장보고   	개발팀

      		부서   	부서별 명수
      		개발팀   	4
      		기획팀   	2
      		디자인팀   	3


=====================================================================================


- DML (데이터 조작어) -

	1. select: 조회(검색)

		select [컬럼명1, ...]
		from [테이블명]
		where [조건식]


	2. insert: 삽입(추가)

		1) 컬럼을 생략할 수 있다
			
			insert into [테이블명]
			([컬럼명1], [컬럼명2], ...)	
			values([값1], [값2], ...)


		2) 모든 값을 전부 작성할 수 있다

			insert into [테이블명]
			values([값1], [값2], ...)


	3. update: 수정
		
		update [테이블명]
		set [기존 컬럼명1] = [새로운 값1], [기존 컬럼명2] = [새로운 값2], ...
		where [조건식]


	4. delete: 삭제

		delete from [테이블명]
		where [조건식];


=====================================================================================


- 조건식 -
	
	- where 절에서 쓸 수 있는 조건식

		>, <			: 초과, 미만
		>=, <=		: 이상, 이하
		=			: 같다
		<>, !=, ^=		: 같지 않다
		AND			: 둘 다 참이면 참
		OR			: 둘 중 하나만 참이면 참


=====================================================================================


- Join -

여러 테이블에 흩어져 있는 정보 중,
사용자가 필요한 정보만 가져와서 가상의 테이블처럼 만들고 결과를 보여주는 것.

정규화를 통해 조회 테이블이 너무 많이 쪼개져있으면 작업이 불편하기 때문에,
조회 성능을 향상시키고자 join을 사용한다.


	- 내부 조인
		
		조건에 일치하는 값만 합쳐서 조회
		
		from [테이블명]
		inner join [테이블명]
		on 조건식
		inner join [테이블명]
		on 조건식
		inner join [테이블명]
		on 조건식
		...

		- 등가 조인
			on 절에 등호가 있을 때. 서로 관계를 맺고 있는(PK-FK) 테이블끼리 join 할 때 주로 사용된다.

		- 비등가 조인
			on 절에 등호가 없을 때. 서로 관계를 맺고 있지 않은 테이블끼리 join 할 때 주로 사용된다.


	- 외부 조인
		
		조건에 일치하지 않아도, 원하는 정보까지 합쳐서 조회
		

		- left outer join

			선행 테이블의 모든 정보를 가져오고 싶을 때 사용한다.


		- right outer join

			선행 테이블의 모든 정보를 가져오고 싶을 때 사용한다.


=====================================================================================


- 옵티마이저 (Optimizer) -

SQL을 가장 빠르고 효율적으로 수행할 최적의 처리 경로(= 최저비용)를 생성해주는 DBMS 내부의 핵심 엔진

사용자가 쿼리문으로 정보를 요청하면. 이를 생성하는 데 필요한 처리 경로는 DBMS에 내장된 옵티마이저가 자동으로 생성한다.
옵티마이저가 생성한 SQL 처리 경로를 실행계획(Execution Plan)이라고 한다.

	- Cost: 예상 수행 시간. 쿼리를 수행하는 데 소요되는 일의 양 또는 시간

	- Cardinality: 실행 결과의 건 수
		
		
- 옵티마이저의 SQL 최적화 과정 -

사용자가 작성한 쿼리를 수행하기 위해, 실행 계획을 찾는다.

데이터 딕셔너리에 미리 수집해놓은 오브젝트 통계 및 시스템 통계 정보를 이용해서,
각 실행계획의 예상 비용을 산정한다.

각 실행계획을 비교한 다음, 비용이 가장 적게 들어가는 하나를 선택하여 실행한다.


- 옵티마이저의 종류 -

	1. 규칙 기반 옵티마이저(RBO)
		
		미리 정해진 규칙에 따라 실행


	2. 비용 기반 옵티마이저(CBO)

		비용이 가장 낮은 실행계획을 선택

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
PARSER				OPTIMIZER					ROW_SOURCE				SQL_ENGINE
											GENERATOR

문법오류 검사			총 비용 계산				실행 가능한 코드로 변경		실행
코드로 변경			실행계획 생성


=====================================================================================


- TCL (트랜잭션 제어어) -

- 트랜잭션
	
	하나의 작업(서비스)에 필요한 쿼리들의 집합, 단위


	- commit

		모든 작업을 확정하는 명령어


	- rollback

		이전 commit 시점으로 이동


- CMD 창에서 오토 커밋 설정 -

> show variables like '%autocommit%';

      +---------------+-------+
      | Variable_name | Value |
      +---------------+-------+
      | autocommit    | OFF   |
      +---------------+-------+

> set autocommit = true;
> set autocommit = false;


=====================================================================================


- View (뷰) -

기존 테이블은 그대로 놔둔 채, 필요한 컬럼들 및 새로운 컬럼을 만든 가상의 테이블
참조만 하는 거라 실제 데이터가 저장되는 것은 아니지만, view로도 충분히 데이터를 관리할 수 있다.

	- 독립성: 다른 곳에서 접근하지 못하도록 하는 성질

	- 편리성: 긴 쿼리문을 짧게 만들어주는 성질

	- 보안성: 기존 쿼리문이 보이지 않는 성질


- View 문법 -

	create view [뷰 이름] as (select 쿼리문);


------------------------------------------------------------------------------------------------------------------------------------------------------


- Github 연동 작업 순서 -

1. python/workspace 파일 우클릭하고 추가 옵션 표시 - Open Git Bash Here 클릭

    * 경로 제대로 확인할 것!!


2. git branch 명령어로 현재 브랜치 목록 확인

    * 아마 'master' 라고 되어있는 거 하나만 있을 것


3. git checkout -b (브랜치명) 으로 새로운 브랜치 생성하면서, 거기로 이동

    * master 브랜치에서 작업하지 말 것. 지금은 혼자 하는 거라 큰 상관은 없겠지만,
      나중에 협업이나 프로젝트 할 때는 이거 지키는 게 매우 중요함

    * 현재 master 브랜치 상태를 기준으로 생성했으니, 그 로그 내용이 그래도 복사됨.
      작업은 여기서 진행


4. git status 입력해서 스테이징 해야 되는 파일 리스트 확인

    * 혹시 모르니, 무턱대고 바로 git add .(전부 스테이징) 하지는 말고, 파일 리스트 한 번 확인

    * git init은 처음에 했으니, 다음에 또 할 필요는 없음.
      단, workspace 파일에 숨은 파일까지 봤을 때, .git 이 없다면 git init 실행
      -> git과 연동하기 위함. 다시 한 번 말하지만, 제발 경로 제대로 확인 할 것!


5. git add . 실행

    * 새로 생겼거나, 내용이 수정된 파일이 전부 스테이징 됨

    * git status 입력해서 'No commits yet' 문구와,
      초록색 글자로 뜨는 (commit 할)파일 리스트 제대로 되어있는지 확인


6. git commit -m "메세지" 로 해당 브랜치에 커밋

    * 메세지 내용은 되도록 영어로, 어떤 작업을 했는지 기록할 것

    * git status 로 로그 확인하면 좋음


7. git checkout master 명령어 입력해서 master 브랜치로 이동

    * 작업은 3번 과정으로 만든 브랜치에서 했으니, master에는 기록이 없을 것


8. git merge (브랜치명) 으로 해당 브랜치에 있는 작업 내역(로그) 전부 가져오기


9. Github 사이트 들어가서, 내 레포지토리 안의 초록색 'Code' 버튼 누르면 나오는 https 주소 복사


10. git remote add origin (9에서 복사한 주소) 입력해서, Github 레포지토리랑 연결

    * 9번 과정에서 복사한 주소를 'origin' 이라는 이름의 원격 저장소로 쓰겠다는 의미

    * Git Bash 안에서의 붙여넣기는 Shift + Insert.
      기존에 쓰던 Ctrl + V 안 먹히니 주의.


11. git remote -v 로 원격 저장소 제대로 만들어졌는지 확인


12. git push origin master 로 Github에 있는 레포지토리에 수정사항 push 하기

    * origin 은 위에서 말한 대로 내 레포지토리의 https 주소고,
      master 는 그 레포지토리 안 master 브랜치(로컬 브랜치랑 다름!)를 의미.

    * 레포지토리 쪽 master 브랜치는 없다면 새로 생성됨


13. Github 레포지토리 들어가서 수정사항 제대로 적용됐는지 확인


- Github 사이트에서 코드 수정한 거 가져오기 -

14. 마찬가지로 Git Bash 열고, 다시 10번 과정으로 레포지토리랑 연결

    * 전에 열려있던 Git Bash 쓰는거면 안 해도 됨


15. git pull origin master 입력

    * 여기서의 master 브랜치는 로컬(내 컴퓨터) 내의 master 브랜치를 의미


16. 수정 사항 제대로 적용됐는지 확인하고, checkout 명령어로 3에서 만든 브랜치로 이동

    * 없으면 checkout -b 로 만들 것


17. git merge main 으로 Github에서 수정 한 거 가져오기

    * 16번 과정에서 없어서 새로 만들었다면 할 필요 없음


- 그 밖의 주의 사항 -

- add . -> merge -> push / pull 정도만 하면 되는 단순한 작업이지만,
  실수 방지를 위해 중간중간 git status 랑 git log 사용할 것


- 내 컴퓨터 / Github 중 어느 한쪽에서 작업했다면 반드시 동기화 할 것.
  절대 양쪽에서 다, 특히 같은 파일을 다른 방식으로 수정한 다음 push / pull 하려고 하지 말 것.
  이 경우에는 무조건 충돌이 발생하기 때문에,
  다시 말하지만 한 쪽에서 작업(이 파일 포함)이 끝날 때마다 push / pull 하는 거 까먹지 말 것!


- 모든 새 텍스트 파일은 작성이 끝난 다음, 'push 부터 한 다음에'
  Github 레포지토리 안 README 옆 수정 버튼 눌러서
  작성한 파일 Ctrl + A / Ctrl + C 로 전체 복사 하고, 페이지 맨 아래에 2줄 띄어서 붙여넣기


- 위 과정이 끝나면 레포지토리 쪽 README.md 파일이 수정되었을 것.
  pull로 가져오기.

- 기타 문제나 모르는 게 생기면 강사님께 문의
