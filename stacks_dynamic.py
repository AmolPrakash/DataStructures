'''
creating stack using dyanmic lists
'''
import random

class Stack:

    def __init__(self, capacity = 1):
        self.array = []
        self.capacity = capacity

    def push(self, data):
        if len( self.array) == self.capacity:
            self.resize()
        temp = self.array.append(data)
        return temp

    def pop(self):
        if 2*len(self.array) <= self.capacity:
            self.resize()
        self.array.pop
        
    def peep(self):
        if self.isEmpty():
            print ("stack underflow")
            return 
        temp = self.array[-1]
        return temp
    
    def size(self):
        return len(self.array)

    def getCapacity(self):
        return self.capacity

    
    def resize(self):
        if len(self.array) == self.capacity:
            self.capacity = self.capacity* 2
            self.array = list(self.array)

        elif 2*len(self.array) <= self.capacity:
            self.capacity = self.capacity//2
            self.array = list(self.array)

random.seed(2)
stack = Stack(1)
for i in range(5):
    element = random.randint(0, 99)
    stack.push(element)


print (stack.size())
print (stack.getCapacity())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print (stack.size())
print (stack.getCapacity())


