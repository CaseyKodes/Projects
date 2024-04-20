# This class is provided for you - you do not need to change anything
class Node:
    '''Node class for linked data structures

        Example:
        --------
            2 Node objects with 1-directional linking
                 _____________      _____________
                | class: Node |    | class: Node |
                |-------------|    |-------------|
                | item = 3    |    | item = 4    |
                | _next = ----|--->| _next = ----|---> None
                |_____________|    |_____________|   
    '''

    def __init__(self, item, _next = None):
        'initialize with data and location of next node'
        self.item = item
        self._next = _next

    def __iter__(self):
        '''recursively yields all items in LL

            iter() is called when we iterate over an object, e.g. `for item in items:`

            Example
            -------
            >>> head_node = Node('a', _next=Node('b', _next=Node('c', _next=Node('d', _next=Node('e')))))
            >>> # head: 'a'-->'b'-->'c'-->'d'-->'e'
            >>> for item in head_node:
            ...     print(item)
            ...
            a
            b
            c
            d
            e
        '''

        # 1) Yield this item
        yield self.item 

        # 2) Yield all other items, starting with the next Node
        if self._next is not None: yield from self._next

    def __repr__(self):
        'Provides a nice string representation of the node'
        return f"Node({self.item})"

class LinkedList:
    '''LinkedList supporing O(1) add_first, remove_first, add_last
    
        Diagrams
        --------
            Empty LL: _head and _tail point to None
                ll._head-->None <-+
                                  |
                ll._tail----------+
    
            One item: _head and _tail point to the same node
                ll._head-->0-->None
                           ^
                ll._tail---+

            Multiple items: _head and _tail point to different nodes
                ll._head-->0-->1-->2-->...-->n-->None
                                             ^
                ll._tail---------------------+
    '''

    # TODO: items needs a default value that IS NOT mutable
    # e.g. DO NOT use an empty list
    def __init__(self, items = None):
        'initialize a new LinkedList w/ optional collection items'
        self._head = None
        self._tail = None
        self._len = 0
        if items == None:
            self._ll = []
        else:
            self._ll = items 
            for i in range (len(self._ll)):
                self.add_last(items[i])

    def add_first(self, item):
        'adds item to beginning of linked list'

        # create a new node pointed at self._head
        newnode = Node(item, _next = self._head)
        # update self._head
        self._head = newnode
        # update len
        self._len += 1
        if self._len == 1:
            self._tail = self._head

    def add_last(self, item):
        'adds item to end of linked list'

        # same as add_first() if this is an empty linked list
        if self._len == 0:
            self.add_first(item)
        # create a new node, update self._tail._next
        else:
            newnode = Node(item)
            self._tail._next = newnode
            # update self._tail
            self._tail = newnode
            # update len
            self._len += 1

    def remove_first(self):
        'removes item from beginning of linked list'
        # Edge case - cannot remove from empty
        if self._len == 0:
            raise RuntimeError ("You can not remove items from an empty list")
        # Edge case - update tail if this is the last node
        if self._head._next == self._tail:
            self._tail = None
        # store item in temporary variable
        hold = self._head.item
        # update self._head
        self._head = self._head._next
        # update len
        self._len -= 1
        # return item from old head
        return hold

    def __len__(self):
        'returns number of nodes in Linked list'
        return self._len

    def __iter__(self):
        'Allows iteration in a for loop'
        if self._head is not None: yield from self._head

    def __repr__(self):
        '''returns a string representation of our linked list
        
            Examples
            --------
            >>> ll1 = LinkedList(range(5))
            >>> print(ll1)
            LinkedList:
                Head: Node(0)
                Tail: Node(4)
                0-->1-->2-->3-->4-->None
            
            >>> ll2 = LinkedList()
            >>> print(ll2)
            LinkedList:
                Head: None
                Tail: None
                None
            
            >>> ll3 = LinkedList(('hello', 'goodbye'))
            >>> print(ll3)
            LinkedList:
                Head: Node(hello)
                Tail: Node(goodbye)
                'hello'-->'goodbye'-->None
        '''
        str_head = f"Head: {self._head}"
        str_tail = f"Tail: {self._tail}"

        L_nodes = []
        # Append string repr of each node
        for node in self:
            L_nodes.append(repr(node)+ '-->')

        # join all the strings together
        return f"LinkedList:\n\t{str_head}\n\t{str_tail}\n\t{''.join(L_nodes)}{None}"