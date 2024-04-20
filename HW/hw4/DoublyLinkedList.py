# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: 
            self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: 
            self._head._next._prev = self._head
        
        # assiging value in dictionary
        self._nodes[item] = self._head


    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: 
            self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: 
            self._tail._prev._next = self._tail 

        # assiging value in dictionary
        self._nodes[item] = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # deletes item from dictionary
        del self._nodes[item]

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # deletes item from dictionary
        del self._nodes[item]

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: 
            self._tail._next = None
        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        '''
        checks the dictionary of nodes if item is in _nodes
        '''
        if item in self._nodes:
            return True
        else:
            return False

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        '''
        returns the nodes directly before and after the item input as a tuple
        '''
        if item not in self._nodes: # edge case raises runtime error if item not in self._nodes
            raise RuntimeError
        
        elif self._nodes[item] == self._head: # edge case when item is head node
            return (None, self._head._next.item)
        
        elif self._nodes[item] == self._tail: # edge case when item is tail node
            return (self._tail._prev.item, None)
        
        else: # all other cases
            return (self._nodes[item]._prev.item, self._nodes[item]._next.item)

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        '''
        removes the item input from both the dictionary and from the double linked list
        does not matter where the node is in the double linked list 
        '''
        if item not in self._nodes: # edge case item not in self._nodes
            raise RuntimeError
        
        elif self._nodes[item] == self._head: # edge case removing the head
            self._head = self._head._next
            self._head._prev = None

        elif self._nodes[item] == self._tail: # edge case removing the tail 
            self._tail = self._tail._prev
            self._tail._next = None

        else: # normal case where item to be removed is in the middle of the DLL    
            self._nodes[item]._prev._next = self._nodes[item]._next
            self._nodes[item]._next._prev = self._nodes[item]._prev

        hold = self._nodes[item] # store item to be removed so it can be returned 
        del self._nodes[item] # deletes input item from dictioary of nodes 
        self._len -= 1 # fixes length to sdjust for removing an item
        return hold.item
