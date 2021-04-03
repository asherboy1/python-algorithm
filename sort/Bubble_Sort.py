#冒泡排序 对无序表进行排序  O(n^2)  无内存额外开销

# def Bubble_sort(list):
#     n = len(list)

#     while n > 0:
#         for j in range(n-1):
#             if list[j] > list[j+1]:
#                 m = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = m

#                 # list[j],list[j+1] = list[j+1],list[j]   #直接表示交换
        
#         n -= 1
    
#     return list

# test = Bubble_sort([7,2,5,1,4,4,0])
# print(test)

#----------------- 官方
def Bubble_sort(list2):
    exchanges = True
    passnum = len(list2) - 1
    while passnum > 0 and exchanges:        #exchanges 性能改进 当一次发现已经不需要都更改了 就直接结束排序
        exchanges = False
        for i in range(passnum):
            if list2[i] > list2[i+1]:
                exchanges = True        #发现有需要排序的 更改exchanges
                list2[i],list2[i+1] = list2[i+1],list2[i]

        passnum -= 1
    return list2

print(Bubble_sort([27,10,52,3,9,18,20]))


