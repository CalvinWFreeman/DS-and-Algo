class Stack:

    class StackNode:
        def __init__ (self, data=None):
            self.next = None
            if data is None:
                self.data = None
            else:
                self.data = data
            
    def __init__(self, node: StackNode = None):
        if node is None:
            self.top = None
        else:
            self.top = node

    def push(self, data):
        node = self.StackNode(data)
        node.next = self.top
        self.top = node
    
    def pop(self):
        data = self.top.data     
        
        if(self.top.next is None):
            self.top = None
        else:
            self.top = self.top.next

        return data
    def peek(self):
        if(self.isEmpty()):
            raise ValueError('Stack is Empty')        
        else:
            return self.top.data
        

    def isEmpty(self):
        if(self.top is None):
            return True
        else:
            return False

    def __str__(self):
        arr = []
        top = self.top
        while(top.next is not None):
            arr.append(top.data)
            top = top.next
        arr.append(top.data)
        return(str(arr))  

if __name__ == "__main__":
    _stack = Stack()
    _stack.push(1)
    _stack.push(10)
    _stack.push(100)

    print("After push: ", _stack)
    print("Let's peek: ", _stack.peek())
    print("Let's pop: ", _stack.pop())
    
    print("After pop: ", _stack)

    print("Is the stack empty?", _stack.isEmpty())

    while(not _stack.isEmpty()):
        print("Popping: ", _stack.pop())
    
    print("Is the stack empty?", _stack.isEmpty())
 

