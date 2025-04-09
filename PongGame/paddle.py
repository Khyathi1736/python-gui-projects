from turtle import Turtle,Screen
screen=Screen()
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

        
    def create_paddle(self,position):
        screen.tracer(0)
        self.shape("square")
        self.pu()
        self.seth(90)
        self.color("white")
        self.shapesize(stretch_len=4,stretch_wid=None)
        self.setpos(position)
        screen.update()
        screen.tracer(1)
        
        
    def move_up(self):
        if self.ycor() <250:
            self.forward(20)
    def move_down(self):
        if self.ycor()>-250:
            self.back(20)