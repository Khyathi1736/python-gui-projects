import random as r
import turtle
WIDTH=(700//2)-20
HEIGHT=(700//2)-20

class Food:
    def __init__(self):
        self.timmy=turtle.Turtle()
        self.timmy.pu()
    def food_generate(self):
        self.timmy.goto(r.randint(-WIDTH,HEIGHT),r.randint(-WIDTH,HEIGHT))
        self.timmy.shape("circle")
        self.timmy.shapesize(stretch_len=0.5,stretch_wid=0.5)
    