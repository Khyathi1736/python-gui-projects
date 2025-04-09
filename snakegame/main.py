import turtle as t 
import snake
import food
import time
import score
# from Higher_Score import high_score
SCREEN_WIDTH=700
SCREEN_HEIGHT=700
ALIGN="center"
FONT=("Arial",15,"normal")

screen=t.Screen()
screen.bgcolor("pink")
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.title("Snake Game")
screen.tracer(0)       #not shows the animation until we use update function.



snake_x_position=0
snake_y_position=0
is_game_on=True

Snake1=snake.Snake()
score_board=score.Score_board()
snake_food=food.Food()

screen.listen()
screen.onkey(key="Up",fun=Snake1.move_up)
screen.onkey(key="Left",fun=Snake1.move_left)
screen.onkey(key="Right",fun=Snake1.move_right)
screen.onkey(key="Down",fun=Snake1.move_down)


def game_continue():
    snake_food.food_generate() #main call
    x=snake_food.timmy.xcor()
    y=snake_food.timmy.ycor()
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        Snake1.move()
        #to check collision with wall
        is_wall_collide()
        #to check collision with itself
        is_collide_itself()
            
                   
        #collision detection with food.
        if  Snake1.segments[0].distance(x,y)<15:
            Snake1.extend_snake()
            score_board.score_increase()         #to increase score                     
            snake_food.timmy.clear()
            game_continue()

def is_wall_collide():
   if Snake1.segments[0].xcor()>340 or Snake1.segments[0].xcor()<=-345 or Snake1.segments[0].ycor()>=345 or Snake1.segments[0].ycor()<=-343:
       t.hideturtle()
       Snake1.reset_snake()
       score_board.reset_score()
    #    t.write("Game Over.",align=ALIGN,font=FONT)
    #    t.exitonclick()
       
def is_collide_itself():
    for i in Snake1.segments[1: ]:  #list slicing i.e avoiding head of the snake to check to collides with itself which is meaningless.
        if Snake1.segments[0].distance(i)<=10:
            Snake1.reset_snake()
            score_board.reset_score()
            #  t.write("Game Over.",align=ALIGN,font=FONT)
            #  t.exitonclick()  
    
       
    
  
#main call       
game_continue()        
         
    
















screen.exitonclick()