#希尔排序 一般从n/2开始 每趟倍增 间隔直至为1  O(n^3/2)

def Shell_sort(list1):
    substring = len(list1) // 2     #设定间隔

    while substring > 0:
        for i in range(substring):      #子列表排序
            Shell_insert_sort(list1,i,substring)

        substring //= 2 #缩小间隔 直至为1

    return list1


def Shell_insert_sort(orilist,startpoint,gap):      #带间隔的插入排序
    for i in range(1,len(orilist)):
        current = orilist[i]
        position = i

        if position > 0 and orilist[i-1] > current:
            orilist[i] = orilist[i-1]
            position -= 1
        
        orilist[position] = current
    

print(Shell_sort([1,5,2,3,9,14,20,16]))