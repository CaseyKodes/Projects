# test stack.py

from stack import stack, queue, linkedlist
import unittest

class TestStack(unittest.TestCase):
    def testPushPop(self):
        n = 4
        s = stack()
        for i in range (n):
            s.push(i)
        for i in range (n):
            self.assertEqual(s.pop(), n-1-i)

class testqueue(unittest.TestCase):
    def test_ende(self):
        n = 8
        q = queue()
        for i in range (n):
            q.enqueue(i)
        for i in range (n):
            self.assertEqual(q.dequeue, i)

class testlinkedlist(unittest.TestCase):
    def test_afrf(self):
        n = 8
        ll = linkedlist()
        for i in range (n):
            ll.add_first(i)
        for i in range (n):
            self.assertEqual(ll.remove_first(), n-1-i)



unittest.main()
