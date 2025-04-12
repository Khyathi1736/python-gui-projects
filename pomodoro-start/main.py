from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 24
SHORT_BREAK_MIN = 4
LONG_BREAK_MIN = 19
CHECK_X=80
CHECK_Y=340
reps=0
is_timer_on=False
checks=""


def on_reset_click():
    global is_timer_on,reps,checks
    checks=""
    check.config(text=checks)
    label.config(text="TIMER",fg=GREEN)
    start.config(state="normal")
    reps=0
    is_timer_on=False
    # remove checks
    canvas.itemconfig(canvas_text,text="00:00")

def take_break(min,sec,break_type):
    if is_timer_on:
        if break_type=="short":
            label.config(text="SHORT BREAK",fg=PINK)
        else:
            label.config(text="LONG BREAK",fg=RED)
        if min==0:
            start_work(WORK_MIN,60)
            return
        if sec!=0:
            sec-=1
        elif sec==0:
            sec=60
            min-=1
        # for better visuvalization of seconds i.e 05,04,03...
        if sec<10:
            canvas.itemconfig(canvas_text,text=f"{min}:0{sec}")
        else:
            canvas.itemconfig(canvas_text,text=f"{min}:{sec}")
        window.after(1000,take_break,min,sec,break_type)
    
def start_timer():
    # to avoid multible clicks of start it disables after clicking and does not work until we hit the reset button
    start.config(state="disabled")
    global is_timer_on,reps
    # reps+=1
    is_timer_on=True
    start_work(WORK_MIN,60)
    
def start_work(min,sec):
    global reps,is_timer_on,checks
    if is_timer_on:
        label.config(text="START WORK",fg="blue")
        if sec!=0:
            sec-=1
        elif sec==0:
            sec=60
            min-=1
        # for better visuvalization of seconds i.e 05,04,03...
        if sec<10:
            canvas.itemconfig(canvas_text,text=f"{min}:0{sec}")
        else:
            canvas.itemconfig(canvas_text,text=f"{min}:{sec}")
        # break controls i.e for every 4 works we have to take long break that funcitonaliry
        if min==0: 
            checks+="✔"
            check.config(text=checks)
            reps+=1
            if reps%4!=0:
                take_break(SHORT_BREAK_MIN,60,"short")
                return
            elif reps%4==0:
                take_break(LONG_BREAK_MIN,60,"long")  
                return            
        window.after(1000,start_work,min,sec)

    

window=Tk()
window.title("Pomodoro")
window.config(padx=80,pady=50,bg=YELLOW)

       
label=Label(text="Timer")
label.config(bg=YELLOW,font=(FONT_NAME,30,"bold"),fg=GREEN)
label.grid(column=1,row=0)

#to add image we should create canvas using canvas class
canvas=Canvas(width=250,height=250,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(125,120,image=tomato_image)
canvas_text=canvas.create_text(125,140,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)

start=Button(text="Start",font=(FONT_NAME,10,"bold"),bg="white",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

check=Label(text="",fg=GREEN,bg=YELLOW,font=("normal",15,"bold"),highlightthickness=0)
check.place(x=CHECK_X,y=CHECK_Y)

reset=Button(text="Reset",font=(FONT_NAME,10,"bold"),bg="white",highlightthickness=0,command=on_reset_click)
reset.grid(column=2,row=2)






window.mainloop()