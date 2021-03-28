#后缀表达式计算
from stack import Stack

def jisuan(str):
    s = Stack()
    tmp = str.split(" ")

    for i in tmp:
        if i not in "()*-+/":
            s.push(int(i))
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.push(math(op1,op2,i))
            
    return s.pop()

def math(a,b,flag):
    if flag == "*":   #*
        return a * b
    if flag == "/":   #/        注意减法 除法的先后顺序
        return b / a
    if flag == "+":   #+
        return a + b
    if flag == "-":   #-
        return b - a

print(jisuan("5 60 7 * +"))
    