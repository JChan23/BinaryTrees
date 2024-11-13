class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def search(self, value):
        if value == self.data:
            return f"{value} was found in the BST"
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.search(value)
            else:
                return f"{value} was not found in the BST"
        else:
            if self.rightChild:
                return self.rightChild.search(value)
            else:
                return f"{value} was not found in the BST"

    def printtree(self):
        if self.leftChild:
            self.leftChild.printtree()
        print(self.data),
        if self.rightChild:
            self.rightChild.printtree()

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.printtree()
print(root.search(7))
print(root.search(14))
