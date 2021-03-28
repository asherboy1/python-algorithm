
from node import Node

class OrderList:
    def __init__(self):
        self.head = None
    
    def add(item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:        #查找插入位置
            if  item <= current.getData():
                found = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)           #创建节点
        if previous == None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found and current.getData() > item:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found
            