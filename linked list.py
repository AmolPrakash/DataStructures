'''
LINKED LIST

unless mentioned the list is alwasy a single linked list

'''

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def setData(self,n):
        self.data = n 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

class LinkedList:
    def __init__(self, node = None):
        self.head = node

    def length(self):
        current = self.head
        c = 0
        while current != None:
            c+=1
            current = current.next
        return c
    
    def printList(self):
        current = self.head
        while current != None:
            print (current.data)
            current = current.next

    def searchList(self, element):
        current = self.head
        while current != None:
            if current.data == element:
                return current
            current = current.next

    #inserting at the begining
    def insertAtBegining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    #inserting at the  ending
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return 
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node

    def insert(self, position, data):
        if position <= 1:
            self.insertAtBegin(data)
            return
        node = Node(data)
        c = 1
        current = self.head
        while(current != None and c < position-1):
            current = current.next
            c += 1
        if current is None:
            self.insertAtEnd(data)
            return
        node.next = current.next
        current.next = node


    def deleteFromFirst(self):
        temp = self.head
        if self.head:
            self.head = self.head.next()
        return temp

    def deleteFromEnd(self):
        current = self.head
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None
        return current

    def findnkth(self, k):
        b1 = self.head
        b2 = self.head
 
        while(b1):
            c = k
            while(c and b1):
            	b1 = b1.next
            	c -= 1
            b2 = b2.next
        return b2

    def circularCheck(self):
        p1 = self.head
        p2 = self.head
        while p1 and p2 and p2.next :
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

    def findCycleLength(self):
        fp = self.head
        sp = self.head
 
        while(fp):
            fp = fp.next
            if fp == sp:
            	break
            if fp:
            	fp = fp.next
            else:
            	return 0
            sp = sp.next
            if fp == sp:
            	break
        if fp in None:
            return 0
         
        c = 0
        fp = fp.next
        while sp != fp:
        	c += 1
        	fp = fp.next
        return c
    def findCycleLength(self):
        fp = self.head
        sp = self.head
 
        while(fp):
            fp = fp.next
            if fp == sp:
            	break
            if fp:
            	fp = fp.next
            else:
            	return None 
            sp = sp.next
            if fp == sp:
            	break
             
        if fp is None:
            return None
        
        fp = self.head
        
        while fp != sp:
            fp = fp.next
            sp = sp.next
        return fp
         
    
                 
            
            
    
def main():

    node1 = Node(2)
    node2 = Node(6)
    node3 = Node(10)
    node4 = Node(8)
    node5 = Node(0)

    node1.setNext(node2)
    node2.setNext(node3)
    node3.setNext(node4)

    #print (node1.getNext().getData())
    
    l1 = LinkedList()
    l1.printList()
    l1.insertAtBegining(5)
    
    l1.insertAtEnd(94)
    l1.insertAtEnd(99)
    l1.insert(5,3)
    l1.printList()
    l1.deleteFromEnd()
    l1.printList()
    result = l1.deleteFromEnd()
    ll.printList()
    if result:
        print (result.data)
    print (l1.length())
    print(l1.printList())

##    result = l1.searchList(10)
##    if result:
##        print (result.data)
##    else:
##        print("not found ")
    ll = LinkedList()
    ll.insertAtEnd(5)
    ll.insertAtEnd(55)
    ll.insertAtBegin(10)
    ll.insert(1, 99)
    ll.insert(3, 6)
    result = ll.delete(4)
    ll.printList()
    if result:
        print (result.data)
    
##    
    

    

if __name__ == "__main__" :
    main()
        
