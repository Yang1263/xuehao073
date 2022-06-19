import os
FindPath = r"C:\Users\dell\Desktop\test"#存放检测文件的根目录

def getfile():
    flag = 0
    try:#检测文件名字以及是否存在
        fileName = input("输入想检测的文件名字(xxx.py):\n")
        if fileName.find(".py",0,len(fileName))==-1: #检查是否为py文件
            raise Exception("输入格式错误!")
        FileNames = os.listdir(FindPath)
        for file in FileNames:#遍历当前目录，对比是否有该文件
            name = os.path.join(FindPath,file)
            if (name.find(fileName,0,len(name))!=-1):
                flag = 1
        if flag == 0:
            raise Exception("未找到文件!")
        else:
            return fileName
    except Exception as erro:
        print(erro)

def str_Processing(fileName):#逐行打开文件
    f = open(r'C:\Users\dell\Desktop\test\%s'%fileName, encoding='utf-8')
    data = f.readlines()
    return data

def catch_errorif(strdata):
    errossif =0#记录错误数
    for eachline in strdata:
        colon=0#记录冒号数
        keywords=0
        temp=str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            data = temp.replace(i, " ")
        data = data.split()
        for word in data:
            if word in ["if"]:
                keywords=keywords+1#检测需要冒号的关键字if
        for eachword in eachline:#函数if与冒号一一对应
            if eachword == ":" and keywords!=0:
                colon+=1

        if colon != keywords:
            print("%s----->此处缺少冒号"%eachline)
            errossif=errossif+1
    if errossif != 0:
        print("发现%s个if函数错误"%errossif)
    else:
        print("未发现if函数错误")

def catch_errortry(strdata):
    errosstry =0#记录错误数
    for eachline in strdata:
        colon=0#记录冒号数
        keywords=0#记录try数
        temp=str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            data = temp.replace(i, " ")
        data = data.split()
        for word in data:
            if word in ["try"]:
                keywords=keywords+1#检测需要冒号的关键字try
        for eachword in eachline:#函数try与冒号一一对应
            if eachword == ":" and keywords!=0:
                colon+=1
      
        if colon != keywords:
            print("%s----->此处缺少冒号"%eachline)
            errosstry=errosstry+1
        
    if errosstry != 0:
        print("发现%s个try函数错误"%errosstry)
    else:
        print("未发现try函数错误")

def catch_errorfor(strdata):
    errossfor =0#记录错误数
    for eachline in strdata:
        colon=0#记录冒号数
        keywords=0
        inwords=0#记录in数目
        temp=str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            data = temp.replace(i, " ")
        data = data.split()
        for word in data:
            if word in ["for"]:
                keywords=keywords+1#检测需要冒号的关键字for
        for eachword in eachline:#函数for与冒号一一对应
            if eachword == ":" and keywords!=0:
                colon+=1
        for word in data:
            if word in ["in"]:
                inwords=inwords+1
                
        if colon != keywords:
            print("%s----->此处缺少冒号"%eachline)
            errossfor=errossfor+1
        if inwords != keywords:
            print("%s----->此处缺少in"%eachline)
            errossfor=errossfor+1
    if errossfor != 0:
        print("发现%s个for函数错误"%errossfor)
    else:
        print("未发现for函数错误")

def errossnum(errif,errtry,errfor):
    errossnum=errif+errtry+errfor
    print("检查完毕，发现个%s错误"%errossnum)
    
def main():
    filename=getfile()
    catch_errorif(str_Processing(filename))
    catch_errortry(str_Processing(filename))
    catch_errorfor(str_Processing(filename))
    
