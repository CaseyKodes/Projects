from solve_puzzle import solve_puzzle as puzzle
import unittest

# for these thests just create lists that only work each way 
class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                self.assertTrue(puzzle([3,6,6,2,6,6]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertTrue(puzzle([4,9,3,9,9,3,9,9,9]))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertTrue(puzzle([2,5,1,7,7,7,7]))
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertFalse(puzzle([3,4,1,2,0]))

unittest.main()