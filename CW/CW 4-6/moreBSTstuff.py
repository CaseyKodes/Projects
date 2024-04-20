# moreBSTstuff

def remove(self, key):
    # multiple cases
    '''
    if item is a leaf just remove
        return none object 
        shortcut 
            make item = item.left/right

    if item has one child
        can not return none because there is child
        just return child 

    if item has mulitple children (hard case)
        break tree for a second 
        swap with a child 
        which child?
            biggest in left or smallest in right subtrees
    '''
    if key == self.key:
        if self.left is None: return self.right
        if self.right is None: return self.left

        self.swapwith(self.left.maxnode())
        self.left = self.left.remove(key)

    self.child= self.child.remove(key)

    return self

# rotation
'''
way to balance tree when to many levels are being used 
'''


