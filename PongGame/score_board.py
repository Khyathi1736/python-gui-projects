from turtle import Turtle,Screen
import tkinter as tk
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.create_score()
        
    def create_score(self):
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=('Arial', 40, 'normal'))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=('Arial', 40, 'normal'))
        
    def l_point(self):
        self.l_score+=1
        self.clear()
        self.create_score()
        if self.l_score==3:
            screen=Screen()
            root = tk.Tk()
            root.title("Game Over")
        
            # Create a Text widget to display output
            text_box = tk.Text(root, height=10, width=50)
            text_box.pack()
        
            # Insert the output text into the Text widget
            text_box.insert(tk.END, "Player 1 Won the Game")

            screen.exitonclick()        
        
        
    def r_point(self):
        self.r_score+=1
        self.clear()
        self.create_score()
        if self.r_score==3:
            screen=Screen()
            root = tk.Tk()
            root.title("Game Over")
        
            # Create a Text widget to display output
            text_box = tk.Text(root, height=10, width=50)
            text_box.pack()
        
            # Insert the output text into the Text widget
            text_box.insert(tk.END, "Player 2 Won the Game")

            screen.exitonclick()
        