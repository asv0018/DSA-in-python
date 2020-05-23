class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def traversePreorder(self):
        print(self.val,end="")
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val,end="")
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.val,end="")

#initialising the instance
root = Node("eat curd rice\n")
root.left = Node("eat rasam\n")
root.right = Node("eat sambhar rice\n")
root.left.left = Node("eat uppinkai rice\n")

print("\npre order traversal:",end="\n")
root.traversePreorder()
print("\nin order traversal:",end="\n")
root.traverseInorder()
print("\npost order traversal:",end="\n")
root.traversePostorder()
