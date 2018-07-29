#Matt Strayer

class LinkedQueue:
    
    
    class _Node:
    
        def __init__(self, element, next):  #initialize node's fields
            self._element = element         #reference to user's element
            self._next = next               #reference to next node
            
            
    def __init__(self):
        #creates empty queue
        self._head = None
        self._tail = None
        self._size = 0 #number of queue elements
        
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        #returns, doesnt remove, first element
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element    #front aligned with head of list
    
    def last(self):
        #returns last element
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._element 
 
 
    def dequeue(self):
        #removes and returns fist element from list (FIFO)
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():     #special case as queue is empty
            self._tail = None   #removed head had been the tail
        return result
    
    
    def enqueue(self, data):
        #adds data onto end of queue
        newest = self._Node(data, None)  #node will be the new tail node
        if self.is_empty():
            self._head = newest       #special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest           #update reference to tail node
        self._size += 1
        
q = LinkedQueue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(9)
q.enqueue(23)
q.enqueue(25)
q.enqueue(81)
print("First in queue:", q.first())
print("Number of elements in queue:", q.size())
q.dequeue()
q.dequeue()
print("New item first in queue:", q.first())
print("Last item in queue:", q.last())
print("Number of elements in queue:", q.size())
print(q.is_empty())