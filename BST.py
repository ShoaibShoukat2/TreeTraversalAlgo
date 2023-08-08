

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None



def insert(root,key):
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)

    return root


#Create Binary Search Tree
if __name__ == '__main__':
    root = None
    root = insert(root,8)
    root = insert(root,3)
    root = insert(root,9)
    root = insert(root,1)
