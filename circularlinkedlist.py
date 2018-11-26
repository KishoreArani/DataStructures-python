class node:
    def __init__(self,value=None):
        self.value = value
        self.next = self
    
    def isEmpty(self):
        return self.value == None

    def append(self,v): #similar to insertAtEnd
        if self.isEmpty():
            self.value = v
            self.next = self
            return
        temp = self
        while(temp.next != self):
            temp = temp.next
        newnode = node(v)
        temp.next = newnode
        newnode.next = self
        return

    def display(self):
        if self.isEmpty():
            print("Empty List!!")
            return
        temp = self
        while(temp.next != self):
            print(temp.value)
            temp = temp.next
        print(temp.value)
        print(self.value)
        return

    def insertAtBeginning(self,v):
        if self.isEmpty():
            self.value = v
            self.next = self
            return
        newnode = node(v)
        self.value,newnode.value = newnode.value,self.value
        self.next,newnode.next = newnode,self.next
        return
    
    def deleteAtEnd(self):
        if self.isEmpty():
            print("List is Empty!!! Deletion is not possible")
            return
        if self.next == next:
            self.value = None
            self.next = None
            return
        temp = self
        while temp.next != self:
            temp2 = temp
            temp = temp.next
        temp2.next = self
        return

    def deleteAtBeginning(self):
        if self.isEmpty():
            print("LIst is Empty!! Deletion is not possible")
            return
        if self.next == self:
            self.value = None
            self.next = None
            return
        temp = self
        while temp.next != self:
            temp = temp.next
        self.value = self.next.value
        self.next = self.next.next
        temp.next = self
        return

    def deleteSpecificNode(self,v):
        if self.isEmpty():
            print("List is Empty!! Deletion is not possible!!")
            return
        if self.value == v:
            self.deleteAtBeginning()
            return
        temp1 = self
        while temp1.next != self:
            temp2 = temp1
            temp1 = temp1.next
            if temp1.value == v:
                temp2.next = temp2.next.next
                return
        print("Reached end of the list."+str(v)+" is not found")
        return


"""	    
l = node(50)
l.append(4)
l.append(5)
l.append(6)
l.append(8)
l.append(9)
l.append(10)
l.display()
print("\n")
l.deleteAtEnd()
l.display()
print("\n")
l.deleteAtBeginning()
l.display()
print("\n")
l.deleteSpecificNode(4)
l.display()
"""

