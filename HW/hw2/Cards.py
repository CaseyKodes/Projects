# Cards.py
import random

class Deck():

    def __init__(self, suits = ["clubs", "diamonds", "hearts", "spades"], values = [1,2,3,4,5,6,7,8,9,10,11,12,13]):
        self.suits = suits
        self.values = values

        # creates card list with double for loops 
        self.cardList = [Card(suit, value) for suit in suits for value in values]
        

    def __len__(self): # calls the len method of a list since that is what cardList is 
        return len(self.cardList)

    def sort(self): #sorts cardlist using list sort by polymorphism
        self.cardList.sort()

    def __repr__(self): # returns deck as a string list of card objects 
        output = "Deck: "

        for item in self.cardList:
            output += str(item) + ", "

        return output

    def shuffle(self): # uses random class to shuffle cardList
        random.shuffle(self.cardList)

    def draw_top(self): # removes that last card object in cardLIst and if cardList is empty raises an error

        if len(self.cardList) == 0:
            raise RuntimeError("the card list is empty")
        else:
            remove = self.cardList[-1]
            self.cardList.remove(self.cardList[-1])
            return remove

    '''
    a deck is a list of card objects 
    methods:
    __len__() returns the amount of cards in the deck the values * the suits
    sort() sorst based on card value 
    __repr__()
    shuffle() uses shuffle from random class
    draw_top() raises RuntimeError if there are no cards in the deck, removes last item in card_list
    instance variables:
    values default values 1-13
    suits default value; 'clubs', 'diamonds', 'hearts', 'spades'
    card_list made from the two pervious lists
    '''

class Card():
    '''
    a card is an object which has both a suit and a value
    '''

    def __init__ (self, suit, value): # defines a card object to have a suit and value
        self.suit = suit
        self.value = value

    def __repr__ (self): # returns the string of ex. "Card (8 of spades)"
        return f"Card ({self.value} of {self.suit})"

    def __lt__(self, other): 
        ''' 
        compers the suit values of two cards to see if the first card is less than,
        if the suits are the same compares the value values of each card
        '''
        if (self.suit < other.suit):
            return True

        elif (self.suit == other.suit):
            return self.value < other.value

        else:
            return False

    def __eq__(self, other): #compares the suit and value of each card input
        return (self.suit == other.suit) & (self.value == other.value)

    '''
    methods:
    __init__()
    __repr__() returns ~ 'Card(3 of hearts)'
    __lt__()  cards are values by suit than values, suits are values alphabetically 
    __eq__()
    instance variables:
    value
    suit 
    '''

class Hand(Deck): #might need to fix the inheritence for this class

    def __init__(self, suits, values): #defines a hand as a list of cards with inheritance from the deck class
        self.suits = suits
        self.values = values
        self.cardList = [Card(suit, value) for suit in suits for value in values]

    def play(self, card): 
        # takes a card input adn tries to remove it from the hand object, if the card is not in hand raises a RunttimeError
        
        if card in self.cardList:
            self.cardList.remove(card)
            return card
        else:
            raise RuntimeError("the card is not in the card list")

    def __repr__(self): # returns hand as a string list of card objects 
        output = "Hand: "

        for item in self.cardList:
            output += str(item) + ", "

        return output

    '''
    a hand is a list of cards objects 
    methods:
    play(card) removes and returns card that was passed, if card is not in hand raises RuntimeError
    instance varaibles
    *none*
    '''

