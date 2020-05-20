class Deque:
    """this is Deque implementation in python"""
    def __init__(self,size):
        self.size = size
        self.array = []*self.size
    def addFront(self,item):
        self.array.append(item)
    def addRear(self,item):
        self.array.insert(0,item)
    def removeFront(self):
        self.array.pop()
    def removeRear(self):
        self.array.pop(0)
    def isEmpty(self):
        return self.array == []*self.size
    def size(self):
        return len(self.array)


d = Deque(5)
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
d.addRear(11)
d.addRear(44)
print(d.isEmpty())
print(d.size)
print(d.array)
d.removeRear()
print(d.array)
d.removeFront()
print(d.array)
