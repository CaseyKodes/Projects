# black jack

import random as r
import os

class Card():
    # card objects have a value 
    # they also contain a string which is just how a card would be said or writen down
    def __init__(self, val, suit):
        self.Suit = suit
        self.Val = val
        self.string = f'{self.Val} of {self.Suit} '
    def getVal(self):
        return self.Val
    def getValnum(self):
        if self.Val == 'Ace' :
            return [1, 11]
        if self.Val == 'King' :
            return 10
        if self.Val == 'Queen' :
            return 10
        if self.Val == 'Jack':
            return 10
        return self.Val
    def getStr(self):
        return self.string
    def __str__(self):
        return self.getStr()     

class Hand():
    # hand objects contain a list of card objects
    # we can add and remove cards from a hand, clear a hand
    def __init__(self, cards):
        self.cards = list()
        for card in cards:
            self.cards.append(card)
    def getCards(self):
        return self.cards
    def addCard(self, card):
        self.cards.append(card)
    def removeCard(self, index):
        try:
            self.cards.pop(index)
        except:
            print('There is no card at that index.')
    def clearHand(self):
        self.cards.clear()

    def getValue(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.getVal() != 'Ace':
                value += card.getValnum()
            if card.getVal() == 'Ace':
                aces +=1

        # logic for aces is wrong 
        if aces<1:
            return value
        elif aces==1:
            if value+11 <=21:
                return value
            else: return value+1
        else: return value + aces

    def __str__(self):
        toreturn = ('Player has: ')
        for card in self.cards:
            toreturn += card.getStr()
            if card!=self.cards[-1]: toreturn+='& '
        return toreturn

class Shoe():
    def __init__(self, numdecks):
        self.deck = list()
        self.dealer = Hand([])
        self.players = list()

        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        for deck in range(numdecks):
            for suit in suits:
                for value in values:
                    self.deck.append(Card(value, suit))

    def shuffle(self):  
        shuffled = []
        while len(self.deck)>0:
            spot = r.randint(0, len(self.deck)-1)
            shuffled.append(self.deck.pop(spot))
        self.deck = shuffled
    
    def deal(self, numPlayers):
        self.players.clear()
        self.dealer.clearHand()
        for card in range(2):
            for player in range(numPlayers):
                if player < len(self.players):
                    self.players[player].addCard(self.deck.pop(0))
                else:
                    self.players.append(Hand([self.deck.pop(0)]))
            self.dealer.addCard(self.deck.pop(0))
    
    def hit(self, player):
        self.players[player].addCard(self.deck.pop(0))
        print(self.players[player].getCards()[-1])
        if self.players[player].getValue() >21:
            print(f'Player {player+1} busts.')
            return 'break'
        elif self.players[player].getValue() <21:
            return 'continue'
        elif self.players[player].getValue() == 21:
            print(f'Player {player+1} has 21 and is done.')
            return 'break'
    
    def stand(self, player):
        print(f'Player {player+1} has {self.players[player].getValue()} and stands.')

    def doubleDown(self, player):
        self.players[player].addCard(self.deck.pop(0))
        print(self.players[player].getCards()[-1])
        print(f'Player {player+1} has {self.players[player].getValue()} and is done since they doubled down.')

    def showHands(self):
        print('Players have:')
        i = 1
        for hand in self.players:
            print(f'{i} {hand}- with a value of {hand.getValue()}')
            i+=1
        print('Dealers top card is:')
        print(self.dealer.getCards()[0])

def game():
    numdecks = 1
    numplayers = 4
    while True:
        # getting user input
        try: 
            numdecks = int(input("How many decks are we playing with? "))
        except:
            print("Must input a number.")
            continue
        try:
            numplayers = int(input('How many players should there be? '))
        except:
            print("Must input a number.")
            continue
        if numplayers*2<=numdecks*52:
            break
    shoe = Shoe(numdecks)
    shoe.shuffle()
    while len(shoe.deck)>2*numplayers:
        shoe.deal(numplayers)
        os.system('cls')
        shoe.showHands()
        for player in range(len(shoe.players)):
            while True:
                try:
                    choice = input(f'Does player {player+1} want to hit, stand or double down?\nThey currently have {shoe.players[player].getValue()}. ')
                    choice = choice.lower()
                    if choice[0]!='h' and choice!='s' and choice!='d':
                        raise KeyError
                except:
                    print("Choice must be 'Hit', 'Stand', or 'Double'.")
                    continue
                if choice[0] == 'h':
                    outcome = shoe.hit(player)
                    if outcome == 'break':
                        break
                elif choice[0] == 's':
                    shoe.stand(player)
                    break
                elif choice[0] == 'd':
                    shoe.doubleDown(player)
                    break

        dealerBust = False
        print(f'Dealers full hand is:')
        for card in shoe.dealer.getCards():
            print(card)
        print(f'With a value of {shoe.dealer.getValue()}')
        while True:
            if shoe.dealer.getValue() < 17:
                toadd = shoe.deck.pop(0)
                print(toadd)
                shoe.dealer.addCard(toadd)
            elif shoe.dealer.getValue() > 21:
                print('Dealer busts.')
                dealerBust = True
                break
            else: # if dealer is between 17 and 21
                print('Dealer stands.')
                break
        print(f'Dealer final value is {shoe.dealer.getValue()}')

        if dealerBust:
            for player in range(len(shoe.players)):
                if shoe.players[player].getValue() <= 21:
                    print(f'Player {player+1} beat the dealer. With a value of {shoe.players[player].getValue()}')
                elif shoe.players[player].getValue > 21:
                    print(f'Player {player+1} busts. With a value of {shoe.players[player].getValue()}')
        elif not dealerBust:
            for player in range(len(shoe.players)):
                if shoe.players[player].getValue() < shoe.dealer.getValue():
                    print(f'Player {player+1} lost to dealer. With a value of {shoe.players[player].getValue()}')
                elif shoe.players[player].getValue() == shoe.dealer.getValue():
                    print(f'Player {player+1} pushes with the dealer. With a value of {shoe.players[player].getValue()}')
                elif shoe.players[player].getValue() > shoe.dealer.getValue() and shoe.players[player].getValue() < 22:
                    print(f'Player {player+1} beat the dealer. With a value of {shoe.players[player].getValue()}')
                elif shoe.players[player].getValue() > 21:
                    print(f'Player {player+1} busts. With a value of {shoe.players[player].getValue()}')
        
        while True:
            exit = input('Enter any character to play the next hand. \nEnter 0 to exit. ')
            if exit and exit !='0':
                break
            elif exit == '0':
                quit()

game()