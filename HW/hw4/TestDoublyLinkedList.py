from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        dll = DLL(range(30))

        self.assertTrue(25 in dll)
        self.assertFalse(40 in dll)
        hold = dll.remove_node(19)
        self.assertFalse(19 in dll)
        dll.add_last(66)
        self.assertTrue(66 in dll)

    def test_neighbors(self):
        dll = DLL(range(50))

        # tests normal case of neighbors of a node in the middle of the DLL
        for i in range(10):
            self.assertEqual(dll.neighbors(i+10), (i+9, i+11))

        # test edge cases of neighbors of head and tail
        self.assertEqual(dll.neighbors(0), (None,1))
        self.assertEqual(dll.neighbors(49), (48,None))

        # tests that neighbors raises an error when input node is not in DLL
        self.assertRaises(RuntimeError, dll.neighbors, 200)

    def test_remove_item(self):
        dll = DLL(range(70))
        self.assertEqual(len(dll), 70) # len = 70 

        # tests that remove_node raises an error if the node is not in the DLL
        self.assertRaises(RuntimeError, dll.remove_node, 200)

        for i in range(10): # tests normal case when node to  be removed is somehwere in the middle of the DLL
            self.assertEqual(dll.remove_node(i+20), i+20) #-10 to the len now at 60
            self.assertEqual(len(dll), 70-1-i)

        # make sure the gap in nodes is patched when a node is removed 
        hold = dll.remove_node(55) # len now 59
        self.assertEqual(dll._nodes[hold-1]._next.item, 56) # testing that the next item after 54 is now 56
        self.assertEqual(dll._nodes[hold+1]._prev.item, 54) # testing that the prev item before 56 is now 45

        # edge case removing the tail node
        self.assertEqual(dll.remove_node(69), 69) # len now 58
        self.assertEqual(dll._tail.item, 68)
        self.assertEqual(dll._tail._next, None)
        self.assertEqual(len(dll), 58)

        # edge case removing the head node
        self.assertEqual(dll.remove_node(0), 0) # len now 57
        self.assertEqual(dll._head.item, 1)
        self.assertEqual(dll._head._prev, None)
        self.assertEqual(len(dll), 57)


unittest.main()
