# This file empty on purpose - add the correct classes/methods below

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority==other.priority and self.item==other.item
    
class PQ_UL: # unordered list
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)
    
    def insert(self, item, priority):
        newE = Entry(item, priority)
        self.L.append(newE)

    def find_min(self):
        if len(self) == 0:
            raise RuntimeError("Queue is empty")
        
        minentry = self.L[0]
        idx = 1
        while idx < len(self.L):
            if self.L[idx].priority < minentry.priority:
                minentry = self.L[idx]
            idx+=1
        
        return minentry

    def remove_min(self):
        minentry = self.find_min()
        self.L.remove(minentry)
        return minentry

class PQ_OL: # ordered list
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)
    
    def insert(self, item, priority):
        newE = Entry(item, priority)
        self.L.append(newE)
        self.L.sort()

    def find_min(self):
        if len(self) == 0:
            raise Exception
        
        minentry = self.L[0]
        idx = 1
        while idx < len(self.L):
            if self.L[idx].priority < minentry.priority:
                minentry = self.L[idx]
            idx+=1
        
        return minentry

    def remove_min(self):
        minentry = self.find_min()
        self.L.remove(minentry)
        return minentry

    