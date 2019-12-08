'''

returning the square root element of a node
so if one pointer is pointing to the 4th node the other pointer must point
to the 2nd node

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

    def sqrt(self):
        a = self.head
        b = self.head
        count = 0
        lyst = []
        while a != None:
            c =+ 1
            lyst.append(c**2)
            if c in lyst:
                b = self.next 
            a = self.next
        print(b)

    
    def SqrtPos(self):
        current = self.head
        sqrt = None
        i =1
        j = 1
        while current != None:
            if i == j*j:
                if sqrt == None:
                    srqt= self.head
                else:
                    sqrt = srqt.getNext
                j = j + 1
            i = i+1
            current = current.next
        return sqrt.getData()


n1 = Node(10);n2 = Node(1);n3 = Node(519);n4 = Node(9);n5 = Node(11);
n6 = Node(16);n7 = Node(321);n8 = Node(451);n9 = Node(31);n10 = Node(109)
n1.next=n2;n2.next=n3;n3.next=n4;n4.next=n5;n5.next=n6;
n6.next=n7;n7.next=n8;n8.next=n9;n9.next=n10

l1 = LinkedList(n1)
l1.SqrtPos()


    
            
        
        
            
        



    
