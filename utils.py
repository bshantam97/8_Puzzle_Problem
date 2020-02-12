class Queue:
    
    " Implementation of a Queue "

    def __init__(self):
        "Initialize the init method"
        self.items = []
        
    def enqueue(self,items):
        "Enqueing element at the zeroth index "
        self.items.insert(0,items)
        
    def dequeue(self):
        "Removing an element from the front of a queue"
        self.items.pop(0)
        
    def size(self):
        "returns the size of the queue"
        return len(self.items)
    
    def is_Empty(self):
        " Returns a boolean value stating whether the queue is empty or not"
        return self.items == []