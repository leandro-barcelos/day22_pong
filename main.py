from turtle import Screen, Turtle

wd = Screen()
wd.setup(width=800, height=600)
wd.bgcolor('black')
wd.title("Pong")
wd.tracer(0)


class Player:
    def __init__(self, player_num=1):
        self.position = [0, 20, -20]
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
        distance_from_border = self.player_body[1].distance(self.X_CORD, 300)
        if distance_from_border > 20:
            for part in self.player_body:
                part.fd(20)
        else:
            pass

    def move_down(self):
        distance_from_border = self.player_body[1].distance(self.X_CORD, -245)
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
        distance_from_bottom = self.player_body[1].distance(self.X_CORD, -245)
        distance_from_top = self.player_body[1].distance(self.X_CORD, 300)
        move_factor = -20
        for part in self.player_body:
            part.fd(move_factor)
        if distance_from_top < 10 or distance_from_bottom < 10:
            move_factor *= -1


player1 = Player(1)
player1.create()
player2 = Player(2)
player2.create()
game_on = True
while game_on:
    wd.update()
    player1.move()
    player2.random_movement()
wd.exitonclick()
