from puzzle import solve_puzzle as sp
import unittest

class TestPuzzle(unittest.TestCase):
    def setUp(self):
        'Initialize some solveable and unsolveable boards'
        self.b1 = [1,2,1,3,2,0,0]
        self.b2 = [2, 3, 1, 0, 0]
        self.b3 = [2, 3, 3, 1, 0]
        self.b4 = [2, 0, 0, 0]
        self.b5 = [1, 0, 1, 0]

        self.solveable_boards = [self.b1, self.b2, self.b3, self.b5]
        self.unsolveable_boards = [self.b4]

    def testBoards(self):
        'Creates subtests for each board in SetUp'
        
        #solveable
        for board in self.solveable_boards:
            with self.subTest(board=board):
                self.assertTrue(sp(board))

        # unsolveable
        for board in self.unsolveable_boards:
            with self.subTest(board=board):
                self.assertFalse(sp(board))

unittest.main()