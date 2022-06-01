from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My Pong Game')
screen.tracer(0)

paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_b.move_up, "Up")
screen.onkeypress(paddle_b.move_down, "Down")
screen.onkeypress(paddle_a.move_up, "w")
screen.onkeypress(paddle_a.move_down, "s")

while game_is_on == True:
    time.sleep(.1)
    ball.move()
    screen.update()
    if ball.ycor() > 280:
        ball.bounce_top()
    
    if ball.ycor() < -280:
        ball.bounce_bottom()
    
    if ball.distance(paddle_b) < 50 and ball.xcor() > 340:
        ball.bounce_right()

    if ball.distance(paddle_a) < 50 and ball.xcor() < -340:
        ball.bounce_left()

    if ball.xcor() > 350:
        scoreboard.clear()
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -350:
        scoreboard.clear()
        scoreboard.r_point()
        ball.reset()
    

    

screen.exitonclick()