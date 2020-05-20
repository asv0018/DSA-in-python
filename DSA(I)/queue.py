#implementation of Queue in python3
class Queue:
    #initialisation of queue
    def __init__(self):
        self.queue = []

    #add an element
    def enqueue(self,item):
        self.queue.append(item)

    #remove an element
    def dequeue(self):
        if len(self.queue)<1:
            return None
        else:
            return self.queue.pop(0)

    #display the queue
    def display(self):
        print(self.queue)

    #return the size
    def size(self):
        return len(self.queue)

#main

#creating an instance
q=Queue()

#enqueueing the numbers by looping in for method
for i in range(10):
    q.enqueue(i)

#display of the Queue
q.display()

#appling dequeueing on the queue
q.dequeue()

print("After removing an element")
q.display()

#creating another instance
tasks=Queue()

#adding tasks into the task-scheduling
tasks.enqueue('Read the book "How to read a book!?"')
tasks.enqueue('Watch the movie "how to learn JAVA in a day!"')
tasks.enqueue('Program your pc to auto-upload the assignments to Moodle')

#view all the tasks
tasks.display()

#to check which task is first ?
print("The task you need to do now is : ",str(tasks.dequeue()))

#if first task is cleared,what next?
tasks.display()

#to check what to do next
print("The task you need to do now is : ",str(tasks.dequeue()))

#check the remaining tasks
tasks.display()

#to check what next
print("The task you need to do now is : ",str(tasks.dequeue()))

#to check anything if there is any
tasks.display()
