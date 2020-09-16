#                     (1)
#                   /    \
#                  2)    (2)
#                 / \    / \
#               (5) (6) (6) (5)
# Write a program to confirm above tree nodes are symmetric

#
# In the console, run: 
#     python symmeticTree.py or 
#     symmeticTree.py
#
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isLeaf(node):
    return node.left == None and node.right == None

def isSymmetric(node1, node2):
    if node1 == None and node2 == None:
        return True

    if (node1 == None and node2 != None) or (node1 != None and node2 == None): 
        return False

    if node1.value != node2.value:
        return False
    
    if isLeaf(node1) and isLeaf(node2):
        return True
    else:
        return isSymmetric(node1.left, node2.right) and isSymmetric(node1.right, node2.left)

def symmetricTree(node):
    return isSymmetric(node.left, node.right)

    
    
# Test methods 
def testSymmMetricTree():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(4)
    root.left.left = Node(3)
    root.right.right = Node(3)
    assert(symmetricTree(root))
    root.left.right = Node(2)
    assert(symmetricTree(root) == False)
    root.right.left = Node(2)
    print("Running testsymmetricTree passed!")

def testSymmetricTree2():
    root = Node(1)
    assert(symmetricTree(root))
    
    left1 = Node(2)
    right1 = Node(2)
    root.left = left1
    assert(symmetricTree(root) == False)
    
    root.right = right1
    assert(symmetricTree(root))
    
    root.left.left = Node(5)
    root.left.right = Node(6)
    assert(symmetricTree(root) == False)
    
    root.right.left = Node(6)
    assert(symmetricTree(root) == False)
    
    root.right.right = Node(5)
    assert(symmetricTree(root))
    
    print("Running testsymmetricTree2 passed!")

# run the test methods
testSymmMetricTree()
testSymmetricTree2()
