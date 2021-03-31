#二分法查找有序表       分而治之 解决小部分问题 缩小问题规模 O(log n)

# def erfen_search(list1,item):
#     found = False
#     first = 0
#     last = len(list1) - 1

#     while last >= first and not found:
#         midpoint = (first + last) // 2      #每次查找前与中间项比较
#         if list1[midpoint] == item:
#             found = True
#         else:
#             if list1[midpoint] > item:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1 
    
#     return found

# print(erfen_search([1,3,5,7,9,11,15,22,23],22))

#二分法递归 

def binearySearch(list2,item):
    found = True
    if len(list2) == 0:
        return False
    else:
        if list2[len(list2)//2] == item:
            return True
        else:
            if list2[len(list2)//2] > item:
                return binearySearch(list2[:len(list2)//2],item)        #切片！ 有时间开销O(k) k为切片长度
            else:
                return binearySearch(list2[len(list2)//2 + 1:],item)

print(binearySearch([1,2,3,5,6,9,18,41],1))