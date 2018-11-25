class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
    
    def isempty(self):
        return (self.value == None)
    
    def append(self,v): #similar to insertAtEnd
        if self.value == None:
            self.value = v
            return
        temp = self
        while(temp.next!=None):
            temp = temp.next
        temp.next = node(v)
        return
    
    def display(self):
        if self.value == None:
            print("Empty List")
            return
        if self.next == None:
            print(self.value)
            return
        temp = self
        while(temp.next!= None):
            print(temp.value)
            temp = temp.next
        print(temp.value)
        return

    def insertAtBeginning(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = node(v)
        (self.value ,newnode.value) = (newnode.value,self.value)
        (self.next,newnode.next) = (newnode,self.next)
        return

    def insertAtEnd(self,v): #similar to append
        if self.isempty():
            self.value = v
            return
        temp = self
        while(temp.next != None):
            temp = temp.next
        newnode = node(v)
        temp.next = newnode
        return

    def deleteAtBeginning(self):
        if self.isempty():
            print("List is empty!!!")
            return
        if self.next == None:
            self.value = None
            return
        else:
            self.value = self.next.value
            self.next = self.next.next
            return

    def deleteAtEnd(self):
        if self.isempty():
            print("List is Empty!!Deletion is not possible")
            return
        if self.next == None:
            self.value = None
            return
        temp1 = self
        while(temp1.next!= None):
            temp2 = temp1
            temp1 = temp1.next
        temp2.next = None
        return
        
    def deleteSpecificNode(self,v):
        if self.isempty():
            print("List is Empty!!Deletion is not possible")
            return
        if self.next == None:
            if self.value == v:
                self.value = None
                return
        temp1 = self
        while(temp1.next != None):
            temp2 = temp1
            temp1 = temp1.next
            if temp1.value == v:
                temp2.next = temp2.next.next
                return
        print("reached end of the list."+str(v)+" is not found")
        return



"""
l = node(5)
l.append(4)
l.append(3)
l.append(2)
l.append(1)
l.display()
print("\n")
l.insertAtBeginning(6)
l.insertAtEnd(7)
l.display()
print("\n")
l.deleteAtBeginning()
l.display()
print("\n")
l.deleteAtEnd()
l.display()
print("\n")
l.deleteSpecificNode(3)
l.deleteSpecificNode(9)
print("\n")
l.display()
"""
