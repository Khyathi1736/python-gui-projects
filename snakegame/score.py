from turtle import Turtle 
# from Higher_Score import  high_score
ALIGN="center"
FONT=("Arial",15,"normal")
with open("file.txt") as score_file:
    maxscore=int(score_file.read())
    
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.Score=0
        self.Highscore=maxscore
        self.create_score_board()
        
    def create_score_board(self):
        self.clear()
        self.pu()
        self.hideturtle()
        self.setpos(0,330)
        self.write(f"Score : {self.Score} HighScore : {self.Highscore}",align=ALIGN,font=FONT)
        
    def score_increase(self):
        # global high_score
        self.clear()
        self.Score+=1
        self.write(f"Score : {self.Score} Highscore :{self.Highscore}",align=ALIGN,font=FONT)
        
    def reset_score(self):
        
        if self.Score>self.Highscore:
            self.Highscore=self.Score
            with open("file.txt",mode="w") as maxscore:
                maxscore.write(f"{self.Highscore}")
                
        self.Score=0
        self.create_score_board()