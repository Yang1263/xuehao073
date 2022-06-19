import turtle,datetime,time
def drawGap():
  turtle.penup()
  turtle.fd(5)
def drawLine(draw):
  turtle.pendown() if draw else turtle.penup()
  turtle.fd(40)
  turtle.right(45)
  turtle.fd(5)
  turtle.right(90)
  turtle.fd(5)
  turtle.right(45)
  turtle.fd(40)
  turtle.right(45)
  turtle.fd(5)
  turtle.right(90)
  turtle.fd(5)
  turtle.right(45)
  turtle.fd(40)
  turtle.right(45)
  turtle.fd(5)
  turtle.left(45)
  drawGap()
  turtle.right(90)
def drawDigit(d):
  drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
  drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
  drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
  drawLine(True) if d in [0,2,6,8] else drawLine(False)
  turtle.left(90)
  drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
  drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
  drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
  turtle.left(180)
  turtle.penup()
  turtle.fd(20)
def drawDate(date):
  turtle.pencolor("red")
  for i in date:
    if i == '-':
      turtle.write('年',font=("Arial",18,"normal"))
      turtle.pencolor("red")
      turtle.fd(40)
    elif i == '=':
        turtle.write('月',font=("Arial",18,"normal"))
        turtle.pencolor("red")
        turtle.fd(40)
    elif i == '+':
        turtle.write('日',font=("Arial",18,"normal"))
    else:
        drawDigit(eval(i))

def getm():
    try:
        m=int(input("请选择：1.自动输入2.手动输入"))
    except:
        print("请输入正确格式的选项代号，例如1")
    return m

def getThetime(m):
    if m==1:
          Thetime=datetime.datetime.now().strftime('%Y-%m=%d+1')
          return Thetime
    elif m==2:
        try:
            tss1=(input("请按格式2011-1-1 输入一个时间"))
            timeArray = time.strptime(tss1, "%Y-%m-%d")
            otherStyleTime = time.strftime("%Y-%m=%d+1", timeArray)
            Thetime=otherStyleTime
            return Thetime
        except:
            print("输入格式错误！")
            
def main():
    turtle.setup(1000,350,200,200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    m=getm()
    Thetime=getThetime(m)
    drawDate(Thetime)
    turtle.hideturtle()


