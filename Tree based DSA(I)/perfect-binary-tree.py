class Newnode:
    def __init__(self,k):
        self.key = k
        self.right = None
        self.left  = None

def calculateDepth(node):
    d = 0
    while node is not None:
        d+=1
        node = node.left
    return d

def isPerfect(root,d,level = 0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return d == (level + 1)
    if root.left is None or root.right is None:
        return False
    return isPerfect(root.left,d,level + 1) and isPerfect(root.right,d,level + 1)

root = Newnode(1)
root.left = Newnode(2)
root.right = Newnode(3)
root.left.left = Newnode(4)
root.left.right = Newnode(5)
#till here it is not a perfect binary tree

root.right.right = Newnode(6)
root.right.left = Newnode(7)
#now is a perfect binary tree

if isPerfect(root,calculateDepth(root)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
