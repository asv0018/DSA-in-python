class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def inorder(root):

    if root is not None:
        # traverse left
        inorder(root.left)
        # traverse root
        print(str(root.key)+"->",end=" ")
        # traverse right
        inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)

    return node

def deleteNode(root,key):

    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:

        #if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if the node has two children
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

if __name__ == "__main__":

    root = None
    root = insert(root,8)
    root = insert(root,3)
    root = insert(root,1)
    root = insert(root,6)
    root = insert(root,7)
    root = insert(root,10)
    root = insert(root,14)
    root = insert(root,4)

    # checking the tree  by inorder traversal
    print("The inorder traversal: ",end=' ')
    inorder(root)
    print()
    # Time to delete a element
    root = deleteNode(root,10)

    # Now traversal through the tree
    print("After deleting th element %d, from the inorder traversal is: ",10)
    inorder(root)
