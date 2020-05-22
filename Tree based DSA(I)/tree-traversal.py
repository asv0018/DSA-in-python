class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.value = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.value)+"->",end = "")
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.value)+"->",end = "")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value)+"->",end = "")

# creation of a heap
root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)

# traversal of node
print("Inorder traversal ")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)
