import random
from turtle import Screen, Turtle
from time import sleep

wd = Screen()
wd.setup(width=800, height=600)
wd.bgcolor('black')
wd.title("Pong")
wd.tracer(0)


class Player:
    def __init__(self, player_num=1):
        self.position = [0, 20, 40, -20, -40]
        self.player_body = []
        self.player_num = player_num
        if self.player_num == 1:
            self.X_CORD = -350
        else:
            self.X_CORD = 350

    def create(self):
        for pos in self.position:
            p = Turtle()
            p.shape('square')
            p.color('white')
            p.pu()
            p.seth(90)
            p.goto(self.X_CORD, pos)

            self.player_body.append(p)

    def move_up(self):
        distance_from_border = self.player_body[2].distance(self.X_CORD, 300)
        if distance_from_border > 20:
            for part in self.player_body:
                part.fd(20)
        else:
            pass

    def move_down(self):
        distance_from_border = self.player_body[2].distance(self.X_CORD, -245)
        if distance_from_border > 20:
            for part in self.player_body:
                part.bk(20)
        else:
            pass

    def move(self):
        wd.listen()
        wd.onkeypress(self.move_up, 'Up')
        wd.onkeypress(self.move_down, 'Down')

    def random_movement(self):
        distance_from_bottom = self.player_body[2].distance(self.X_CORD, -245)
        distance_from_top = self.player_body[2].distance(self.X_CORD, 300)
        for part in self.player_body:
            part.fd(8)
        if distance_from_top < 10:
            for part in self.player_body:
                part.seth(270)
        elif distance_from_bottom < 10:
            for part in self.player_body:
                part.seth(90)


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('square')
        self.ball.color('white')
        self.ball.pu()
        self.ball.seth(random.randint(0, 360) )
        self.start_angle()

    def start_angle(self):
        angle = [num for num in range(90, 270) if num not in range(75, 106) and num not in range(255, 286)]
        self.ball.seth(angle[random.randint(0, len(angle) - 1)])

    def move(self):
        self.ball.fd(2)

    def hit_player(self, player):
        for part in player.player_body:
            if abs(self.ball.xcor()) + 10 in range(int(player.player_body[0].xcor() - 10), int(player.player_body[0].xcor() + 11)):
                if self.ball.heading() < 90:
                    self.ball.seth(self.ball.heading() + 90)
                elif self.ball.heading() > 90:
                    self.ball.seth(self.ball.heading() - 90)

    def hit_wall(self):
        distance_from_bottom = self.ball.distance(self.ball.xcor(), -245)
        distance_from_top = self.ball.distance(self.ball.xcor(), 300)
        if distance_from_top < 10 or distance_from_bottom < 10:
            if self.ball.heading() < 180:
                self.ball.seth(self.ball.heading() + 90)
            elif self.ball.heading() > 180:
                self.ball.seth(self.ball.heading() - 90)


player1 = Player(1)
player1.create()
player2 = Player(2)
player2.create()
game_ball = Ball()
game_on = True
while game_on:
    sleep(0.01)
    wd.update()
    player1.move()
    player2.random_movement()
    game_ball.move()
    game_ball.hit_player(player1)
    game_ball.hit_player(player2)
    game_ball.hit_wall()
wd.exitonclick()
