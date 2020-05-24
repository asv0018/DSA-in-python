class Node:
    def __init__(self,item):
        self.item = item
        self.left = self.right = None

class CalculateHeight:
    def __init__(self):
        self.calculateHeight = 0

def isHeightBalanced(root, calculateHeight):

    leftHeight = CalculateHeight()
    rightHeight = CalculateHeight()

    if root is None:
        return True

    l = isHeightBalanced(root.left,leftHeight)
    r = isHeightBalanced(root.right,rightHeight)

    calculateHeight.CalculateHeight = max(leftHeight.calculateHeight,rightHeight.calculateHeight) + 1
    if abs(leftHeight.calculateHeight - rightHeight.calculateHeight) <= 1:
        return l and r

    return False

# creating an instance...
calculateHeight = CalculateHeight()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
# validating is the tree balanced or unbalanced...
if isHeightBalanced(root,calculateHeight):
    print("The tree is balanced")
else:
    print("The tree is not balanced")
