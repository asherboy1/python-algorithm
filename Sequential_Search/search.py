#无序表顺序查找 --------------------O(n)

# def sequentialSearch(list1,item):
#     weizhi = 0
#     found = False

#     while weizhi < len(list1) and not found:
#         if list1[weizhi] == item:
#             found = True
#         else:
#             weizhi += 1

#     return found

# print(sequentialSearch([1,15,24,79,0,5],5))

#有序表查找 -----------------------O(n)

def sequentialSearch(list2,item):
    weizhi = 0
    flag = False
    found = False

    while weizhi < len(list2) and not found and not flag:       #设置了停止 当查找目标为有序表时  所想查找的值如果小于了当前列表里的值  就停止了查找
        if list2[weizhi] == item:
            found = True
        else:
            if list2[weizhi] > item:
                flag = True
            else:
                weizhi += 1
    
    return found

print(sequentialSearch([1,2,4,9,13,25,32],25))
