#冒泡排序 对无序表进行排序  O(n^2)  无内存额外开销

def Bubble_sort(list):
    n = len(list)

    while n > 0:
        for j in range(n-1):
            if list[j] > list[j+1]:
                m = list[j]
                list[j] = list[j+1]
                list[j+1] = m

                # list[j],list[j+1] = list[j+1],list[j]   #直接表示交换
        
        n -= 1
    
    return list

test = Bubble_sort([7,2,5,1,4,4,0])
print(test)
                

