# stack.py

class stack:
    def __init__(self):
        self.L = []

    def push(self, item):
        self.L.append(item)

    def pop(self):
        return self.L.pop()

class queue:
    def __init__(self):
        self.L = []

    def enqueue(self,item):
        self.L.append(item)

    def dequeue(self):
        return self.L.pop(0)

class node:
    def __init__(self,item,next):
        self.item = item
        self.next = next
    
    def _repr__(self):
        return f"Node({self.item})"

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_first(self, item):
        newnode = node(item,next = self.head)
        self.len += 1 

    def remove_first(self):            
        item = self.head.item
        self.head = self.head.next
        self.len -= 1
        if len(self) == 0:
            self.tail = self.head


    def __len__(self):
        return 0 


'''
import time
class stackset:
    def __init__(self):
        self.S = set()

    def push (self,item):
        newItem = (time.time(),item)
        self.S.add(newItem)
        time.sleep(.01)
    
    def pop(self):
        tmax = 0 
        for item in self.S:
            if item[0] > tmax:
                tmax = item[0]
                oldestitem = item

        self.S.remove(oldestitem)
        return oldestitem[1]'''