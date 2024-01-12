# 부모 클래스: 모양
# 메서드: 각 모서리의 갯수

# 삼각형
# 사각형
# 오각형
# 육각형

# 각 자식 클래스에 상속, 값 오버라이딩

# 각 클래스(도형) 별 넓이 구하기

# 어떤 도형인지 판단하는 메서드 - 모서리 개수를 받음

# 도형 클래스(부모) - 가로, 세로 길이 및 모서리 개수 필요
class Shape:
    def __init__(self, width, height, points):
        self.width = width
        self.height = height
        self.points = points

# 삼각형 클래스
# 가로, 세로 길이를 받는 건 그대로이기 때문에 생성자 재선언은 따로 하지 않음
class Triangle(Shape):
    # 삼각형 넓이 = 가로 * 세로 / 2
    def triangle_area(self):
        return self.width * self.height / 2

# 사각형 클래스
# 마찬가지로 가로, 세로 길이는 그대로
class Square(Shape):
    # 사각형 넓이 = 가로 * 세로
    def square_area(self):
        return self.width * self.height

# 오각형이랑 육각형은 넓이 어떻게 구해야 될 지 모르겠네요 ㅠ
class Pentagon(Shape):
    def __init__(self):
        pass

class Hexagon(Shape):
    def __init__(self):
        pass

# 삼각형 테스트
triangle = Triangle(20, 10, 3)
print(triangle.triangle_area())

# 사각형 테스트
square = Square(15,15, 4)
print(square.square_area())
