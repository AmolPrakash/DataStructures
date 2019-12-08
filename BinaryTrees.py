import queue
class BTNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data
    
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left

class BT:
    def __init__(self, root = None):
        self.root = root

        
    def inorder(self,root):
        #left -->root --> right 
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
    def postorder(self,root):
        #left -->root --> right 
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data)

    def preorder(self,root):
        #left -->root --> right 
        if root is None:
            return
        print(root.data)
        self.inorder(root.left)
        self.inorder(root.right)
    
    def size(self, root):
        if root is None:
            return 0
        q = queue.Queue()
        q.put(root)
        c = 0
        while(not q.empty()):
            temp = q.get()
            c += 1
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)            
        return c
    
    def levelorder(self, root):
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        while(not q.empty()):
            temp = q.get()
            print (temp.data)
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
            
    def sizeRec(self,node):
        if root is None:
            return
        return 1 + self.sizeRec(root.left)+ self.sizeRec(root.right)
    

    def search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        left = self.search(root.left, data)
        if left:
            return left
        right = self.search(root.right, data)
        return right

    def findMax(self, root):
        if root is None:
            return 0
        lmax = self.findMax(root.left)
        rmax = self.findMax(root.right)
        return max(root.data, lmax, rmax)

    def deepest(self, root):
        if root is None:
            return root
        q = queue.Queue()
        q.put(root)
        while(not q.empty()):
            temp = q.get()
            print (temp.data)
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
        print (temp.data)

    def height(self, root):
        if root is None:
            return 0
        q = Queue.Queue()
        c = 0
        q.put(root)
        special = BTNode("$")
        q.put(special)
        while(not q.empty()):
            temp = q.get()
            if temp.data == "$":
                c += 1
                if not q.empty():
                    q.put(special)
            else:
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
        return c

    def levelwithmaxsum(self, root):
        if root is None:
            return float("-inf"), -1
        q = queue.Queue()
        c = 0
        maxSum = float("-inf")
        maxLevel = 0
        q.put(root)
        special = BTNode("$")
        q.put(special)
        currentLevelSum = 0
        while(not q.empty()):
            temp = q.get()
            if temp.data == "$":
                c += 1
                if not q.empty():
                    q.put(special)
                if maxSum < currentLevelSum:
                    maxSum = currentLevelSum
                    maxLevel = c
                currentLevelSum = 0
            else:
                currentLevelSum += temp.data
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
        return maxSum, maxLevel

    def lca(self, root, A, B):
        if not root:
            return None
        if root.data == A or root.data == B:
            return root
        l = self.lca(root.left, A, B)
        r = self.lca(root.right, A, B)
        if l and r:
            return root
        if l:
            return l
        return r
     
    
         
count = 1      
node1 = BTNode(6);node2 = BTNode(9);node3 = BTNode(2);node4 = BTNode(30);node5 = BTNode(35)

node1.left = node2; node1.right = node3
node3.left = node4
node4.right = node5

bt = BT(node1)
print ("______________")
bt.inorder(node1)
print ("______________")
bt.postorder(node1)
print ("______________")
bt.preorder(node1)
print ("______________")

print (bt.size(node1))
print (bt.search(node1,30))
print(bt.findMax(node1))
print(bt.deepest(node1))
print(bt.levelwithmaxsum(node1))
print (bt.lca(node1,35,9).data)

