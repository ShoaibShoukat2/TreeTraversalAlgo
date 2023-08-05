



class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


#left root right
def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.leftChild)
        print(root.data)
        InOrderTraversal(root.rightChild)


# root left right

def PreOrderTraversal(root):
    if root:
        print(root.data)
        PreOrderTraversal(root.leftChild)
        PreOrderTraversal(root.rightChild)


def PostorderTraversal(root):
   if root:
      PostorderTraversal(root.leftChild)
      PostorderTraversal(root.rightChild)
      print(root.data)


if __name__ == "__main__":
    
    root = Node(2)
    root.leftChild = Node(4)
    root.leftChild.rightChild = Node(5)
    root.rightChild = Node(7)
    root.rightChild.leftChild = Node(6)
    root.rightChild.leftChild.leftChild = Node(9)
    root.rightChild.rightChild = Node(10)
    root.rightChild.rightChild.leftChild = Node(12)
    root.rightChild.rightChild.rightChild = Node(14)

    InOrderTraversal(root)
