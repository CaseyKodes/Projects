# implimentation  of the Hashmap ADT

class hashmap:
    def __init__(self):
        """initializes an empty map"""
        self.map = {}

    def __contains__(self, user):
        """returns if item is in map"""
        return user in self.map

    def get(self, user):
        """returns balance of user"""
        return self.map[user]

    def add(self, user, balance=None):
        """adds user and balance to map"""

        if balance == None:
            balance = 0

        self.map[user] = balance