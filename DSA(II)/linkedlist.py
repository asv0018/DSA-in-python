class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    #initialising the class with an instance
    llist = LinkedList()

    #assign data values
    First = Node(100)
    Second = Node(200)
    third = Node(300)
    fourth = Node(400)
    #connect nodes
    llist.head = First
    First.next = Second
    Second.next = third
    third.next = fourth
    #print the linked list data
    while llist.head != None:
        print(llist.head.data, end=" ")
        llist.head = llist.head.next
