#括号匹配
from stack import Stack 

def kuohaopipei(str):
    tmp = Stack()
    flag = True         #学会用flag
    i = 0

    while i < len(str) and flag :
        s = str[i]
        if s in "({[":
            tmp.push(s)
        else:
            if tmp.isEmpty():
                flag = False
            else:
                top = tmp.pop()

                if not match(top,s):
                    flag = False
        i += 1

    if tmp.isEmpty() and flag:
        return True
    else:
        return False


def match(a,b):         #精髓 通过预设值 对 最先匹配括号进行比较
    zuo = "({["
    you = ")}]"
    return zuo.index(a) == you.index(b)



print(kuohaopipei('(())'))

print(kuohaopipei('((((())'))

print(kuohaopipei("{()}"))