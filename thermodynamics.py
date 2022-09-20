import turtle, math, random

class Compound(turtle.Turtle):
    def __init__ (self, pos_x, pos_y, vx, vy):
        col = random.choice(['red','green','yellow','skyblue','purple'])
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color(col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vx = vx
        self.vy = vy
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(self.pos_x, self.pos_y)

    def move(self):
        x = self.xcor()
        y = self.ycor()
        x += self.vx
        y += self.vy
        self.setpos(x,y)


class Display:

    def __init__(self):
        turtle.bgcolor("black")
        turtle.setworldcoordinates(-1000, -1000, 1000, 1000)
        turtle.delay(0)
        self.lst = []
        self.lst2 = []
        self.num_compounds = 0
        self.Thermodynamicsloop()
        turtle.listen()
        turtle.mainloop()
    def Thermodynamicsloop(self):
        turtle.ontimer(self.Thermodynamicsloop,30)
        if self.num_compounds < 50:
            mx = random.randint(-900,900)
            my = random.randint(-900,900)
            mvx = random.randint(-10,10)
            mvy =random.randint(-10,10)
            if mvx == 0:
                mvx = random.randint(-30,30)
            if mvy == 0:
                mvy =random.randint(-30,30)
            self.compounds = Compound(mx,my, mvx, mvy)
            self.lst.append(self.compounds)
            self.num_compounds += 1
            col = random.choice(['red','green','yellow','skyblue','purple','white','orange'])
        for i in self.lst:
            i.move()
            self.lst2.append(i)
            if i.xcor() > 999:
                i.vx *= -1
            if i.xcor() < -999:
                i.vx *= -1
            if i.ycor() > 999:
                i.vy *= -1
            if i.ycor() < -999:
                i.vy *= -1


Display()
