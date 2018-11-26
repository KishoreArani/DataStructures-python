class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self,data):
        if self.rear == None:
            self.front = self.rear = node(data)
            return
        self.rear.next = node(data)
        self.rear = self.rear.next

    def deQueue(self):
        if self.front == None:
            print("Empty Queue!!Deletion is not possible")
            return
        self.front = self.front.next

    def display(self):
        if self.front == None:
            print("Empty Queue!!")
            return
        temp = self.front
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
        return

"""
l = Queue()
l.display()
l.enQueue(4)
l.display()
l.enQueue(5)
l.enQueue(6)
l.enQueue(7)
l.enQueue(8)
print("\n")
l.display()
l.deQueue()
print("\n")
l.display()
l.deQueue()
l.deQueue()
print("\n")
l.display()
"""
