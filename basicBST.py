#make tree
#insert into tree
#find stuff in tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data < self.data:
            if self.left is None: #doesn't point to another node
                self.left = Node(data)
                return
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None: #doesn't point to another node
                self.right = Node(data)
                return
            else:
                self.right.insert(data)

    def search(self, value):
        if value == self.data:
            return str(value)+" was found in the BST"
        elif value < self.data:
            if self.left: #is not None (i.e. node points to another node)
                return self.left.search(value)
            else:
                return str(value)+" was not found in the BST"
        elif value > self.data:
            if self.right: #is not None (i.e. node points to another node)
                return self.right.search(value)
            else:
                return str(value)+" was not found in the BST"


    def PrintTree(self):
        if self.left: #is not None (i.e. node points to another node)
            self.left.PrintTree()
        print(self.data)
        if self.right: #is not None (i.e. node points to another node)
            self.right.PrintTree()




root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.PrintTree()
print(root.search(19))
print(root.search(69))

