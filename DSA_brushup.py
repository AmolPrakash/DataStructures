#### remebering DSA things 
##
###factrial
##def fact(x):
## 	if x == 0:
## 		return 1
## 	return x * fact(x-1)
##
###towerOfHanoi 
##
##def tower(num,start = 1, end = 3):
##	if num:
##		tower(num-1,start, 6-start-end)
##		print ("move disk %d from peg %d to peg %d"%(num, start,end))
##		tower(num-1,6-start-end,end)

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next
    
    def setNext(self,next):
        self.next = next
        
    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

class LinkedList:
    def __init__(self,node = None):
        self.head = node

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext
        return count
    def printList(self):
        current = self.head
        while current != None:
            print (current.data)
            current = current.next
        

node1 = Node(2)
node2 = Node(6)
node3 = Node(10)
node4 = Node(8)


node1.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)






        
