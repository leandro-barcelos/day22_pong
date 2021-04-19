import random
import sys
from turtle import Screen, Turtle
from time import sleep

wd = Screen()
wd.setup(width=800, height=600)
wd.bgcolor('black')
wd.title("Pong")
wd.tracer(0)
BOTTOM = -300
UPPER = 300


def dist_up(turtle):
    return abs(turtle.ycor() - UPPER)


def dist_bot(turtle):
    return abs(turtle.ycor() - BOTTOM)


class Player:
    def __init__(self, player_num=1):
        self.position = [0, 20, 40, -20, -40]
        self.body = []
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

            self.body.append(p)

    def move_up(self):
        distance_from_border = dist_up(self.body[2])
        if distance_from_border > 20:
            for part in self.body:
                part.fd(20)
        else:
            pass

    def move_down(self):
        distance_from_border = dist_bot(self.body[4])
        if distance_from_border > 20:
            for part in self.body:
                part.bk(20)
        else:
            pass

    def move(self):
        wd.listen()
        if self.player_num == 1:
            wd.onkeypress(self.move_up, 'w')
            wd.onkeypress(self.move_down, 's')
        if self.player_num == 2:
            wd.onkeypress(self.move_up, 'Up')
            wd.onkeypress(self.move_down, 'Down')

    def random_movement(self):
        distance_from_bottom = self.body[2].distance(self.X_CORD, BOTTOM)
        distance_from_top = self.body[2].distance(self.X_CORD, UPPER)
        for part in self.body:
            part.fd(8)
        if distance_from_top < 10:
            for part in self.body:
                part.seth(270)
        elif distance_from_bottom < 10:
            for part in self.body:
                part.seth(90)


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('square')
        self.ball.color('white')
        self.ball.pu()
        self.ball.seth(random.randint(0, 360))
        self.set_angle()

    def set_angle(self, player_scorer=0):
        if player_scorer != 0:
            if player_scorer == 1:
                angle = [num for num in range(0, 360) if num not in range(30, 330)]
                self.ball.seth(angle[random.randint(0, len(angle) - 1)])
            elif player_scorer == 2:
                angle = [num for num in range(150, 210)]
                self.ball.seth(angle[random.randint(0, len(angle) - 1)])
        else:
            angle = [num for num in range(0, 360) if num not in range(30, 150) and num not in range(210, 330)]
            self.ball.seth(angle[random.randint(0, len(angle) - 1)])

    def move(self):
        self.ball.fd(5)

    def hit_player(self, player):
        pass

    def bounce(self, players):
        if dist_up(self.ball) < 10 or dist_bot(self.ball) < 10:
            self.ball.seth(360 - self.ball.heading())
        for player in players:
            for part in player.body:
                if self.ball.distance(part.position()) < 10:
                    self.ball.seth(540 - self.ball.heading())

    def return_position(self, player_scorer=0):
        self.ball.goto(0, 0)
        self.set_angle(player_scorer)


class Scoreboard:
    def __init__(self):
        self.players_points = [0, 0]
        x = 100
        y = 150
        positions = [(-x, y), (x, y)]
        self.writers = []
        for pos in positions:
            w = Turtle()
            w.hideturtle()
            w.pu()
            w.goto(pos)
            w.pencolor('white')
            self.writers.append(w)

    def point(self, ball):
        if ball.ball.xcor() < -400:
            self.players_points[1] += 1
            ball.return_position(2)
        elif ball.ball.xcor() > 400:
            self.players_points[0] += 1
            ball.return_position(1)

    def write(self):
        for i in [0, 1]:
            self.writers[i].clear()
            self.writers[i].write(f"{self.players_points[i]}", align='center', font=('Pong Score', 100, 'normal'))

    def check_win(self):
        for i in [0, 1]:
            if self.players_points[i] == 9:
                print(f"Player {i + 1} won!")
                sys.exit()


player1 = Player(1)
player1.create()
player2 = Player(2)
player2.create()
game_ball = Ball()
score = Scoreboard()
game_on = True
while game_on:
    sleep(0.01)
    wd.update()
    player1.move()
    player2.move()
    # player2.random_movement()
    game_ball.move()
    game_ball.bounce([player1, player2])
    score.point(game_ball)
    score.write()
    score.check_win()

wd.exitonclick()
