class Node:
    def __init__(self,data = None,right = None,left = None):
        self.data = data
        self.right = right
        self.left = left

    def isEmpty(self):
        return (self.data == None)

    def addChild(self,data):
        if self.isEmpty():
            self.data = data
            return
        temp = self
        while(True):
            if temp.right == None and temp.left == None:
                if data > temp.data:
                    temp.right = Node(data)
                    return
                if data < temp.data:
                    temp.left = Node(data)
                    return
            if data > temp.data:
                if temp.right == None:
                    temp.right = Node(data)
                    return
                temp = temp.right
            if data < temp.data:
                if temp.left == None:
                    temp.left = Node(data)
                    return
                temp = temp.left

    def inOrder(self):
        temp = self
        if temp.left:
            temp.left.inOrder()
        print(temp.data,sep = " ",end = " ")
        if temp.right:
            temp.right.inOrder()

    def preOrder(self):
        temp = self
        print(temp.data,sep = " ",end = " ")
        if temp.left:
            temp.left.preOrder()
        if temp.right:
            temp.right.preOrder()

    def postOrder(self):
        temp = self
        if temp.left:
            temp.left.postOrder()
        if temp.right:
            temp.right.postOrder()
        print(temp.data,sep = " ",end = " ")

"""
l = Node()
l.addChild(10)
l.addChild(4)
l.addChild(12)
l.addChild(3)
l.addChild(5)
l.addChild(11)
l.addChild(13)
l.inOrder()
print()
l.preOrder()
print()
l.postOrder()
print()
"""
