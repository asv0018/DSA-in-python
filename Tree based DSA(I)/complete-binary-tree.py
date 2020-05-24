#the main difference between complete binary tree
#and full binary tree is that,complete binary tree
#should have all the leaf element to left
#full binary tree is expected to have either 2 childrens
#or no children.

#therefore the difference lies here all the complete
#binary tree need not be a full binary tree and viceversa

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def isComplete(root,index,numberNodes):
    if root is None:
        return True
    if index >= numberNodes:
        return False
    return(isComplete(root.left,2*index + 1,numberNodes) and isComplete(root.right,2*index + 2,numberNodes))

def nodeCount(root):
    if root is None:
        return 0
    return (1 + nodeCount(root.left) + nodeCount(root.right))

root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

if isComplete(root,0,nodeCount(root)):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
