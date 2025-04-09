from turtle import Turtle
FORWARD_DISTANCE=10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        
    def create_turtle(self):
        self.color("black")
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.goto(0,-280)
        
    def reset_timmy(self):
        self.goto(0,-280)
        
        
    def move_forward(self):
        self.forward(FORWARD_DISTANCE)
        
    def move_backward(self):
        if self.distance(0,-300)>=10:
            self.back(FORWARD_DISTANCE)