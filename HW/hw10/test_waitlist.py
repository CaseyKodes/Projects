# all of our tests for waitlist and menu

import unittest
from waitlist import Waitlist, Time, Entry

# says in directions that we only need to write test cases for the waitlist class
class TestWaitlist(unittest.TestCase):
    def test_init(self):
        testlist = Waitlist()
        self.assertEqual(len(testlist._entries), 0) # makes sure that an empty list is created when a waitlist object is initialized 

    def test_addcustomer(self):
        testlist = Waitlist()
        testlist.add_customer("boby", "12:34")
        self.assertEqual(len(testlist._entries), 1) # makes sure that the length of the list of entries is incrimented when adding a customer 
        self.assertEqual(testlist._entries[0].name, "boby") # checks to see name is created correctly 
        self.assertEqual(testlist._entries[0].time, Time(12,34)) # checks to see that time was created correctly 
        # repeat tests
        testlist.add_customer("guillmare", "04:29")
        self.assertEqual(testlist._entries[0].name, "guillmare") # makes sure the person with the highest priority or the lowest reservation time is first on the waitlist
        self.assertEqual(testlist._entries[0].time, Time(4,29)) 
        self.assertEqual(len(testlist._entries), 2)

    def test_peek(self):
        testlist = Waitlist()
        self.assertEqual(testlist.peek(), None) # makes sure the inital peek sees nothing
        testlist.add_customer("cam", "06:45")
        testlist.add_customer("pat", "22:07")
        testlist.add_customer("ryan", "11:33")
        # order should be cam, ryan, pat
        self.assertEqual(testlist.peek(), testlist._entries[0]) # makes sure peek only looks at the first item in the list 

    def test_changetime(self):
        testlist = Waitlist()
        testlist.add_customer("frank", "14:25")
        testlist.add_customer("jeff", "11:50")
        self.assertEqual(testlist._entries[0].name, "jeff") # checks to make sure cutomers were added in the correct order pertaining to theit time
        testlist.change_reservation("frank", "08:40")
        self.assertEqual(testlist._entries[0].name, "frank") # checks to see that after a reservation time is swapped the waitlist is updatde
        self.assertEqual(testlist._entries[0].time, Time(8,40)) # checks to make sure the time of an entry is updated correctly
        #self.assertRaises(RuntimeError("Customer is not in list"), testlist.change_reservation("papa", "09:34"))

    def test_printreslist(self):
        testlist = Waitlist()
        testlist.add_customer("casey", "04:34")
        testlist.add_customer("connor", "12:54")
        testlist.add_customer("sherer", "11:56")
        expectedoutput = "The next customer on the wating list is: casey, time: 04:34\nThe next customer on the wating list is: sherer, time: 11:56\nThe next customer on the wating list is: connor, time: 12:54\n"
        self.assertEqual(testlist.print_reservation_list(), expectedoutput) # checks the output of print waitlist

    def test_seatcustomer(self):
        testlist = Waitlist()
        testlist.add_customer("thomas", "14:38")
        testlist.add_customer("izzy", "09:10")
        self.assertEqual(len(testlist._entries), 2) # checks to see that the lenght of list is 2 before seating a customer 
        testseat = testlist.seat_customer() 
        self.assertEqual(testseat.name, "izzy") # checks that the seated customer was the correct one
        self.assertEqual(testseat.time, Time(9,10)) # according to the time their reservation was 
        self.assertEqual(len(testlist._entries), 1) # checks to make sure length of a list is decramented after seating a customer 
        testseat2 = testlist.seat_customer()
        # repeat tests 
        self.assertEqual(testseat2.name, "thomas")
        self.assertEqual(testseat2.time, Time(14,38))
        self.assertEqual(len(testlist._entries), 0)
        #self.assertRaises(RuntimeError("The waitlist is empty"), testlist.seat_customer()) # i forget how to use assert raises 

unittest.main()