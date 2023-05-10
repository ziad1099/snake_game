from turtle import *
import random
import time
#OOP
class Border(Turtle):
    def __init__(self,s_width,s_hieght):
        super().__init__()
        self.width=(s_width/2)-50
        self.hight=(s_hieght/2)-50
        # self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("#FF0802")
        self.pensize(10)
        self.goto(x=self.width,y=self.hight)
        self.pendown()
        self.setheading(270)
        self.fd(self.hight*2)
        self.setheading(180)
        self.fd(self.width*2)
        self.setheading(90)
        self.fd(self.hight*2)
        self.setheading(0)
        self.fd(self.width*2)
class Food(Turtle):
    def __init__(self,s_width,s_hieght):
        super().__init__()
        self.x=s_width/2-70
        self.y=s_hieght/2-70
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("yellow")
        self.loction()

    def loction(self):
        x=random.randint(-self.x,self.x)
        y=random.randint(-self.y,self.y)
        self.goto(x,y) 


class Extra(Turtle):
    def __init__(self,s_width,s_hieght):
        super().__init__()
        self.x=s_width/2-70
        self.y=s_hieght/2-70
        self.hideturtle()
        self.shape("circle")
        self.color("#D12513")
        self.penup()
        self.shapesize(1,1)

    def loction(self):
         x=random.randint(-self.x,self.x)
         y=random.randint(-self.y,self.y)
         self.goto(x,y) 

            

class Score(Turtle):
    def __init__(self,s_width,s_hieght):
        super().__init__()
        self.width=s_width/2-25
        self.hieght=s_hieght/2-25
        self.hideturtle()
        self.color("#9DFF86")
        self.penup()
        self.goto(0,self.hieght)
        self.score=-1
        try:
            file=open("score.txt",'r')
            self.high_score=int(file.read())
            file.close()
            self.update_s()
        except:
            file=open("score.txt",'w')
            # file.write("0")
            self.high_score=0
            file.close()
            self.update_s()
    def update_s(self):
        self.score+=1
        self.clear()
        if self.score>self.high_score:
            self.high_score=self.score
            file = open("score.txt", mode="w")
            file.write(f"{self.high_score}")
            file.close()
        self.write(f"Your Score : {self.score}\tHigh Score : {self.high_score}",align="center",font=("arial",15,"bold"))
    def game_over(self):
        self.clear()
        self.score = 0
        file = open("score.txt", mode="w")
        file.write(f"{self.high_score}")
        file.close()
        self.write(f"Your Score : {self.score}\tHigh Score : {self.high_score}",align="center",font=("arial",15,"bold"))
X_COR=0
def Body():
    s_body=[]
    x_cor=X_COR
    for i in range(5):
        np=Turtle() #new part
        np.penup()
        np.color("white","red")
        np.goto(x_cor,0)
        if i==0:
            np.shape("circle")
            np.shapesize(.5,.5)
        else:
            np.shape("square")
            np.shapesize(.5,.5)
        x_cor-=10
        s_body.append(np)
    return s_body            

class Snake:
    def __init__(self,x,y):
        self.body=Body()
        self.xmax=x/2-50
        self.ymax=y/2-50
        self.coloor=[
            "#FFD0AD","#BBFF26","#46FF0B","#18FF99","#09F8FF","#AB62C2","#644DC2","#C22E5D","#002F7A","#4D7A42",
            "#EDB358","#9E4646"
        ]
        self.cu_color=["white","red"]
        # self.ii=5
    # def move(self):
    #     for i in range(0,len(self.body)):
    #         self.body[i].fd(10) 
    def move(self):
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].setx(self.body[i - 1].xcor())
            self.body[i].sety(self.body[i - 1].ycor())
        self.body[0].forward(10) 
    def wall(self):
        xx=self.body[0].xcor()
        yy=self.body[0].ycor()
        x=self.xmax
        y=self.ymax
        return xx>x-13 or xx<-x+13 or yy>y-13 or yy<-y+13
    def ch_color(self):
        n=random.randint(0,len(self.coloor)-1)
        self.cu_color[1]=self.coloor[n]
        for i in self.body:
            i.color("white",self.coloor[n])
    def grow(self):
        np=Turtle()
        np.penup()
        np.shape("square")
        np.shapesize(.5,.5)    
        np.color("white",self.cu_color[1])
        np.goto(self.body[-1].position())
        self.body.append(np)
    def move_up(self):
        if self.body[0].heading()!=270:
           self.body[0].setheading(90) 
    def move_down(self):
        if self.body[0].heading()!=90:
            self.body[0].setheading(270)
    def move_left(self):
        if self.body[0].heading()!=0:
            self.body[0].setheading(180)
    def move_right(self):
        if self.body[0].heading()!=180:
            self.body[0].setheading(0)  
    def reset(self):
        for i in self.body:
            i.hideturtle()                   
        self.body=Body()
        for i in self.body:
            i.color("white",self.cu_color[1])

#main
def main():
    #setup
    win=Screen()
    win.setup(650,650)
    win.title("Ziad Ayman Ragab")
    win.tracer(0)
    win.bgcolor("#0F0F0F")
    border=Border(650,650)
    food=Food(650,650)
    score=Score(650,650)
    snake=Snake(650,650)
    extra=Extra(650,650)
    win.update()
    #keys
    listen()
    win.onkey(key="Up",fun=snake.move_up)
    win.onkey(key="Down",fun=snake.move_down)
    win.onkey(key="Right",fun=snake.move_right)
    win.onkey(key="Left",fun=snake.move_left)
    #start labale
    start=Turtle()
    start.hideturtle()
    start.penup()
    start.goto(0,200)
    start.pendown()
    start.color("#3DF1FF")
    start.write("Click space to start",font=("Times New Roman",15,"italic bold"),align="center")
    #my name labale
    me=Turtle()
    me.hideturtle()
    me.penup()
    me.goto(0,-305)
    me.pendown()
    me.color("#98FF5E")
    me.write("Created By Ziad Helaly",align="center",font=("Comic Sans MS",15,"normal"))
    #run
    def game():
        f=0
        f2=0
        start.clear()
        while True:
            snake.move()
            time.sleep(0.05)
            update()
            if snake.body[0].distance(food)<15:
                food.loction()
                score.update_s()
                snake.grow()
            if snake.wall():
                score.game_over() 
                snake.reset()
                start.write("Click space to start",font=("Times New Roman",15,"italic bold"),align="center")
                break  

            for i in snake.body[1::]:
                if i.distance(snake.body[0])<5:
                    
                    # start.write("Click space to start",font=("Times New Roman",15,"italic bold"),align="center")
                    f=1
                    break    
            if f==1:
                f=0
                snake.reset()
                score.game_over()
                start.write("Click space to start",font=("Times New Roman",15,"italic bold"),align="center")
                break
            if f2>=1 and snake.body[0].distance(extra)<15:
                snake.ch_color()
                f2=0
                score.score+=1
                score.update_s()

            if score.score%5==0 and score.score not in [0,1] and f2==0:
                extra.loction()
                extra.showturtle()
                f2+=1
            elif f2>=1 and score.score%5==0:
                continue
            else:
                f2=0
                extra.hideturtle() 
    win.onkey(fun=game,key="space")
    win.exitonclick()
#run
if __name__=="__main__":   
    main()
#Ziad Helaly
#2022    