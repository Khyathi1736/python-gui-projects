from turtle import Screen,Turtle
from player import Player
from veichle import Car
from score_board import Score
import time

#setting initial screen
screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("white")

#setting turtle i.e player in position
timmy=Player()
screen.update()

# turtle movement
screen.listen()
screen.onkey(key="Up",fun=timmy.move_forward)
screen.onkey(key="Down",fun=timmy.move_backward)

car=Car()

score=Score()

def is_destination_reached():
    if timmy.distance(0,300)<=20:
        timmy.reset_timmy()
        screen.update()
        score.next_round()
        car.speed_increase()

def is_collide_with_cars():
    global game_is_on
    a=Turtle()
    a.hideturtle()
    for i in car.all_cars:
        if timmy.distance(i)<=21:
            a.write(arg="Game Over",align="center",font=("Arial",20,"normal"))
            game_is_on=False
            
    
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.cerate_car()
    car.move_cars()
    is_collide_with_cars()
    is_destination_reached()



screen.exitonclick()