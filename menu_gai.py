import da_gai
import hello_gai
import shuma_gai
import cipin_gai
import tyyc_gai
import pachong
import grammar

menu0 = '''
        主菜单
==========================
1：绘图程序

2：哈希函数

3：7段数码管

4: 词频统计

5: 体育预测

6：爬虫程序

7：语法检查

8：敬请期待！

9：退出程序！
==========================
'''

#绘图程序
def myda():
    da_gai.main()
    
# 哈希函数
def myhello():
    hello_gai.main()
          
# 七段数码管
def myshuma():
    shuma_gai.main()

#词频统计
def mycipin():
    cipin_gai.main()

#体育预测
def mytyyc():
    tyyc_gai.main()

#爬虫程序
def mypachong():
    pachong.main()

#语法检查
def myyufa():
    grammar.main()
    
# 待开发
def qidai():
    print("功能尚待开发!")
    
def menuzong(): 
    while True:
        print(menu0)
        try:
            mc0= int(input("请输入菜单号:"))
            if mc0 == 1:
                myda()
            elif mc0 == 2:
                myhello()
            elif mc0 == 3:
                myshuma()
            elif mc0 == 4:
                mycipin()
            elif mc0 == 5:
                mytyyc()
            elif mc0 == 6:
                mypachong()
            elif mc0 == 7:
                myyufa()
            elif mc0 == 8:
                qidai()
            elif mc0 == 9:
                break
            else:
                print("输入的菜单号有误!")
        except ValueError:
            print("请输入正确格式的菜单号")
            
                
def main():
    menuzong()

main()
