class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

def isFullTree(root):
    if root is None:
        return true
    elif root.left is None and root.right is None:
        return true
    elif root.left is not None and root.right is not None:
        return(isFullTree(root.left) and isFullTree(root.right))
    else:
        return False

#initialising the node:
root = Node(1)
root.left = Node(3)
root.right = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = node(6)
root.left.left.right = Node(7)

if isFullTree(root):
    print("The tree id is s full binary tree")
else:
    print("The tree id is not a full binary tree")
