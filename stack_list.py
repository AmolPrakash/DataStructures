'''
stacks with lists
'''
import random

class Stack:

    def __init__(self, capacity = 15):
        self.array = []
        self.capacity = capacity

    def push(self, data):
        if len(self.array) < self.capacity:
            self.array.append(data)
        else:
            print("stack overflow")

    def ifEmpty(self):
        if len(array) == 0:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            print ("stack underflow")
            return 
        temp = self.array.pop
        return temp

    def peep(self):
        if self.isEmpty():
            print ("stack underflow")
            return 
        temp = self.array[-1]
        return temp

    def printer(self):
        for i in self.array:
            print(i) 


stack = Stack()
        

for i in range(7):
    element = random.randint(0,99)
    print("pushing ", element )
    stack.push(element)

print (stack.array,stack.capacity)

        
