import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        # all five tree structures are tested for arguments sake
        
        r'''    CCCCXXX
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
        '''
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

        r'''    CCXCCXX
                /
               / \
              -   *
             /\   /\
            Q  9 10 3
        '''
        root = BETNode('/')
        root.add_left(BETNode('-'))
        root.add_right(BETNode('*'))
        root.left.add_left(BETNode('Q'))
        root.left.add_right(BETNode('9'))
        root.right.add_left(BETNode('10'))
        root.right.add_right(BETNode('3'))
        expected_str = '((Q-9)/(10*3))'
        self.assertEqual(repr(root), expected_str)

        r'''    CCXCXCX
                *
               / \
              +   J
             / \
            /   3
           / \
          K   2

        '''
        root = BETNode('*')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('J'))
        root.left.add_left(BETNode('/'))
        root.left.add_right(BETNode('3'))
        root.left.left.add_left(BETNode('K'))
        root.left.left.add_right(BETNode('2'))
        expected_str = '(((K/2)+3)*J)'
        self.assertEqual(repr(root), expected_str)

        r'''    CCCXXCX
                -
               / \
              +   10
             / \
            A   *
               / \
              6   2
        '''
        root = BETNode('-')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('10'))
        root.left.add_left(BETNode('A'))
        root.left.add_right(BETNode('*'))
        root.left.right.add_left(BETNode('6'))
        root.left.right.add_right(BETNode('2'))
        expected_str = '((A+(6*2))-10)'
        self.assertEqual(repr(root), expected_str)

        r'''    CCCXCXX
                +
               / \
              J   -
                 / \
                /   A
               / \
              Q   3
        '''
        root = BETNode('+')
        root.add_left(BETNode('J'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('/'))
        root.right.add_right(BETNode('A'))
        root.right.left.add_left(BETNode('Q'))
        root.right.left.add_right(BETNode('3'))
        expected_str = '(J+((Q/3)-A))'
        self.assertEqual(repr(root), expected_str)


    # TODO: Add test cases below. Repr is provided for you.
    # tests evaluate for all tree shapes
    def test_evaluate_tree1(self): 
        r'''
               *
              / \
             A   *
                / \
               2   +
                  / \
                 6   5
           '''
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('6'))
        root.right.right.add_right(BETNode('5'))
        #(6+5)*2)*1 = 22
        expectedoutput = 22
        self.assertEqual(BETNode.evaluate(root), expectedoutput)

    def test_evaluate_tree2(self): 
        r'''
                -
               / \
              +   /
             /\   /\
            K  J  Q 6
        '''
        root = BETNode('-')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('/'))
        root.left.add_left(BETNode('K'))
        root.left.add_right(BETNode('J'))
        root.right.add_left(BETNode('Q'))
        root.right.add_right(BETNode('6'))
        #(13+11)-(12/6)= 22
        expectedoutput = 22
        self.assertEqual(BETNode.evaluate(root), expectedoutput)
    
    def test_evaluate_tree3(self): 
        r'''
                *
               / \
              -   4
             / \
            *   Q
           / \
          10  3

        '''
        root = BETNode('*')
        root.add_left(BETNode('-'))
        root.add_right(BETNode('4'))
        root.left.add_left(BETNode('*'))
        root.left.add_right(BETNode('Q'))
        root.left.left.add_left(BETNode('10'))
        root.left.left.add_right(BETNode('3'))
        #(10*3)-12*4=72
        expectedoutput = 72
        self.assertEqual(BETNode.evaluate(root), expectedoutput)
    
    def test_evaluate_tree4(self): 
        r'''
                -
               / \
              *   J
             / \
            7   -
               / \
              9   4
        '''
        root = BETNode('-')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('J'))
        root.left.add_left(BETNode('7'))
        root.left.add_right(BETNode('-'))
        root.left.right.add_left(BETNode('9'))
        root.left.right.add_right(BETNode('4'))
        #(9-4)*7-11 = 24
        expectedoutput = 24
        self.assertEqual(BETNode.evaluate(root), expectedoutput)
    
    def test_evaluate_tree5(self): 
        r'''
                +
               / \
              4   *
                 / \
                -   3
               / \
              8   1
        '''
        root = BETNode('+')
        root.add_left(BETNode('4'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('-'))
        root.right.add_right(BETNode('3'))
        root.right.left.add_left(BETNode('8'))
        root.right.left.add_right(BETNode('1'))
        #(8-1)*3+4=25
        expectedoutput = 25
        self.assertEqual(BETNode.evaluate(root), expectedoutput)

    def test_evaluate_tree5(self): 
        r'''
                /
               / \
              4   *
                 / \
                -   3
               / \
              8   8
        '''
        root = BETNode('/')
        root.add_left(BETNode('4'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('-'))
        root.right.add_right(BETNode('3'))
        root.right.left.add_left(BETNode('8'))
        root.right.left.add_right(BETNode('8'))
        expectedoutput = 24
        self.assertGreaterEqual(BETNode.evaluate(root), expectedoutput)

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self): 
        nodupes = create_trees('K639') # no reapeats should create the max amount of trees 
        self.assertEqual(len(nodupes), 7680)

    def test_hand2(self): 
        onedupe = create_trees('33QA') # one repeat should be half of the max
        self.assertEqual(len(onedupe), 3840)
    
    # these next two were just for me to see how many combos were made
    def test_hand3(self):
        twodupes = create_trees('666K')
        self.assertEqual(len(twodupes), 1280)
    
    def test_hand4(self):
        allsame = create_trees('JJJJ')
        self.assertEqual(len(allsame), 320)
        
class TestFindSolutions(unittest.TestCase):
    def test0sols(self): 
        zero = find_solutions('A1A1') # there is no possible way to create 24 with these values
        self.assertEqual(len(zero), 0)

    def test_A23Q(self): 
        thirtythree = find_solutions('A23Q') # there should be 33 ways to create 24 with these values
        self.assertEqual(len(thirtythree), 33)

unittest.main()