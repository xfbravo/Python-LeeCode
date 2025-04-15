import random
class BiTree:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data is None:
            self.data=data
        elif data<=self.data:
            if self.left is None:
                self.left=BiTree(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            if self.right is None:
                self.right=BiTree(data)
            else:
                self.right.insert(data)
    def search(self,data):
        if self.data is None:
            return False
        elif data==self.data:
            return True
        elif data<self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(data)
    def adjust(self):
        if self.left is not None:
            self.left.adjust()
        if self.right is not None:
            self.right.adjust()
        if self.left is not None and self.right is not None:
            if self.left.data>self.right.data:
                temp=self.left
                self.left=self.right
                self.right=temp
    def prePrint(self):
        if self.left is not None:
            self.left.prePrint()
        print(self.data,end=" ")
        if self.right is not None:
            self.right.prePrint()
    def inPrint(self):
        print(self.data,end=" ")
        if self.left is not None:
            self.left.inPrint()
        if self.right is not None:
            self.right.inPrint()
    def postPrint(self):
        if self.left is not None:
            self.left.postPrint()
        if self.right is not None:
            self.right.postPrint()
        print(self.data,end=" ")

bit=BiTree()
for i in range(50):
    bit.insert(random.randint(1,100))
bit.prePrint()
print()
bit.postPrint()
print()
bit.inPrint()
print()
print(bit.search(50))
