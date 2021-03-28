#十进制转N进制
from stack import Stack

def shizhuaner(num,n):
    digits = "0123456879ABCDEF"

    s = Stack()
    while num != 0:
        tmp = num % n       #求余数
        num = num // n      #整数除
        s.push(tmp)
    
    str = ""
    for i in range(s.size()):
        str = str + digits[s.pop()]     #设置对应位置 进行转换
    
    print(str)

shizhuaner(233,16)