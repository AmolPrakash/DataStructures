'''
QUEUues

first in first out
youll need to maintain two pointers

head and tail

'''

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class Queue:

    def __init__(self, node = None ):
        self.front = node
        self.rear = node
        self.length = 0

    def enQueue(self,data):
        node = Node(data)
        self.rear.next = node
        self.rear = node
        self.length =+ 1
        if self.front is None:
            self.front = node 

    def deQueue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front  =  self.front.next
        self.length =- 1
        if self.front is None:
            self.rear = None

        return temp.data

    
    
        
