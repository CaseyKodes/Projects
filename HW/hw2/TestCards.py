# TestCards.py

import unittest
from Cards import *

'''
uses unittests to test all classes in Cards.py
'''

class TestDeck(unittest.TestCase):

    def test_init(self): # tests that self.suit and self.values work
        deckin = Deck(['fire', 'water'], [1,2])

        self.assertEqual(deckin.suits, ['fire', 'water'])
        self.assertEqual(deckin.values, [1,2])

    def test_len(self): # tests len
        deck1 = Deck(["water", "fire", "air"], [2,3,4,5,6])

        self.assertEqual(len(deck1), 15)

    def test_sort(self): # tests sort which sorts alphabetically by suit then numerically by value
        deck6 = Deck(["jump", "fly", "walk"], [45,47,46])
        expected = Deck(["fly", "jump", "walk"], [45,46,47])

        deck6.shuffle()
        deck6.sort()
        
        self.assertEqual(repr(deck6), repr(expected))

    def test_repr(self): # test repr of deck
        deck2 = Deck(["dox", "space"], [5,6])
        expected = "Deck: Card (5 of dox), Card (6 of dox), Card (5 of space), Card (6 of space), "

        self.assertEqual(repr(deck2), expected)

    def test_shuffle(self): # test shuffle by assertNotEqual
        deck3 = Deck(["tree", "stone"], [9,8,7,6])
        shuffled = deck3.shuffle()

        self.assertNotEqual(repr(deck3), repr(shuffled))

    def test_drawtop(self): # test draw top and what error is raised 
        deck4 = Deck()
        deck7 = Deck([], [])
        expected = Card("spades", 13)

        self.assertEqual(deck4.draw_top(), expected)
        #self.assertRaises(RuntimeError, deck7.draw_top())

class TestCard(unittest.TestCase):

    def test_init(self): # tests self.value and self.suit
        cardin = Card("perfect", 7)

        self.assertEqual(cardin.suit, "perfect")
        self.assertEqual(cardin.value, 7)

    def test_repr(self): # tests repr of card
        card = Card("glove", 9)
        expected = "Card (9 of glove)"
        self.assertEqual(repr(card), expected)

    def test_lt(self): # test less than cards are less than by alphabetical suit (a<b) then by value (6<7) 
        card1 = Card("ace", 4)
        card2 = Card("ace", 7)
        card3 = Card("spade", 4)
        card4 = Card("spade", 7)

        self.assertLess(card2, card3) # 7 of ace < 4 of spade = true
        self.assertLess(card1, card2) # 4 of ace < 7 of ace = true
        self.assertLess(card2, card4) # 7 of ace < 7 of spade = true
    
    def test_eq(self): # tests equal card are equal when they have the same suit and value
        card5 = Card("box", 8)
        card6 = Card("box", 4)
        card7 = Card("hop", 8)
        card8 = Card("box", 8)

        self.assertNotEqual(card5, card6)
        self.assertNotEqual(card5, card7)
        self.assertEqual(card5, card8)

class TestHand(unittest.TestCase):

    def test_init(self): # test self.suit and self.value 
        handin = Hand(['gift'], [4,5,6,7])

        self.assertEqual(handin.suits, ['gift'])
        self.assertEqual(handin.values, [4,5,6,7])
    
    def test_play(self): # tests play and what error is raised 
        hand = Hand(["fox", "cat"], [3,4,5])
        expected = Card("fox", 4)

        self.assertEqual(hand.play(Card("fox", 4)), expected)
        #self.assertRaises(RuntimeError, hand.play(Card("frog", 8)))
    
    def test_repr(self): # test repr of hand 
        hand2 = Hand(["dox"] , [5,6])
        expected = "Hand: Card (5 of dox), Card (6 of dox), "

        self.assertEqual(repr(hand2), expected)


unittest.main()