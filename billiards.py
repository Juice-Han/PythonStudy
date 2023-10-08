class Ball: # 공의 정보를 담고 있는 클래스
    def __init__(self):
        self.x = 0 # 공의 x 좌표
        self.y = 0 # 공의 y 좌표
        self.gradient = 1  # 공 진행 방향의 기울기가 1이면 1, -1 이면 -1
        self.direction = 1  # 공 진행 방향의 기울기가 1이면 1, -1 이면 -1

    def move(self):  # 공의 x,y 좌표 1씩 변화
        if self.direction == 1: # 오른쪽으로 진행하는 중이면
            self.x += 1  # x값 1 증가
            if self.gradient == 1: # 기울기가 1 이면
                self.y += 1 # y값도 1 증가
            else:
                self.y -= 1 # 아니면 1 감소
        else:
            self.x -= 1
            if self.gradient == 1:
                self.y -= 1
            else:
                self.y += 1

    def cushion_check(self, width, height): # 공이 쿠션에 닿았는지 확인하는 함수
        if (0 <= self.x <= width) and self.y == height: # 공의 좌표가 top cushion이라면
            print("top cushion (", self.x, ", ", self.y, ")") # 좌표 출력. 그 후 쿠션에 따라 공의 진행 방향 변화시키기
            if self.gradient == 1:
                self.gradient = -1
            else:
                self.gradient = 1
        elif (0 <= self.x <= width) and self.y == 0:
            print("bottom cushion (", self.x, ", ", self.y, ")")
            if self.gradient == 1:
                self.gradient = -1
            else:
                self.gradient = 1
        elif self.x == 0 and (0 <= self.y <= height):
            print("left cushion (", self.x, ", ", self.y, ")")
            if self.gradient == 1:
                self.direction = 1
                self.gradient = -1
            else:
                self.direction = 1
                self.gradient = 1
        elif self.x == width and (0 <= self.y <= height):
            print("right cushion (", self.x, ", ", self.y, ")")
            if self.gradient == 1:
                self.direction = -1
                self.gradient = -1
            else:
                self.direction = -1
                self.gradient = 1


def billiards(width, height):  # 당구 게임 실행 함수
    ball = Ball()  # 공 생성
    while True:
        ball.move()  # 공 움직이기
        if ball.x == 0 and ball.y == 0:  # 움직인 후 만약 공이 구석에 들어갔다면 좌표 출력하고 반복문 종료
            print("bottom left pocket (", ball.x, ", ", ball.y, ")")
            break
        elif ball.x == 0 and ball.y == height:
            print("top left pocket (", ball.x, ", ", ball.y, ")")
            break
        elif ball.x == width and ball.y == 0:
            print("bottom right pocket (", ball.x, ", ", ball.y, ")")
            break
        elif ball.x == width and ball.y == height:
            print("top right pocket (", ball.x, ", ", ball.y, ")")
            break
        ball.cushion_check(width, height) # 움직인 후 공이 쿠션에 닿았는지 확인


height_input = int(input())  # 높이 입력받기
width_input = int(input())  # 너비 입력받기
billiards(width_input, height_input)  # 당구게임 실행