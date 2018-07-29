class LinkedListDeque:
    
    class Node:
        
        def __init__(self, element, previous, next):
            self.element = element
            self.previous = previous
            self.next = next
            
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer           #trailer is after header
        self.trailer.previous = self.header       #header is before trailer
        self.size = 0
        
    def size(self):
        return self.size
    
    def is_empty(self):
        #return true if list is empty
        return self.size == 0
    
    def insert_between(self, data, nodeBefore, nodeAfter):
        #adds data between two specific nodes and returns new node
        newest = self.Node(data, nodeBefore, nodeAfter)
        nodeBefore.next = newest
        nodeAfter.previous = newest
        self.size += 1
        return newest
    
    def delete_node(self, node):
        #delete node from list and return its element
        nodeBefore = node.previous
        nodeAfter = node.next
        nodeBefore.next = nodeAfter
        nodeAfter.previous = nodeBefore
        self.size -= 1
        element = node.element
        node.previous = node.next = node.element = None
        return element
    
    #class LinkedDeque(DoublyLinkedList):
        
    def first(self):
        #returns, doesnt remove, element at the front of deque
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.header.next.element
    
    def last(self):
        #returns, doesnt remove, element from the back of deque
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.trailer.previous.element
    
    def addFront(self, data):
        self.insert_between(data, self.header, self.header.next) #after header
        
    def addRear(self, data):
        self.insert_between(data, self.trailer.previous, self.trailer) #before trailer
        
    def removeFront(self):
        #remove and return element from front
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.delete_node(self.header.next)
    
    def removeRear(self):
        #remove and return element from back
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.delete_node(self.trailer.previous)
    
    
myDeque = LinkedListDeque()
myDeque.addRear(5)
myDeque.addFront(6)
myDeque.addFront(80)
myDeque.addFront(94)
myDeque.addFront("hello")
print(myDeque.first())
print(myDeque.removeRear())

        
            
            
        
        
        