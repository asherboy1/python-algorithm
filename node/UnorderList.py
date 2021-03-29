#仅对第一个结点有效
from node import Node
class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):     #从链表头 加入
        temp = Node(item)
        temp.setNext(self.head)     #注意逻辑 次序  否则结果严重
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = curent.getNext()
            count += 1

        return count
    
    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() != item:
                current = current.getNext()
            else:
                found = True
        
        return found
    
    def remove(self,item):
        previous = None
        current = self.head
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def apend(self,item):
        current = self.head
        while current != None:
            if current.getNext() == None:
                current.setNext(item):
                current = current.getNext()
                current.setNext(None)

                
        
