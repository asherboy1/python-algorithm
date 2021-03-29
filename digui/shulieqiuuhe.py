#不使用 循环语句 进行数列求和 递归

#递归三要素
#1.有一个基本结束条件
#2.能够向基本结束条件进行演进 逐步减小问题规模
#3.必须调用自身

def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])        #调用自身 更小规模

print(listsum([1,5,4,7]))