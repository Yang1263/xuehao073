from random import *
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示）")
def getInputs():
    a=eval(input("请输入选手A的能力值(0-1):"))
    b=eval(input("请输入选手B的能力值(0-1):"))
    wa=eval(input("请输入选手A的失误概率(0-1):"))
    wb=eval(input("请输入选手B的失误概率(0-1):"))
    n=eval(input("模拟比赛的场次:"))
    return a,b,wa,wb,n
def simNGames(n,probA,probB,wA,wB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB,wA,wB)
        if scoreA>scoreB:
            winsA +=1
        else:
            winsB +=1
    return winsA,winsB
def gameOver(a,b):
    return a==15 or b==15
def simOneGame(probA,probB,wA,wB):
    scoreA, scoreB= 0,0
    serving ="A"
    List1=['晴天','雨天','多云']
    if choice(List1) == "晴天":
        wea = 1
    elif choice(List1) == "多云":
        wea = 0.9
    else:
        wea = 0.8
    List2=['失误','不失误']
    if choice(List2) == "失误":
        wro = 1
    else:
        wro = 0
    probA1 = probA * 0.8+wea*0.1-wA*wro 
    probB1 = probB * 0.8+wea*0.1-wB*wro
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA1:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<probB1:
                scoreB+=1
            else:
                serving="A"
        return scoreA,scoreB
def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def main():
    printIntro()
    probA,probB,wA,wB,n=getInputs()
    winsA,winsB=simNGames(n,probA,probB,wA,wB)
    printSummary(winsA,winsB)


