from turtle import Turtle
class Score():
    def __init__(self):
        self.current_round=1
        self.round_board=Turtle()
        self.round()
   
    def round(self):
        self.round_board.pu()
        self.round_board.hideturtle()
        self.round_board.goto(-270,270)
        self.round_board.write(f"Level : {self.current_round}",align="center",font=("Arial",10,"normal"))
        
    def next_round(self):
        self.current_round+=1
        self.round_board.clear()
        self.round()
        