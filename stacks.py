'''
STACKS
'''
import random 
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class Stack:
    stackSize = 0 
    def __init__(self, node = None):
        self.top = node
        self.stackSize = 0
        
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.stackSize += 1
        
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        self.stackSize =- 1
        return temp.data

    def peep(self):
        return self.top

    def size(self):
        return self.stackSize

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    

# seed is like a key to generate random values
# if same seed value is passed the the same sequence is generated
random.seed(1)

stack = Stack ()

for i in range(10):
    element = random.randint(0,99)
    print("pushing ", element )
    stack.push(element)

for i in range (9):
    print ("popping", stack.pop())
    print(stack.size())
print (stack.isEmpty)



    
    

