#test_hashing

from hashing import Entry, ListMapping
import unittest

class TestEntry(unittest.TestCase):
    def setUp(self):
        self.e1 = Entry('pikachu', ['tail whip', 'thunder shock', 'growl', 'quick attack'])
        self.e2 = Entry('greninja', ['water shurkien', 'night slash', 'mat block', 'hydro pump'])

    def test_init(self):
        "Initialize entrys w/ key:value pairs"
        self.assertEqual(self.e1.key, 'pikachu')
        self.assertEqual(self.e1.value,['tail whip', 'thunder shock', 'growl', 'quick attack'])

        self.assertEqual(self.e2.key, 'greninja')
        self.assertEqual(self.e2.value, ['water shurkien', 'night slash', 'mat block', 'hydro pump'])

    def test_repr(self):
        "String representation"
        self.assertEqual(repr(self.e1), "Entry(key=pikachu, value=['tail whip', 'thunder shock', 'growl', 'quick attack'])")
        self.assertEqual(repr(self.e2), "Entry(key=greninja, value=['water shurkien', 'night slash', 'mat block', 'hydro pump'])")

class TestListMapping(unittest.TestCase):
    def setUp(self):
        self.empty_map = ListMapping()

    def test_putget_twopairs(self):
        "Adds and retrieves a two key:value pairs"
        my_map = ListMapping()
        my_map['pikachu'] = ['tail whip', 'thunder shock', 'growl', 'quick attack']
        my_map['greninja'] = ['water shurkien', 'night slash', 'mat block', 'hydro pump']

        self.assertEqual(my_map['pikachu'], ['tail whip', 'thunder shock', 'growl', 'quick attack'])
        self.assertEqual(my_map['greninja'], ['water shurkien', 'night slash', 'mat block', 'hydro pump'])

    def test_putget_many(self):
        "Adds and retrieves many two key:value pairs"
        my_map = ListMapping()
        n = 100
        for i in range(n):
            my_map[i] = str(i)
        
        for i in range(n):
            self.assertEqual(my_map[i], str(i))

    def test_get_notin(self):
        "Attempt to retrieve a missing key"
        my_map = ListMapping()
        n = 100

        # First, make sure put/get works as expected
        for i in range(n):
            my_map[i] = str(i)
        
        for i in range(n):
            self.assertEqual(my_map[i], str(i))

        # Now, check for a missing key
        with self.assertRaises(KeyError):
            my_map['pikachu']  

unittest.main()