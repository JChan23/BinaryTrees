class Node:
    def __init__(self, data, left, right):
        self.__DataValue = data  # string
        self.__LeftPointer = left  # integer
        self.__RightPointer = right  # integer

    def DataValueGetter(self):
        return self.__DataValue

    def LeftPointerGetter(self):
        return self.__LeftPointer

    def RightPointerGetter(self):
        return self.__RightPointer

    def LeftPointerSetter(self, NewPointer):
        self.__LeftPointer = NewPointer

    def RightPointerSetter(self, NewPointer):
        self.__RightPointer = NewPointer

BinaryTreeArray = [Node(-1, -1, -1) for i in range(12)] # Array of type Node - initialise with blanks
NextNode = -1

def CreateTree(NodeData):
    global NextNode
    NextNode = 0
    BinaryTreeArray[NextNode] = Node(NodeData, -1, -1)  # pointers? must be an integer
    NextNode = NextNode + 1

def AttachLeft(NodeData, ParentNode):
    global NextNode
    BinaryTreeArray[NextNode] = Node(NodeData, -1, -1)  # pointers? must be an integer
    BinaryTreeArray[ParentNode].LeftPointerSetter(NextNode)   #parent tree left pointer points to new node. HOW TO ASSIGN TO A PRIVATE CLASS!!!
    NextNode = NextNode + 1

def AttachRight(NodeData, ParentNode):
    global NextNode
    BinaryTreeArray[NextNode] = Node(NodeData, -1, -1)  # pointers? must be an integer
    BinaryTreeArray[ParentNode].RightPointerSetter(NextNode)  #parent tree left pointer points to new node
    NextNode = NextNode + 1

def printLeftTree():
    pointer = 0
    while pointer != -1:
        print(BinaryTreeArray[pointer].DataValueGetter())
        pointer = BinaryTreeArray[pointer].LeftPointerGetter()

CreateTree("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)
printLeftTree()

def Traverse_leafs(node_index):
    if BinaryTreeArray[node_index].LeftPointerGetter() != -1:  # is not None (i.e. node points to another node)
        Traverse_leafs(BinaryTreeArray[node_index].LeftPointerGetter())
    if BinaryTreeArray[node_index].LeftPointerGetter() == -1 and BinaryTreeArray[node_index].RightPointerGetter() == -1:
        print(BinaryTreeArray[node_index].DataValueGetter())
    if BinaryTreeArray[node_index].RightPointerGetter() != -1:  # is not None (i.e. node points to another node)
        Traverse_leafs(BinaryTreeArray[node_index].RightPointerGetter())

Traverse_leafs(0)
