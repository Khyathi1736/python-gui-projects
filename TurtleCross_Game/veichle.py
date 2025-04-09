import turtle as t 
import random as r
t.colormode(255)
CAR_MOVEMENT=10
class Car():
    def __init__(self):
        self.all_cars=[]
        
    def rand_col(self):
        while True:
            re=r.randint(0,255)
            b=r.randint(0,255)
            g=r.randint(0,255)
            colour=(re,b,g)
            if (re,b,g)!=(255,255,255):
                return colour
    
    def cerate_car(self):
        chance=r.randint(1,6)
        if chance==6 or chance==1:
            y=r.randint(-240,240)
            new_car=t.Turtle()
            new_car.pu()
            new_car.shape("square")
            new_car.color(self.rand_col())
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.seth(180)
            new_car.goto(300,y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for i in self.all_cars:
            i.forward(CAR_MOVEMENT)
            
    def speed_increase(self):
        global CAR_MOVEMENT
        CAR_MOVEMENT+=10
        self.move_cars()