import turtle as t
SEGMENT_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20

class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()
        
        
    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)
        
    def add_segment(self,position):   
            new_segment=t.Turtle("square")
            new_segment.pu()
            new_segment.speed(0)
            new_segment.setposition(position)
            self.segments.append(new_segment)
    def extend_snake(self):
            self.add_segment(self.segments[-1].position())  #add at last segment position.
        
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
            
        
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].setpos(self.segments[i-1].pos())
        self.segments[0].forward(DISTANCE)
    
    
    def move_up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].seth(90)
    def move_down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].seth(270)
            
    def move_left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].seth(180)
    def move_right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].seth(0)
    