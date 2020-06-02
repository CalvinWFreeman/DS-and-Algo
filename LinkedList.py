class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, node: Node = None):
        if(node is None):
            self.head = None
            self.length = 0
        else:
            self.head = node
            self.length = 1

    def addNodeToTail(self, node: Node):
        if(self.head is None):
            self.head = Node(node.data)
            self.head.next = None
            self.length = 1
        else:
            head_p = self.head
            while(head_p.next is not None):
                head_p = head_p.next
            head_p.next = node
            self.length += 1
    
    def getNodeByPos(self, pos):
        if(pos < self.length):
            head_p = self.head
            for i in range(0, pos-1):
                head_p = head_p.next
            return head_p
        else:
            return None
    
    def __str__(self):
        arr = []
        head_p = self.head
        while(head_p.next is not None):
            arr.append(head_p.data)
            head_p = head_p.next
        arr.append(head_p.data)
        return(str(arr))  

