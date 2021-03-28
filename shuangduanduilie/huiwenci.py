#回文词

#--------------------------1
# from deque import Deque

# def huiwenci(str):
#     d = Deque()
#     flag = True
#     j = 0
#     for i in str:
#         d.addFront(i)
    
#     num = d.size() / 2
#     while j < int(num) and flag:
#         if d.removeFront() == d.removeRear():
#             j += 1
#             continue
#         else:
#             flag = False
    
#     if (d.size() == 1 or d.isEmpty()) and flag == True:
#         return True
#     else:
#         return False
    
# print(huiwenci("hlh"))
# print(huiwenci("ckamkcs"))
# print(huiwenci("hjkjh"))

#-----------------------------------2

from deque import Deque

def huiwenci(str):
    flag = False