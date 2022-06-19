import hashlib

def ha(data):
    result=hashlib.md5(data.encode())
    print("hash value is:")
    print(result)
    print("hexadecimal result is")
    print(result.hexdigest())

def getdata():
    try:
        data=input("请输入：")
    except:
        print("请重新输入正确的值")
    return data
    
def main():
    data=getdata()
    ha(data)
    

