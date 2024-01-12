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
