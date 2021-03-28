#约瑟夫问题
from queue import Queue

def hotpotato(namelist,num):
    q = Queue()
    for i in namelist:
        q.enqueue(i)
    
    while q.size() > 1:
        for j in range(num):
            q.enqueue(q.dequeue())
        
        q.dequeue()
    
    return q.dequeue()

name = ["Tony","Tom","lili","LUCY","ALEX","KIKI"]       #队首出队 默认炸弹在队首
name.reverse()
print(hotpotato(name,3))