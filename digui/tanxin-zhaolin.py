#贪心算法 找零 25 10 1

n25 = 0
n10 = 0
def zhaolin(num):
    global n25
    global n10
    if n25 * 25 < num:
        n25 += 1
        return zhaolin(num - 25)
    elif n10 * 10 < num:
        n10 += 1
        return zhaolin(num - 10)
    else:
        return f"需要{num+10}个1分 {n10}个10分 {n25}个25分 硬币"   


print(zhaolin(53))