import Stack as s
import random

class StackHelper:

    @staticmethod
    def sortStack(stack: s.Stack, asc=True):
        sortedStack = s.Stack()
        if asc:
            while(not stack.isEmpty()):
                if sortedStack.isEmpty():
                    StackHelper.transfer(stack, sortedStack)
                else:
                    temp = stack.pop()
                    if temp < sortedStack.peek():
                        sortedStack.push(temp)
                    else:
                        numTransfer = 0
                        while(not sortedStack.isEmpty() and temp > sortedStack.peek()):
                            StackHelper.transfer(sortedStack, stack)
                            numTransfer += 1
                        sortedStack.push(temp)
                        StackHelper.transfer(stack, sortedStack, numTransfer)
        return sortedStack

    @staticmethod
    def transfer(source: s.Stack, target: s.Stack, numTransfer=1):
        for i in range(0, numTransfer):
            target.push(source.pop())


if __name__ == "__main__":
    _stack = s.Stack()

    for i in range(0, random.randint(1, 20)):
        _stack.push(random.randint(1,100))
    
    print("Not Sorted: ", _stack)
    print("Sorted: ", StackHelper.sortStack(_stack))



