NullPointer = -1 #Constant
RootPointer = 0 #Integer
FreePtr = 0 #Integer

Tree = [] # This is the 'array'

def InitiliseTree():
    """
    This Initialises the tree with 7 instances for the binary tree.
    To follow the pseudocode I need to use global variables liberally.
    """
    global NullPointer
    global RootPointer
    RootPointer = NullPointer
    FreePtr = 0
    for Index in range(6):
        Tree.append([Index + 1,0.0,-1])
    Tree.append([NullPointer,0.0,-1])

def InsertNode(NewItem):
    """
    I've swapped the if FreePtr != NullPointer because Pycharm complained at me. Rightly so.
    The Hodder book was better here and so I raised an error if the array is full. Originally it just did nothing.
    If that's annoying change it to a print statement.
    """
    global FreePtr # Passed by ref
    global NullPointer # Passed by ref
    global RootPointer
    if FreePtr == NullPointer:
        raise Exception("Sorry, this binary Tree array is full")
    else:  # Space in the array
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr][0]
        Tree[NewNodePtr][1] = NewItem
        Tree[NewNodePtr][0] = NullPointer
        if RootPointer == NullPointer: # Check if empty tree
            RootPointer = NewNodePtr
        else:
            ThisNodePtr = RootPointer # Start at the root of the tree
            while ThisNodePtr != NullPointer:
                PreviousNodePtr = ThisNodePtr
                if Tree[ThisNodePtr][1] > NewItem:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr][0]
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr][2]
            if TurnedLeft == True:
                Tree[PreviousNodePtr][0] = NewNodePtr
            else:
                Tree[PreviousNodePtr][2] = NewNodePtr


def FindNode(SearchItem):
    """
    If it can't find the item then it will return -1.
    """
    global RootPointer
    global NullPointer
    ThisNodePtr = RootPointer
    while ThisNodePtr != NullPointer and Tree[ThisNodePtr][1] != SearchItem:
        if Tree[ThisNodePtr][1] > SearchItem:
            ThisNodePtr = Tree[ThisNodePtr][0]
            print("Went left",ThisNodePtr)
        else:
            ThisNodePtr = Tree[ThisNodePtr][2]
            print("Went right",ThisNodePtr)
    return ThisNodePtr



InitiliseTree()

InsertNode(2.5)
InsertNode(5.7)
InsertNode(3.3)
InsertNode(7.5)
InsertNode(11.11)
InsertNode(12.4)
InsertNode(15.4)
# #InsertNode(3.4)

for i in Tree: print(i)

print(FindNode(7.5))
