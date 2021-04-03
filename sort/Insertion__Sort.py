#插入排序 时间复杂度O(n^2)

def Insert_sort(list1):
    for i in range(1,len(list1)):
        current = list1[i]      #取得值与位置
        position = i

        while position > 0 and list1[position-1] > current:     #与前项进行比较 去尝试寻找 比自己小的值与位置
            list1[position] = list1[position-1]
            position -= 1
        
        list1[position] = current
    
    return list1

print(Insert_sort([4,5,2,9,16,20,1]))