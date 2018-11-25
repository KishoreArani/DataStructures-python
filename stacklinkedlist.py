class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        return

    def pop(self):
        if self.head == None:
            print("Stack is empty!! Deletion is not possible")
            return
        self.head = self.head.next
        return

    def display(self):
        if self.head == None:
            print("Stack in empty!!!")
            return
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
        return

