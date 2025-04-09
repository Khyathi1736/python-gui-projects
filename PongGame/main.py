from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.move_up)
screen.onkey(key="Down",fun=r_paddle.move_down)
screen.onkey(key="w",fun=l_paddle.move_up)
screen.onkey(key="s",fun=l_paddle.move_down)



game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()
    #detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
    #detect collision with left paddle
    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #when right side misses the ball
    if ball.xcor()>330  and  ball.distance(r_paddle)>50:
        ball.reset()
        ball.bounce_x() 
        score.l_point()  
    #when left side misses the ball.   
    if ball.xcor()<-340  and  ball.distance(l_paddle)>50:
        ball.reset()
        ball.bounce_x()
        score.r_point()
        
screen.exitonclick()