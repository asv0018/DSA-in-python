class CircularQueue:
    """"This is an implementation of CircularQueue in Python"""
    def __init__(self,size):
        self.size = size
        self.array = [None for i in range(size)]
        self.front = self.rear = -1
    def enqueue(self,value):
        if (self.rear+1)%self.size==self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.array[self.rear] = value
        else:
            self.rear = (self.rear+1)%self.size
            self.array[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.array[self.front]
            self.array.pop(self.front)
            self.front = self.rear = 1
            return temp
        else :
            temp = self.array[self.front]
            self.array.pop(self.front)
            self.front = (self.front+1)%self.size
            return temp
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.rear >= self.front:
            for i in range(self.front,self.rear):
                print(self.array[i],end = " ")
            print()
        else:
            for i in range(self.front,self.size):
                print(self.array[i],end = " ")
            for i in range(0,self.rear+1):
                print(self.array[i],end = " ")
            print()
        if ((self.rear+1)%self.size == self.front):
            print("Queue is Full")

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
