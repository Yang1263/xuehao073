import keyword
keylist=keyword.kwlist

def getname():
    try:
        wenjian=input("请输入文件名：（例如hello.py）")
    except:
        print("请按正确的格式输入（如hello.py）")
    return wenjian

def getText(wenjian):
    txt = open(wenjian, "r",encoding='utf-8'). read()
    txt = txt.lower()
    for ch in  '!"#$%&()*+,-./;:<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    return txt

def getitems(wenjianTxt):
    words = wenjianTxt.split()
    counts = {}
    for word in words:
        if word in keylist:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    return items
    

def getprint(items):
    items.sort(key=lambda x:x[1], reverse=True)
    try:
        for i in range(33):
            word, count = items[i]
            print("{0:<10}{1:>5}".format(word, count))
    except:
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

def main():
    name=getname()
    text=getText(name)
    items=getitems(text)
    getprint(items)

    
    
