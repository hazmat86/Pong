from turtle import Turtle, Screen
import random
from paddles import Paddle
from ball import Ball

game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My Pong Game')

paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(paddle_a.move_up, "Up")
screen.onkeypress(paddle_a.move_down, "Down")
screen.onkeypress(paddle_b.move_up, "w")
screen.onkeypress(paddle_b.move_down, "s")

#while game_is_on == True:
  

screen.exitonclick()