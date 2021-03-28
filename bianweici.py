#变位词

#-----------------------------1 时间复杂度 O(nlogn)
# def bianweici1(str1,str2):

#     if len(str1) != len(str2):
#         return False
    
#     list1 = list(str1)
#     list2 = list(str2)
#     list1.sort()        #sort并不是无代价的 也需要消耗资源    
#     list2.sort()

#     for i in range(len(str1)):
#         if list1[i] == list2[i]:
#             continue
#         else:
#             return False

#     return True

# str1 = input("str1:\n").lower()
# str2 = input("str2:\n").lower()
# result = bianweici1(str1,str2)
# print(result) 

#-----------------------------2     时间复杂度O(n)
# def bianweici2(str1,str2):
#     c1 = [0] * 26       #创建了一个列表 谁当了初始值 复制了26个
#     c2 = [0] * 26

#     if len(str1) != len(str2):
#         return False

#     for i in range(len(str1)):
#         tmp = ord(str1[i]) - ord('a')       #通过ascii码 算出每次字符出现的次数 在进行比较！
#         c1[tmp] = c1[tmp] + 1

#         tmp = ord(str2[i]) - ord('a')
#         c2[tmp] = c2[tmp] + 1
    
#     num = 0
#     flag = True
#     while num < 26 and flag:    #精髓 固定比较26次    空间 换取 时间
#         if c1[num] == c2[num]:
#             num += 1
#             continue
#         else:
#             flag = False
    
#     return flag

# print(bianweici2("abc","cba"))

#---------------------------3  时间复杂度为O(n)
def bianweici3(str1,str2):

    if len(str1) != len(str2):
        return False

    dict1 = {}          #采用了字典 相比于方法2 更优化了空间 查找更迅速
    dict2 = {}
    save = []
    for i in range(len(str1)):
        tmp = ord(str1[i]) - ord('a')
        save.append(tmp)
        if str(tmp) in dict1.keys():
            dict1[str(tmp)] += 1
        else:
            dict1[str(tmp)] = 1
        
        tmp = ord(str2[i]) - ord('a')
        if str(tmp) in dict2.keys():
            dict2[str(tmp)] += 1
        else:
            dict2[str(tmp)] = 1
        
    for j in set(save):
        try:
            if dict1[str(j)] == dict2[str(j)]:
                continue
        except:
            return False
        else:
            return False

    return True

print(bianweici3("abcd","ceba")) 