import requests
from bs4 import BeautifulSoup

except_layer = 2#设置期待层数与初始层
layer = 0

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)#获取对应的网页
        r.raise_for_status()#状态查询
        return r.text
    except:
        return ""

def getURL(text):
    global layer#全局变量
    global except_layer
    if layer < except_layer:#判断当前层数与期待层数是否一致
        layer += 1
        link_lst = []
        soup = BeautifulSoup(text, 'html.parser')#选择解析器
        links = soup.find_all('a')#获取soup内的a标签并返回一个列表
        for item in links:
            url = item.get('href')
            link_lst.append(url)#在列表末尾添加新的对象
        link_lst = list(filter(lambda url_str: 'http' in url_str, link_lst))#将网页链接作为列表传入
        print(link_lst)
        return link_lst
    else:
        l = []
        return l

def paChong(url):
    text = getHTMLText(url)
    lst = getURL(text)
    for m in lst:
        if lst == []:
            break
        paChong(m)

def main():
    url = input("请输入想爬网站：")
    paChong(url)




