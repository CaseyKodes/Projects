# black jack

import random as r
import os

class Card():
    # card objects have a value 
    # they also contain a string which is just how a card would be said or writen down
    def __init__(self, val, suit):
        self.Suit = suit
        self.Val = val
        self.string = f'{self.Val} {self.Suit} '
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
    def __init__(self, cards, balance):
        self.cards = list()
        self.balance = balance
        self.betSize = int()
        self.doubled = False
        self.insure = False
        self.split = False
        self.splitAmounts = list()
        self.doubleArray = list()
        self.bj = False
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
    def getDoubled(self):
        return self.doubled
    def setDoubled(self, boolean):
        self.doubled = boolean
    def getBalance(self):
        return self.balance
    def setBalance(self, newB):
        self.balance = newB
    def changeBalance(self, diff):
        self.balance = self.balance + diff
    def getbs(self):
        return self.betSize
    def setbs(self, nb):
        self.betSize = nb
    def getBJ(self):
        return self.bj
    def setBJ(self, boolean):
        self.bj = boolean
    def getIN(self):
        return self.insure
    def setIN(self, boolean):
        self.insure = boolean
    def getSplit(self):
        return self.split
    def setSplit(self, boolean):
        self.split = boolean
    def getSplitNums(self):
        return self.splitAmounts
    def addSplitNum(self, amount):
        self.splitAmounts.append(amount)
    def getDarray(self):
        return self.doubleArray
    def addDarray(self, boolean):
        self.doubleArray.append(boolean)

    def getValue(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.getVal() != 'Ace':
                value += card.getValnum()
            if card.getVal() == 'Ace':
                aces +=1

        # logic for aces is wrong 
        if aces>0:
            if (value+11+aces-1) > value+aces and (value+11+aces-1)<=21:
                return (value+11+aces-1)
            else:
                return value+aces
        return value

    def __str__(self):
        toreturn = ('Player has: ')
        for card in self.cards:
            toreturn += card.getStr()
            if card!=self.cards[-1]: toreturn+='& '
        return toreturn

class Shoe():
    def __init__(self, numdecks, balance):
        self.deck = list()
        self.dealer = Hand([], 0)
        self.players = list()
        self.balance = balance

        suits = ['s', 'h', 'c', 'd']
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
        for player in self.players:
            player.clearHand()
        self.dealer.clearHand()
        for card in range(2):
            for player in range(numPlayers):
                if player < len(self.players):
                    self.players[player].addCard(self.deck.pop(0))
                else:
                    self.players.append(Hand([self.deck.pop(0)], self.balance))
            self.dealer.addCard(self.deck.pop(0))
    
    def hit(self, player):
        self.players[player].addCard(self.deck.pop(0))
        print(self.players[player].getCards()[-1])
        if self.players[player].getValue() >21:
            print(f'Player {player+1} busts. With a value of {self.players[player].getValue()}')
            return 'break'
        elif self.players[player].getValue() <21:
            print(f'Player {player+1} with a value of {self.players[player].getValue()}')
            return 'continue'
        elif self.players[player].getValue() == 21:
            print(f'Player {player+1} has 21 and is done.')
            return 'break'
    
    def stand(self, player):
        print(f'Player {player+1} has {self.players[player].getValue()} and stands.')

    def doubleDown(self, player):
        player.setDoubled(True)
        player.addCard(self.deck.pop(0))
        print(player.getCards()[-1])
        print(f'Player has {player.getValue()} and is done since they doubled down.')
    
    def split(self, player:Hand, playernum):
        # we need to split the hand into two hands
        # but they need to belong to the same user 
        # we need to make 2 new hands one from each of the cards in the hand
        hand1 = Hand([player.getCards()[0]], 0)
        hand2 = Hand([player.getCards()[1]], 0)
        hands = [hand1, hand2]
        splitTotals = [0,0]
        dtoatals = [False, False]
        player.setSplit(True)
        i = -1
        for hand in hands:
            i+=1
            hand.addCard(self.deck.pop(0))
            print(f'{hand}')
            while True:
                try:
                    choice = input(f'Does player {playernum} want to hit, stand, split or double down?\nThey currently have {hand.getValue()}. ')
                    choice = choice.lower()
                    if choice[0]!='h' and choice[0:2]!='st' and choice[0:2]!='sp' and choice[0]!='d':
                        raise KeyError
                except:
                    print("Choice must be 'Hit', 'Stand', 'Split', or 'Double'.")
                    continue
                if len(self.deck)>1:
                    if choice[0] == 'h':
                        dtoatals[i] = False
                        toadd = self.deck.pop(0)
                        print(toadd)
                        hand.addCard(toadd)
                        if hand.getValue() == 21:
                            print(f'This split hand is done with a value of 21.')
                            splitTotals[i] = (hand.getValue())
                            break
                        elif hand.getValue() > 21:
                            print(f'Player {playernum} busts split hand with: {hand.getValue()}')
                            splitTotals[i] = (hand.getValue())
                            break
                        else:
                            continue
                        
                    elif choice[0:2] == 'st':
                        print(f'Player {playernum} stays on split hand with: {hand.getValue()}')
                        splitTotals[i] = (hand.getValue())
                        dtoatals[i] = False
                        break
                        
                    elif choice[0:2] == 'sp':
                        if len(hand.getCards()) > 2:
                            print('This player can not split they have more than 2 cards.')
                            continue
                        elif hand.getCards()[0].getValnum() != hand.getCards()[1].getValnum():
                            print('This player can not split they do not have a pair.')
                            continue
                        elif len(self.deck)<2:
                            print('There are not enough cards in the deck to split.')
                            continue

                        if (hand.getCards()[0].getValnum() == hand.getCards()[1].getValnum()
                            and len(self.deck)>2 and len(hand.getCards()) == 2):
                            toadd1, toadd2 = self.split(hand, playernum) # does eveyrthing in the split function
                            for num in toadd1:
                                splitTotals.append(num)
                            for TF in toadd2:
                                dtoatals.append(TF)
                            break
                        
                    elif choice[0] == 'd':
                        dtoatals[i] = True
                        toadd = self.deck.pop(0)
                        print(toadd)
                        hand.addCard(toadd)
                        print(f'Player {playernum} dobuled down, split hand ended with: {hand.getValue()}')
                        splitTotals[i] = hand.getValue()
                        break

        for i in range(len(dtoatals)):
            if splitTotals[i] != 0:
                player.addSplitNum(splitTotals[i])
                player.addDarray(dtoatals[i])

        return splitTotals, dtoatals

    def showHands(self):
        print('Players have:')
        i = 1
        for hand in self.players:
            print(f'{i} {hand}\nWith a current balance of {hand.getBalance()}')
            i+=1
        print('Dealers top card is:')
        print(self.dealer.getCards()[0])

def game():
    numdecks = 1
    numplayers = 4
    startingB = 1000
    betsize = 10
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
        try: 
            startingB = float(input("How much do players start with? "))
        except:
            print("Must input a number.")
            continue
        if (1+numplayers)*2<=numdecks*52:
            break
    shoe = Shoe(numdecks, startingB)
    shoe.shuffle()
    enough = True
    while len(shoe.deck)>2*(numplayers+1):
        dealerBlackJack = False
        i = 1
        shoe.deal(numplayers)
        os.system('cls')
        for hand in shoe.players:
            hand.setDoubled(False)
            hand.setBJ(False)
            hand.setIN(False)
            hand.setSplit(False)
            while True:
                isaNum = True
                try: 
                    betsize = float(input(f"What is the bet size, for player {i}? "))
                except:
                    print("Must input a number.")
                    isaNum = False
                if isaNum:
                    break
            hand.setbs(betsize)
            i+=1
        shoe.showHands()
        if shoe.dealer.getCards()[0].getVal() == 'Ace':
            if shoe.dealer.getValue() == 21:
                dealerBlackJack = True
                # dealer has blackjack and we do not need to run any hands
            for insuredPLay in range(len(shoe.players)):
                if not shoe.players[player].getBJ():
                    insur = ''
                    while True:
                        try:
                            insur = input(f'Does {insuredPLay+1} want to take insurance? ')
                            insur = insur.lower()
                            insur = insur[0]
                            if insur=='y' or insur=='n':
                                break
                            else: raise KeyError
                        except:
                            print('Answer must be "y" or "n"')
                            continue
                    if insur == 'y': shoe.players[player].setIN(True)

        for player in range(len(shoe.players)):
            if len(shoe.players[player].getCards())==2 and shoe.players[player].getValue()==21:
                print(f'Player {player+1} has blackjack!')
                shoe.players[player].setBJ(True)
                continue
            if dealerBlackJack: continue
            while True:
                try:
                    choice = input(f'Does player {player+1} want to hit, stand, split or double down?\nThey currently have {shoe.players[player].getValue()}. ')
                    choice = choice.lower()
                    if choice[0]!='h' and choice[0:2]!='st' and choice[0:2]!='sp' and choice[0]!='d':
                        raise KeyError
                except:
                    print("Choice must be 'Hit', 'Stand', 'Split', or 'Double'.")
                    continue
                try:
                    if choice[0] == 'h':
                        outcome = shoe.hit(player)
                        if outcome == 'break':
                            break
                    elif choice[0:2] == 'st':
                        shoe.stand(player)
                        break
                    elif choice[0:2] == 'sp':
                        if len(shoe.players[player].getCards()) > 2:
                            print('This player can not split they have more than 2 cards.')
                            continue
                        elif shoe.players[player].getCards()[0].getValnum() != shoe.players[player].getCards()[1].getValnum():
                            print('This player can not split they do not have a pair.')
                            continue
                        elif len(shoe.deck)<2:
                            print('There are not enough cards in the deck to split.')
                            continue
                        if (shoe.players[player].getCards()[0].getValnum() == shoe.players[player].getCards()[1].getValnum()
                            and len(shoe.deck)>2 and len(shoe.players[player].getCards()) == 2):
                            shoe.split(shoe.players[player], player+1) # does eveyrthing in the split function
                            break
                        
                    elif choice[0] == 'd':
                        shoe.doubleDown(shoe.players[player])
                        break
                except Exception as e:
                    print('Ran out of cards in the deck, hands are final.', e)
                    enough = False
                    break
            if not enough:
                break
        dealerBust = False
        print(f'Dealers full hand is:')
        for card in shoe.dealer.getCards():
            print(card)
        while True:
            try:
                if shoe.dealer.getValue() < 17:
                    toadd = shoe.deck.pop(0)
                    print(f'Dealer hits: {toadd}')
                    shoe.dealer.addCard(toadd)
                elif shoe.dealer.getValue() > 21:
                    print('Dealer busts.')
                    dealerBust = True
                    break
                else: # if dealer is between 17 and 21
                    print('Dealer stands.')
                    break
            except:
                    print('Ran out of cards in the deck, hands are final.')
                    enough = False
                    break
        print(f'Dealer final value is {shoe.dealer.getValue()}')

        if dealerBust:
            for player in range(len(shoe.players)):
                if shoe.players[player].getDoubled():
                    times = 2
                elif shoe.players[player].getBJ():
                    times = 2.5
                else: times = 1

                if shoe.players[player].getSplit():
                    wins = 0
                    loses = 0
                    extraloses = 0
                    extrawins = 0
                    print(shoe.players[player].getSplitNums())
                    print(shoe.players[player].getDarray())
                    i = -1
                    for num in shoe.players[player].getSplitNums():
                        i+=1
                        if num > 21:
                            loses+=1
                            if shoe.players[player].getDarray()[i]:
                                extraloses +=1
                        elif num<= 21:
                            wins +=1
                            if shoe.players[player].getDarray()[i]:
                                extrawins +=1
                    shoe.players[player].changeBalance(shoe.players[player].getbs()*(wins+extrawins-loses-extraloses))
                    print(f'Player {player+1} split their hand, they won {wins} times and lost {loses} times. Updated balance = {shoe.players[player].getBalance()}')
                    continue

                if shoe.players[player].getBJ():
                    shoe.players[player].changeBalance(shoe.players[player].getbs()*times)
                    print(f'Player {player+1} beat the dealer, with Black Jack. Updated balance = {shoe.players[player].getBalance()}')
                    continue

                if shoe.players[player].getValue() <= 21:
                    shoe.players[player].changeBalance(shoe.players[player].getbs()*times)
                    print(f'Player {player+1} beat the dealer. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
                elif shoe.players[player].getValue() > 21:
                    shoe.players[player].changeBalance(-1*shoe.players[player].getbs()*times)
                    print(f'Player {player+1} busts. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
                
        elif not dealerBust:
            for player in range(len(shoe.players)):
                if shoe.players[player].getDoubled():
                    times = 2
                elif shoe.players[player].getBJ():
                    times = 2.5
                else: times = 1

                if shoe.players[player].getSplit():
                    wins = 0
                    loses = 0
                    extraloses = 0
                    extrawins = 0
                    print(shoe.players[player].getSplitNums())
                    print(shoe.players[player].getDarray())
                    i = -1
                    for num in shoe.players[player].getSplitNums():
                        i +=1
                        if num > 21:
                            loses+=1
                            if shoe.players[player].getDarray()[i]:
                                extraloses +=1
                        elif num <= 21:
                            if num>shoe.dealer.getValue():
                                wins +=1
                                if shoe.players[player].getDarray()[i]:
                                    extrawins +=1
                            elif num < shoe.dealer.getValue():
                                loses +=1
                                if shoe.players[player].getDarray()[i]:
                                    extraloses +=1
                        
                    shoe.players[player].changeBalance(shoe.players[player].getbs()*(wins+extrawins-loses-extraloses))
                    print(f'Player {player+1} split their hand, they won {wins} times and lost {loses} times. Updated balance = {shoe.players[player].getBalance()}')
                    continue

                if shoe.players[player].getBJ():
                    if dealerBlackJack:
                        print(f'Both {player+1} and Dealer have Black Jack so they push. Updated balance = {shoe.players[player].getBalance()}')
                    else:
                        shoe.players[player].changeBalance(shoe.players[player].getbs()*times)
                        print(f'Player {player+1} beat the dealer, with Black Jack. Updated balance = {shoe.players[player].getBalance()}')
                    continue

                if shoe.players[player].getIN() and not dealerBlackJack:
                    shoe.players[player].changeBalance(-.5*shoe.players[player].getbs())
                    print(f'Player {player+1} took insurance and lost. Updated balance = {shoe.players[player].getBalance()}')
                    continue
                elif shoe.players[player].getIN() and dealerBlackJack:
                    shoe.players[player].changeBalance(shoe.players[player].getbs())
                    print(f'Player {player+1} took insurance and Won. Updated balance = {shoe.players[player].getBalance()}')
                    continue

                if shoe.players[player].getValue() < shoe.dealer.getValue():
                    shoe.players[player].changeBalance(-1*shoe.players[player].getbs()*times)
                    print(f'Player {player+1} lost to dealer. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
                elif shoe.players[player].getValue() == shoe.dealer.getValue():
                    print(f'Player {player+1} pushes with the dealer. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
                elif shoe.players[player].getValue() > shoe.dealer.getValue() and shoe.players[player].getValue() < 22:
                    shoe.players[player].changeBalance(shoe.players[player].getbs()*times)
                    print(f'Player {player+1} beat the dealer. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
                elif shoe.players[player].getValue() > 21:
                    shoe.players[player].changeBalance(-1*shoe.players[player].getbs()*times)
                    print(f'Player {player+1} busts. With a value of {shoe.players[player].getValue()}. Updated balance = {shoe.players[player].getBalance()}')
        
        while True:
            if enough:
                exit = input('Enter any character to play the next hand. \nEnter 0 to exit. ')
                if exit != '0': break
                else: print('Thanks for playing.'); quit()
            else:
                print('Shoe is empty thank you for playing.')
                quit()
    print('Not enough cards for the number of players specified thank you for playing.')

game()