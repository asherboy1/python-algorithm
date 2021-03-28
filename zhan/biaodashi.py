# 中缀转后缀
from stack import Stack

def zhongzhuanhou(str):
    match = {
        "*" : 3,
        "/" : 3,
        "+" : 2,
        "-" : 2,
        "(" : 1
    }

    s = Stack()
    zflist = str.split(" ")
    tmp = []
    for i in zflist:
        if i in "ABCD":
            tmp.append(i)
        elif i == "(":
            s.push(i)
        elif i == ")":
            top = zflist.pop()
            while top != "(":
                tmp.append(top)
                top = s.pop()
        else:
            while (not s.isEmpty()) and (match[s.peek()] >= match[i]):      #设置优先级 比较  优先级高的出栈
                tmp.append(s.pop())
            
            s.push(i)
        
    while not s.isEmpty():
        tmp.append(s.pop())
    
    return "".join(tmp).replace("(","").replace(")","")

print(zhongzhuanhou("A + ( B * C )"))
print(zhongzhuanhou("( A + B ) * ( C + D )"))
