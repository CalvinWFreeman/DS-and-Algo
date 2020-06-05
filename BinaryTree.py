from typing import Callable 
import random

#Tree Node
class Node():
    def __init__(self, name : str, value: int, left : 'Node' = None , right : 'Node' = None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

#Class containing traversal methods for binary trees
class Traversal():
    @staticmethod
    def inOrderTraversal(node: Node, visit : Callable[[Node], None]):
        if(node != None):
            Traversal.inOrderTraversal(node.left, visit)
            visit(node)
            Traversal.inOrderTraversal(node.right, visit)

    @staticmethod
    def preOrderTraversal(node: Node, visit : Callable[[Node], None]):
        if(node != None):
            visit(node)
            Traversal.inOrderTraversal(node.left, visit)
            Traversal.inOrderTraversal(node.right, visit)

    @staticmethod
    def postOrderTraversal(node: Node, visit : Callable[[Node], None]):
        if(node != None):
            Traversal.inOrderTraversal(node.left, visit)
            Traversal.inOrderTraversal(node.right, visit)
            visit(node)

def createBinaryTree(depth: int):
    root = Node("root", random.randint(0, 11))
    currentDepth = 0

    def createChildren(node: Node, currentDepth: int, depthLimit: int):
        if(currentDepth < depthLimit):
            currentDepth += 1

            node.left = Node("leftChild", random.randint(0, 10))
            createChildren(node.left, currentDepth, depthLimit)

            node.right = Node("rightChild", random.randint(0, 10))
            createChildren(node.right, currentDepth, depthLimit)
    
    createChildren(root, 0, depth)
    return root
            
#test class to print in order, pre order, and post order traversal
def printTraversals(root: Node):
    print("In Order Traversal")

    print()
    Traversal.inOrderTraversal(root, lambda node : print(node.name, node.value))
    print()

    print("Pre Order Traversal")

    print()
    Traversal.preOrderTraversal(root, lambda node : print(node.name, node.value))
    print()

    print("Post Order Traversal")

    print()
    Traversal.postOrderTraversal(root, lambda node : print(node.name, node.value))
    print()

if __name__ == "__main__":
    depth = 1
    root = createBinaryTree(depth)
    print("Tree Depth of " + str(depth))
    print()
    printTraversals(root)
    
    depth = 2
    root = createBinaryTree(depth)
    print("Tree Depth of " + str(depth))
    print()
    printTraversals(root)
