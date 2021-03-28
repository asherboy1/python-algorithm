class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item): #O(n)
        return self.queue.insert(0,item)
    
    def dequeue(self):  #O(1)
        return self.queue.pop()
    
    def isEmpty(self):
        return self.queue == []
    
    def size(self):
        return len(self.queue)