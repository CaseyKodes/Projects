import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    
    def __repr__(self):
        return f"{self.name}, time: {self.time}"

class Waitlist:
    def __init__(self):
        self._entries = [] # creats a list attribute called entries for each waitlist

    def add_customer(self, name, time):
        #TODO add customers to the waiting list.
        if len(time) != 5: # checks to make sure the input time is valid 
            raise RuntimeError("The input time is not a valid time")
        if time[2] != ':':
            raise RuntimeError("The input time is not a valid time")
        restime = Time(time[:2], time[3:]) # creats a time object which can be more easily sorted
        self._entries.append(Entry(name, restime))
        self._entries.sort() # sorts list based on time 

    def peek(self):
        #TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        # Return a tuple of the extracted item (customer, time). Return None if the heap is empty
        if len(self._entries) == 0: # if the list is empty returns none
            return None
        return self._entries[0] # if ths list is not empty returns the first element in the list which will be the one with the highest priority 

    def seat_customer(self):
        #TODO The program should extract the customer with the highest priority 
        # (i.e., the earliest reservation time) from the priority queue.
        # Return a tuple of the extracted item (customer, time)
        if len(self._entries) == 0: # if list is empty raises an error
            raise RuntimeError("The waitlist is empty")
        toreturn = self._entries[0] # stores what should be returned
        self._entries.remove(toreturn) # removes that item from the list
        return toreturn # returns the item 

    def print_reservation_list(self):
        #TODO Prints all customers in order of their priority (reservation time).
        # Maintain the heap property
        if len(self._entries) == 0: # if list is empty raises an error
            return ("The waitlist is empty")
        string = ""
        for customer in self._entries: # loops through the list and adds to a string that will be returned
            string += (f"The next customer on the wating list is: {customer}\n")
        return string
    
    def change_reservation(self, name, new_priority):
        #TODO Change the reservation time (priority) for the customer with the given name
        if len(self._entries) == 0:# if list is empty raises an error
            return ("The waitlist is empty")
        if len(new_priority) != 5: # if the length is not 5 the time is not valid and raises an error
            raise KeyError("The input time is not a valid time")
        for customer in self._entries: # loops through the list to find the entry with the name of the customer who wants to change their time 
            if name == customer.name:
                customer.time = Time(new_priority[:2], new_priority[3:]) # changes time of the customer 
                toreturn =  f"{customer.name}'s reservation time has been changed to {customer.time}" # stores value to return
                self._entries.sort() # resorts list since it can be out of order from changing a reservation time
                return toreturn # returns a string saying what user and what time were updated 
        raise RuntimeError("Customer is not in list") # if the customer input is not found raises an error

    #Add other methods you may need

