from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, color="orange", shape="circle"):
        self.segments = []
        self.color = color
        self.shape = shape
        self.x_cord = 0
        self.create_snake()
        self.head = self.segments[0]
        


    def create_snake(self):
        for _ in range(3):
            self.add_segment()
    

    def add_segment(self,):
        new_segment = Turtle(shape=self.shape)
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(x=self.x_cord, y=0)
        self.segments.append(new_segment)
        self.x_cord = self.x_cord - 20


    def extend(self):
        self.add_segment()


    def move(self):
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num -1].xcor()
                new_y = self.segments[seg_num -1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reappear_x(self):
        position_x = self.head.xcor() * -1
        position_y = self.head.ycor()
        self.head.goto(position_x, position_y)


    def reappear_y(self):
        position_x = self.head.xcor()
        position_y = self.head.ycor() * -1
        self.head.goto(position_x, position_y)
