import turtle

def pen_da(pythonsize,penColor,head,speed):
    turtle.setup(0.5,0.5,0,0)       
    turtle.pensize(pythonsize)
    turtle.color(penColor)
    turtle.seth(head)    
    turtle.speed(speed)                   

def pen(size):
    pen_da(size,"red",0,1)

def getInput():
    try:
        size=int(input("画笔大小，如25"))
    except ValueError:
        print("请按正确的格式输入")
    return size

def getlen():
    try:
        length=int(input("请输入大小:(例如：200)"))
    except ValueError:
        print("请按照正确的格式输入")
    return length
  
def draw1(length):
    scale=50
    for i in range(length//4+1):
        a='*'   *i
        b='.'*(scale - i)
        c=(i/scale)*100
        turtle.fd(length//50)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')

def draw2(length):
    scale=50
    for i in range(length//4+1):
        a='*'   *i
        b='.'*(scale - i)
        c=(i/scale)*100
        turtle.fd(length//50)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')

def draw3(length):
    scale=50
    for i in range(length//4+1):
        j=i+length//4
        a='*'   *j
        b='.'*(scale - j)
        c=(j/scale)*100
        turtle.circle(-length,75//20)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')

def draw4(length):
    scale=50 
    for i in range(length//4+1):
        a='*'   *i
        b='.'*(scale - i)
        c=(i/scale)*100
        turtle.circle(length,75//20)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')
def drawDa(length):

    turtle.pendown()     
    draw1(length)
    turtle.penup()

    turtle.back(length/2)
    turtle.seth(-90) 
    turtle.back(length/4)
    turtle.pendown()
    draw2(length//2)
    turtle.penup()

    turtle.goto(length//2,0)
    turtle.seth(-90) 
    turtle.pendown()
    draw3(length//2)
    turtle.penup()

    turtle.goto(length//2,0)
    turtle.seth(-90) 
    turtle.pendown()
    draw4(length//2)
    turtle.mainloop()


def main():
    size=getInput()
    pen(size)
    length=getlen()
    drawDa(length)

      
