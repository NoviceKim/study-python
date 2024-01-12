# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

class Member:
    # 번호의 초기값 지정
    number = 0

    # 생성자 선언 - 아이디, 비번, 이름
    # 번호는 알아서 증가하니 받을 필요 없음
    # 클래스 객체 만들면 번호가 1 증가
    def __init__(self, **kwargs):
        # Member 클래스 자체에 저장된 number 변수값 +1
        Member.number += 1
        
        # 현재 Member 클래스에 선언된 number(+1한 값) 갖고 와서 그대로 할당
        self.number = Member.number

        self.id = kwargs.get('id')
        self.password = kwargs.get('password')
        self.name = kwargs.get('name')

    # 관리자 회원가입의 기준은 따로 두지 않음
    # 이 메소드로 클래스에 접근하면 id 앞에 "admin_" 글자 붙여줌
    @classmethod
    def admin_connect(cls, **kwargs):
        # 딕셔너리 타입으로 전달된 값에서 'id' 키를 찾고, 그 값 앞에 'admin' 을 붙여서 재할당
        kwargs["id"] = "admin_" + kwargs["id"]

        # 위의 데이터 수정 과정 이후의 딕셔너리를 클래스 생성자에 반환(= __init__ 의 매개변수로 넣음)
        return cls(**kwargs)

# 클래스 메소드 테스트
admin = Member.admin_connect(id='KGH', password='12345678', name='김광협')

member = Member(id='KGH', password='12345678', name='김광협')

print(admin.id, admin.number, sep=", ")


print(member.id, member.number, sep=", ")

# Private
# 변수 앞에 __number 같이 아래 슬래시 2개를 붙이면, 해당 클래스 내에서만 접근 가능
# 목적 1. 외부에서 그 변수에 직접 접근하려고 하지 말자
# 목적 2. 접근하고 싶다면, 그 클래스의 메소드로 접근하자
