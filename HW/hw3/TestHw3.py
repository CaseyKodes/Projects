# test hw 3

import unittest
import hw3

class Testhw3(unittest.TestCase):

    # defining all global testing variables 
    
    global testlist1
    testlist1 = [1,2,3,4,5,5,6,7]
    global testlist2
    testlist2 = [1,2,3,4,5,6,7,8,9,10,10]

    global testtarget1
    testtarget1 = 10
    global testtarget2
    testtarget2 = 20
    
    global expected1
    expected1 = {(3,7),(4,6)}
    global expected2
    expected2 = set()
    
    '''
    tests both methods for when there sohuld be output 
    and for when there should not be output
    both tests check for the case where there are two 
    identical values in the input list that equal the targert
    '''

    # tests naive with output
    def test_findPairsNaiveWithOutput(self):
        testData1 = hw3.findPairNaive(testlist1, testtarget1)
        self.assertEqual(testData1, expected1)

    # tests naive without output
    def test_findPairsNaiveWithoutOutput(self):
        testData2 = hw3.findPairNaive(testlist2, testtarget2)
        self.assertEqual(testData2, expected2)

    # tests optimize with output
    def test_findPairsOptimizedWithOutput(self):
        testData3 = hw3.findPairOptimize(testlist1, testtarget1)
        self.assertEqual(testData3, expected1)

    # tests optimize without output
    def test_finPairsOptimizeWithoutoutput(self):
        testData4 = hw3.findPairOptimize(testlist2, testtarget2)
        self.assertEqual(testData4, expected2)


unittest.main()