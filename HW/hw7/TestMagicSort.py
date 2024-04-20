import unittest
import random as ran
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort

class Test_linear_scan(unittest.TestCase):
    def test_linearscan(self):
        # tests a sorted list that only has one of each value
        L = [1,2,3,4,5]
        self.assertEqual(linear_scan(L), "list is sorted")
        # tests a reversed list that only has one of each value
        L = [5,4,3,2,1]
        self.assertEqual(linear_scan(L), "list is reversed")
        # tests and unsorted list that has a lot of values out of place
        L = [1,5,3,7,9,2,3,7,4,1,7,6,5,4,8,5,9,6,3]
        self.assertEqual(linear_scan(L), "unsorted use quicksort")
        # tests an unsorted list that only has a few values out of place
        L = [6,5,7,4,3,9,2,1]
        self.assertEqual(linear_scan(L), "unsorted use insertion")
        # tests a reversed list that has a lot of similar values
        L = [5,5,5,5,5,5,4]
        self.assertEqual(linear_scan(L), "list is reversed")
        # tests a sroted list that has a lot of similar values 
        L = [5,5,5,5,5,6]
        self.assertEqual(linear_scan(L), "list is sorted")

class Test_reverse_list(unittest.TestCase): 
    # one test case easy to check
    def test_reverselist(self):
        reverse = [9,8,7,6,5,4,3,2,1]
        sorted = [1,2,3,4,5,6,7,8,9]
        reverse_list(reverse)
        self.assertEqual(reverse, sorted)

        # lots of tests to make sure a wide variety of list sizes work
        for i in range(1, 50):
            L = [n for n in range(i)]
            copy = L.copy()
            L.sort(reverse=True)
            reverse_list(L)
            self.assertEqual(copy, L)

class Test_insertionsort(unittest.TestCase): 
    # one easy test case to check 
    def test_insertionsort(self):
        random = [6,3,8,7,9,5,4,1,2]
        sorted = [1,2,3,4,5,6,7,8,9]
        insertionsort(random)
        self.assertEqual(sorted, random)

        # lots of tests to check a lot of random lists
        for n in range(1, 50):
            L = [ran.randint(0, n) for i in range(n)]
            copy = L.copy()
            insertionsort(L)
            copy.sort()
            self.assertEqual(copy, L)

class Test_quicksort(unittest.TestCase): 
    # one easy test case to check 
    def test_quicksort(self):
        random = [6,3,8,7,9,5,4,1,2]
        sorted = [1,2,3,4,5,6,7,8,9]
        quicksort(random)
        self.assertEqual(sorted, random)

        lotunsort = [9,7,6,88,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4,3,6,5,7,4] # 6 things out of place 
        copy = lotunsort.copy()
        copy.sort()
        quicksort(lotunsort)
        self.assertEqual(copy, lotunsort)

        # lots of tests to check a lot of random lists
        for n in range(1, 50):
            L = [ran.randint(0, n) for i in range(n)]
            copy = L.copy()
            quicksort(L)
            copy.sort()
            self.assertEqual(copy, L)

class Test_mergesort(unittest.TestCase): 
    # one easy test case to check 
    def test_mergesort(self):
        random = [6,3,8,7,9,5,4,1,2]
        sorted = [1,2,3,4,5,6,7,8,9]
        mergesort(random)
        self.assertEqual(sorted, random)

        # tests with duplicate values 
        random = [6,3,5,8,7,9,5,4,1,5,2]
        sorted = [1,2,3,4,5,5,5,6,7,8,9]
        mergesort(random)
        self.assertEqual(sorted, random)
        
        # lots of tests to check a lot of random lists
        for n in range(1, 50):
            L = [ran.randint(0, n) for i in range(n)]
            copy = L.copy()
            mergesort(L)
            copy.sort()
            self.assertEqual(copy, L)

class Test_magicsort(unittest.TestCase): 
    def test_magicsort(self):
        # all magic sort tests make sure the list was in fact sorted in place 

        # tests when a sorted list in input
        # magic sort should not return anything when a sorted list is input
        L = [1,2,3,4,5,6,7,8,9]
        self.assertEqual({}, magic_sort(L))

        # tests when a reverse list is input
        # magic sort should return the reverse_list call 
        L = [6,5,4,3,2,1]
        self.assertEqual(magic_sort(L), {'reverse_list'})
        self.assertEqual(L, [1,2,3,4,5,6])

        # tests when an unsorted list with 5 or less items are out of order
        # magic sort should only return insertionsort when <=5 items are out of order
        L = [5,4,3,2,8,6,9]
        lcopy = L.copy()
        self.assertEqual(magic_sort(L), {'insertionsort'})
        lcopy.sort()
        self.assertEqual(L, lcopy)

        # test when reverse list should be called for a big list 
        n = 1000
        L = [(n-i) for i in range(n)]
        self.assertEqual(magic_sort(L), {'reverse_list'})
        copy = L.copy()
        copy.sort()
        self.assertEqual(copy, L)

        # tyest when all three should be called 
        L = [(n-i) for i in range(n)]
        L[:6] = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(magic_sort(L), {'quicksort', 'insertionsort', 'mergesort'})
        copy = L.copy()
        copy.sort()
        self.assertEqual(copy, L)

        # lots of tests to check a lot of random lists
        for n in range(1, 50):
            L = [ran.randint(0, n) for i in range(n)]
            copy = L.copy()
            print(magic_sort(L)) # to see what really is going on 
            self.assertNotEqual(magic_sort(L), {'DNE'}) # to make sure magic does return some set of strings
            copy.sort()
            self.assertEqual(copy, L)


unittest.main()
