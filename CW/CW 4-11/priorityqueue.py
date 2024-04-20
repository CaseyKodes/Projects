# priority queue


# heap
'''

tree like, but ordering is only bottom to top biggest to smallest

il = 1+2n
ir = 2+2n
ip = 0 = none   /   1, 2 = 0   /   3, 4 = 1   /    5, 6= 2

'''


class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Entry(item={self.item}, priority{self.priority})"
    

class Heap:
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)
    
    def iparent(self, idx):
        return (idx-1)//2 if (idx-1)//2 >= 0 else None

    def ileft(self,idx):
        il = idx*2+1
        return il if il<len(self) else None

    def iright(self, idx):
        ir = idx*2+2
        return ir if ir<len(self) else None

    def upheap(self, idx):
        #find parent idx 
        parentidx = self.iparent(idx)

        #while parent exists 
        while parentidx is not None:
            #if parent is smaller swap
            if self.L[parentidx] > self.L[idx]:
                self.L[parentidx], self.L[idx] = self.L[idx], self.L[parentidx]

                idx = parentidx
                parentidx = self.iparent(idx)

    def downheap(self,idx):
        pass

    def peek(self):
        return self.L[0].item

    def insert(self, item, priority):
        newe = Entry(item = item, priority=priority)
        self.L.append(newe)
        self.upheap(len(self)-1)

    def removemin(self):
        pass

    def findMinChild(self, idx):
        pass