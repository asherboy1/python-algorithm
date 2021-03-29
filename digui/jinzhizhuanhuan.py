#进制转换

#递归层数可调 

# import sys
# sys.getrecursionlimit()

def zhuanhuan(str1,base):
    convertstring = "0123456789ABCDEF"
    if str1 < base:
        return convertstring[str1]
    else:
        return zhuanhuan(str1//base,base) + convertstring[str1%base]    #先入到栈底

print(zhuanhuan(11,8))
