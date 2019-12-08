'''
implementation of queues using dynamic arrays


'''

class Queue:

    def __init__(self, length = 3):
        self.queue = []
        self.length = length
        self.first = None
        self.last = None
        self.size = 0

    def enQueue(self, data):
        #print ("before : " + str(self.queue))
        if self.size >= self.length:
            self.resize()
        self.queue.append(data)
        if self.first is None: 
            self.first = data
            if self.last is None:
                self.last = data
        else:
            self.last = data
        self.size = self.size + 1 
        print ("after : " +str(self.queue))

    def deQueue(self):
        
        if self.size <= 0:
            print("nothing in queue")
            return
        else:
            self.queue.pop(0)
            self.size -= 1
            print (self.queue)
            self.first = self.queue[0]
            self.last = self.queue[-1]
        if self.size*2 == self.length:
            self.resize()
                
    def resize(self):
        if self.size >= self.length:
            temp = list(self.queue)
            self.length = 2*self.length
            self.queue = temp 
        else:
            temp = list(self.queue)
            self.length = self.length//2
            self.queue = temp


queue1 = Queue()
queue1.enQueue(1)

print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(2)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(3)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(4)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(5)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(6)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.enQueue(7)
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
#print (queue1)
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))
queue1.deQueue()
print ("front" + str(queue1.first))
print("back " + str(queue1.last))


    
