'''
binary search trees
'''

class BSTNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root = None):
        self.root = root

    def searchRec(self,root, data):
        if not root:
            return None
        if root.data == data:
            return root
        if root.data > data:
            return search(root.left, data)
        return search(root.right,data)
    
    def search(self,root, data):
        if not root:
            return None
        current = root
        while (current != data):
            if current.data == data:
                return current
            if current.data> data:
                current = current.left
            else:
                current = current.right
        return None


    def findMax(self, root):
        if not root:
            return None
        if root.right is None:
            return root
        return self.findMax(root.right)
    
    def maxIt(self,root):
        if not root:
            return None
        if root.right != None:
            root = root.right
        return root 
        
    def findMin(self,root):
        if not root:
            return None
        if root.left is None:
            return root
        return self.findMin(root.left)
    
    def minIt(self, root):
        if not root:
            return None 
        while root.left !=  None:
            root = root.left
        return root 

    def rangePrint(self, root, A, B):
        if not root:
            return None
        if root.data >= A :
            self.rangePrint(root.left, A, B)
        if A <= root.data <= B:
            print (root.data)
        if root.data <= B:
            self.rangePrint(root.right, A, B)

    def ascend(self,root):# inorder
        #left -->root --> right 
        if root is None:
            return
        self.ascend(root.left)
        print(root.data)
        self.ascend(root.right)
        
    def desend(self,root):#inorder
        #right -->root -->left
        if root is None:
            return
        self.desend(root.right)
        print(root.data)
        self.desend(root.left)

    def kthSmallest(self,root,k):#inorder
        #right -->root -->left
        if root is None:
            return
        l = self.kthSmallest(root.left , k)
        if l:
            return l
        global count
        count = count + 1
        if count == k:
            return root
        return self.kthSmallest(root.right, k)
    
    def kthBiggest(self,root,k):
        if root is None:
            return
        r = self.kthBiggest(root.right , k)
        if r:
            return r
        global count
        count = count + 1
        if count == k:
            return root
        return self.kthBiggest(root.left, k)

    def lca(self, root, A, B):
        if not root:
            return None
        if A < root.data and B < root.data:
            l = self.lca(root.left, A, B)
            if l:
                return l
        if  A <= root.data <= B:
            return root
        if A > root.data and  B > root.data:
            r = self.lca(root.right, A, B)
            return r
     
        
node1 = BSTNode(6);node2 = BSTNode(2);node3 = BSTNode(10);node4 = BSTNode(2);
node5 = BSTNode(15);node6 = BSTNode(4);node7 = BSTNode(12);node8 = BSTNode(3);
node9 = BSTNode(5);
count = 0 
node1.left = node2; node1.right = node3
node2.right = node6; node6.left= node8;node6.right=node9
node3.right=node5;node5.left = node7

count = 0  
bt = BST(node1)
print(bt.lca(node1,3,3).data)
