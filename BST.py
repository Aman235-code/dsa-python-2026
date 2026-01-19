class Node:
    def __init__(self, value):
        self.left = None
        self.right = None 
        self.data = value

def insert( root, value):
    if root is None:
        return Node(value)
        
    if root.data == value:
        return root 
        
    if value < root.data:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root

def get_successor(root):
    root = root.right
    while root is not None and root.left is not None:
        root = root.left
    return root

def delete(root, value):
    if root is None:
        return root 
    
    if root.data > value:
        root.left = delete(root.left, value)
    elif root.data < value:
        root.right = delete(root.right, value)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = get_successor(root)
            root.data = successor.data
            root.right = delete(root.right, successor.data)

    return root

def search(root, value):
    if root is None:
       print("Element not found")
       return
        
    if root.data == value:
        print("Element found")
        return
        
    if value < root.data:
       search(root.left, value)
       return

    else:
       search(root.right, value)

    
def inOrder(root):
    if(root!= None):
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)
# root.left.left = Node(12)
# root.left.right = Node(18)
# inOrder(root)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)
inOrder(root)

delete(root, 30)
print("/n")
inOrder(root)
