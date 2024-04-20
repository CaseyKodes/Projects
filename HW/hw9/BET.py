import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, value):
        # very simple method just need to change self.left from none to a new BETNode
        self.left = value

    def add_right(self, value):
        # very simple method just need to change self.right from none to a new BETNode
        self.right = value

    def evaluate(self): 

        if self.value in BETNode.OPERATORS: # checking if value is an opperator
            leftvalue = self.left.evaluate()
            rightvalue = self.right.evaluate()

            # evaluate section
            # each if statement coordinates to a differetn opperator
            if self.value == '+':
                return leftvalue + rightvalue
            elif self.value == '-':
                return leftvalue - rightvalue
            elif self.value == '*':
                return leftvalue * rightvalue
            elif self.value == '/':
                if rightvalue == 0:
                    rightvalue = 0.00000001 # to make sure there is no chance this tree will evaluate to 24
                return leftvalue / rightvalue
        
        elif self.value in BETNode.CARD_VAL_DICT: # is value is not an opperaotr we just return the value
            return BETNode.CARD_VAL_DICT[self.value]

    def __repr__(self):
        string = "("

        # base case is actually when self.left is None 
        # this means we have found the left most object
        # then we know to return back up the recursive stack 
        if self.left is None:
            return str(self.value)
        
        else:
            toBeAdded = repr(self.left) # if self.left is not none we want to recursively call repr until self.left is none 
            string += toBeAdded
            string += str(self.value) # this is adding the opperator to the string expression of a tree

            toBeAdded = repr(self.right) # we call self.right last because the right BETNodes should show up last in the tree expression 
            string += toBeAdded

        string += ")"
        return string

def create_from_postfix(post): 
    stack = []
    for item in post: # itterates through the inout string
        if item in BETNode.OPERATORS: # if item is in operators we make more calls to make a sub tree
            root = BETNode(item)
            root.add_right(stack.pop())
            root.add_left(stack.pop())
            stack.append(root)
        else: # is item is a value we push it to a stack for later use
            stack.append(BETNode(item))
    return stack.pop()

def create_trees(cards): 
    '''
    takes in elements to be in a tree 
        these elements only include 4 cards to make trees from

    uses itertools class to create all trees
        with all possible combinations of opperators

    returns a set of all the possible trees
        right now only returns the postfix notation of the tree
        need to make a function to generate actual tree from postfix notation
    '''
    trees = set()
    possibletrees = ['CCXCCXX', 'CCXCXCX', 'CCCXXCX', 'CCCXCXX', 'CCCCXXX'] # these are the types of trees that are actually valid
    opperations = itertools.product('-+*/', repeat = 3)
    for oCombo in opperations:
        treevalue = cards[0] + cards[1] + cards[2] + cards[3] + oCombo[0] + oCombo[1] + oCombo[2] # combines card combo and operator combo to one string to permutate again
        possibletreeshape = itertools.permutations(treevalue, 7)
        for shape in possibletreeshape:
            treestring = shape[0] + shape[1] + shape[2] + shape[3] + shape[4] + shape[5] + shape[6] # makes a string to check against the possible tree list
            pattern = ''
            for char in treestring: # creates a patern based off of what is a operator and what is a value 
                if char in BETNode.CARD_VAL_DICT:
                    pattern += 'C'
                elif char in BETNode.OPERATORS:
                    pattern += 'X'
            if pattern in possibletrees: # adds treestring to set of trees if it is a valid shape from posisbletrees
                trees.add(treestring)       
    return trees           

def find_solutions(cards): 
    '''
    takes in  4 card values and makes a call to create trees then those trees are evlauated 
    finds which ones evaluate to 24 
    returns the set of trees that evalute to 24 

    should be a simple for loop to loop through all trees and just evalute all of them and then add them to a set if they evalute to 24 
    '''
    # what i think the whole thing should be
    '''
    but evaluate functions is for BETNode objects not tree objects 
    do we need to think about only the root node of each tree when evaluating a tree object
    '''
    trees = create_trees(cards) # call to create trees
    solved = [] # empty set to fill
    for tree in trees:
        BET = create_from_postfix(tree) # call to create from post fix 
        if BET.evaluate() == 24: # if evaluate gives the value wwe want than we add it to the solved list
            solved.append(repr(BET))
    return solved

if __name__ == '__main__':
        r'''
                +
               / \
              *   4
             / \
            A   -
               / \
              2   3
        '''
        root = BETNode('+')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('4'))
        root.left.add_left(BETNode('A'))
        root.left.add_right(BETNode('-'))
        root.left.right.add_left(BETNode('2'))
        root.left.right.add_right(BETNode('3'))
        #print(root.evaluate())

        #print(list(itertools.permutations('4567-*/', 7)))
        opperations = list(itertools.product('-+*/', repeat=3))
        print()
        #print(opperations)
        print()
        #print(list(itertools.permutations('1234', 4)))
        
        ''' opperations = list(itertools.product('-+*/', repeat = 3))
        opperations = opperations[1:6]
        cardcombo = list(itertools.permutations('548K', 4))
        cardcombo = cardcombo[1:8]
        for oCombo in opperations:
            for cCombo in cardcombo:
                treevalue = cCombo[0] + cCombo[1] + cCombo[2] + cCombo[3] + oCombo[0] + oCombo[1] + oCombo[2]
                print(treevalue)
                #possibletreeshape = itertools.permutations(treevalue, 7)'''
        