class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,prevNode,newData):
        if prevNode is None:
            print("Thes given previous node must in LinkedList")
            return
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def insertAtEnd(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode

    def deleteNode(self,pos):
        if self.head == None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None

    def printlink(self):
        temp = self.head
        while (temp):
            print(str(temp.data)+" ",end = "")
            temp = temp.next


if __name__ == '__main__':
    link = LinkedList()
    link.insertAtEnd(1)
    link.insertAtBeginning(2)
    link.insertAtBeginning(3)
    link.insertAtEnd(4)
    link.insertAfter(link.head.next,5)
    link.printlink()
    #link.deleteNode(3)
    #link.printlink()
