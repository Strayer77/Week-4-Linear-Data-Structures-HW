#Matt Strayer

class LinkedListStack:
    
    #node class
    class _Node:
        #node class for storing a singly linked node
        
        def __init__(self, element, next):
            self._element = element          #reference to element
            self._next = next                #reference to the next node
            
            
    #stack methods
    def __init__(self):
        self._head = None                    #reference to the head node
        self._size = 0                       #number of items in stack
        
    def size(self):
        #returns number of elements in a stack
        return self._size
    
    def is_empty(self):
        #will return true if stack is empty, false if not
        return self._size == 0
    
    def push(self, data):
        #adds data to the top of the stack
        self._head = self._Node(data, self._head) #create and link new node
        self._size += 1                           #increases size by 1
        
    def top(self):
        #returns, but does not remove, element at top of stack
        #raises exception if stack is empty
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element               #returns the head of list
    
    def pop(self):
        #remove and return the element from top of stack
        
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self._head._element
        self._head = self._head._next            #new top node
        self._size -= 1
        return result
    

#creating instance of linked list stack
listStack = LinkedListStack()

listStack.push(5)
listStack.push(10)
listStack.push(15)
listStack.push(20)
print(listStack.top())
print(listStack.size())
listStack.pop()
listStack.pop()
print(listStack.top())
print(listStack.size())

