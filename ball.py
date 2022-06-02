from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_top(self):
        self.y_move *= -1

    def bounce_bottom(self):
        self.y_move *= -1
    
    def bounce_right(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_left(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.move_speed = 0.1
        self.move()