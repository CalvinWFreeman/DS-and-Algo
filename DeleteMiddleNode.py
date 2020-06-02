import LinkedList as ll

def deleteMiddleNode(node: ll.Node):

    #grab data of next node in the list 
    #head -> targetnode -> (node2) -> tail
    nextNode = node.next

    #set data of current node to next node
    #head -> (targetnode.data = node2.data) -> node2 -> tail
    node.data = nextNode.data

    #set current node next to node after next
    #head -> targetnode -> tail 
    #(node2) -> tail
    nextNextNode = nextNode.next
    
    if(nextNextNode is None):
        node.next = None
    else:
        node.next = nextNextNode

if __name__ == "__main__":
    linkedList = ll.LinkedList()

    #create test list
    for i in range(1, 10):
        linkedList.addNodeToTail(ll.Node(i))
    
    print(linkedList)

    #get a middel node
    middleNode = linkedList.getNodeByPos(8)
    print(middleNode.data)

    #delete the middle node
    deleteMiddleNode(middleNode)
    print(linkedList)
    