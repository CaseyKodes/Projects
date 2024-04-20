# test factorial 

from factorial import factorial 
import unittest

class TestFactorial(unittest.TestCase):
    def test_expected(self):
        self.assertEqual(factorial(5), 120)

    def test_edge(self):
        self.assertEqual(factorial(0), 1)

    def test_typing(self):
        with self.assertRaises(TypeError):
            factorial(2.3)


class TestsumK(unittest.TestCase):
    pass



unittest.main()
