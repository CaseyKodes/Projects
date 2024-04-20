import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self): 
      # use sort_halfsorted(L, bubble) to test

      # test a list which is in a somewhat random order
      unsorted = [-3,-5,-1,-17,0,6,5,2,10,7]
      sort_halfsorted(unsorted, bubble)
      self.assertEqual(unsorted, [-17,-5,-3,-1,0,2,5,6,7,10])
      # tests a list that is in half reversed order (negatives and positives still on the correct side o fthe zero)
      reversed = [-1,-3,-4,-10,0,7,5,3,1]
      sort_halfsorted(reversed, bubble)
      self.assertEqual(reversed, [-10,-4,-3,-1,0,1,3,5,7])
      # tests a list that is already sorted
      sorted = [-6,-3,-2,-1,0,5,6,17,20]
      sort_halfsorted(sorted, bubble)
      self.assertEqual(sorted, [-6,-3,-2,-1,0,5,6,17,20])

      # testing each type of sort with each type of list and tests that the sorted list has the same values as the unsorted list 
      for pattern in ['random', 'reverse', 'sorted']:
         for n in range(1, 100):
            for i in range(n):
               L, idx_zero = generate_halfsorted(n, i, pattern)
               sort_halfsorted(L, bubble)
               self.assertEqual(find_zero(L), i)
               values = set(L.copy())
               self.assertTrue(is_sorted(L))
               # test that the same values stayed in the list even after sorting
               self.assertEqual(values, set(L))

   def test_halfosrted_selection(self): # only one that does not work right now
      # use sort_halfsorted(L, selection) to test

      # test a list which is in a somewhat random order
      unsorted = [-3,-5,-1,-17,0,6,5,2,10,7]
      sort_halfsorted(unsorted, selection)
      self.assertEqual(unsorted, [-17,-5,-3,-1,0,2,5,6,7,10])
      # tests a list that is in half reversed order (negatives and positives still on the correct side o fthe zero)
      reversed = [-1,-3,-4,-10,0,7,5,3,1]
      sort_halfsorted(reversed, selection)
      self.assertEqual(reversed, [-10,-4,-3,-1,0,1,3,5,7])
      # tests a list that is already sorted
      sorted = [-6,-3,-2,-1,0,5,6,17,20]
      sort_halfsorted(sorted, selection)
      self.assertEqual(sorted, [-6,-3,-2,-1,0,5,6,17,20])

      # testing each type of sort with each type of list and tests that the sorted list has the same values as the unsorted list 
      for pattern in ['random', 'reverse', 'sorted']:
         for n in range(1, 100):
            for i in range(n):
               L, idx_zero = generate_halfsorted(n, i, pattern)
               sort_halfsorted(L, selection)
               self.assertEqual(find_zero(L), i)
               values = set(L.copy())
               self.assertTrue(is_sorted(L))
               # test that the same values stayed in the list even after sorting
               self.assertEqual(values, set(L))

   def test_halfsorted_insertion(self): 
      # use sort_halfsorted(L, insertion) to test

      # test a list which is in a somewhat random order
      unsorted = [-3,-5,-1,-17,0,6,5,2,10,7]
      sort_halfsorted(unsorted, insertion)
      self.assertEqual(unsorted, [-17,-5,-3,-1,0,2,5,6,7,10])
      # tests a list that is in half reversed order (negatives and positives still on the correct side o fthe zero)
      reversed = [-1,-3,-4,-10,0,7,5,3,1]
      sort_halfsorted(reversed, insertion)
      self.assertEqual(reversed, [-10,-4,-3,-1,0,1,3,5,7])
      # tests a list that is already sorted
      sorted = [-6,-3,-2,-1,0,5,6,17,20]
      sort_halfsorted(sorted, insertion)
      self.assertEqual(sorted, [-6,-3,-2,-1,0,5,6,17,20])

      # testing each type of sort with each type of list and tests that the sorted list has the same values as the unsorted list 
      for pattern in ['random', 'reverse', 'sorted']:
         for n in range(1, 100):
            for i in range(n):
               L, idx_zero = generate_halfsorted(n, i, pattern)
               sort_halfsorted(L, insertion)
               self.assertEqual(find_zero(L), i)
               values = set(L.copy())
               self.assertTrue(is_sorted(L))
               # test that the same values stayed in the list even after sorting
               self.assertEqual(values, set(L))

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()
