from turtle import Turtle,Screen
import random
screen=Screen()
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.level_choosen=screen.textinput(title="Choose level",prompt="1.easy 2.medium 3.difficult")
        if self.level_choosen=="easy":
            self.level=0.5
        elif self.level_choosen=="medium":
            self.level=0.1
        elif self.level_choosen=="difficult":
            self.level=0
        else:
            self.level=0.1
        li=[5,8,10,13,15,17,20]
        r=random.choice(li)
        print(r)
        self.x_move=r
        self.y_move=r
    
    def move(self):
        time.sleep(self.level)
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.y_move*= -1
                
    def bounce_x(self):
        self.x_move*= -1
        
    def reset(self):
        self.goto(0,0)
        time.sleep(0.5)
        
        