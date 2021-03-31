#选择排序 

def Selection_sort(list1):
    n = len(list1) - 1
    while n > 0:
        position = 0
        for i in range(1,n+1):
            if list1[i] > list1[position]:
                position = i        #记录位置

        tmp = list1[position]
        list1[position] = list1[n]
        list1[n] = tmp

        n -= 1
    
    return list1

a = Selection_sort([1,5,0,12,10,4,6])
print(a)