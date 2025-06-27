# trying to make a poker simulator 
 
# currently we can 
    # made card and hand class and they have been integrated so 
    # the working functions work with them, in some cases the functions 
    # imporoved slihtly now that we abstracted to new classes

    # deal hands to any number of players so long as we have enough cards
    # the hands can be any size as long as we have enough cards 
    # we can deal a board of 5 cards
    # we can calculate the rank of each players hand 
    # break ties between players if they have te same hand rank
    # deal any number of boards 
# currently we can NOT
    # 
# next step
    # impliment dead and wild cards
        # for dead we just need to make a dead card list and if the card we are looking at is in that list we do not count it for anything
        # for wild we count it as every suit but also need to consider it as every rank, this gets tricky since if we just add 1 to every rank 
        # for every wild card this program will always think a person has a stright even if they have less than 5 cards 

import random as r

class Rankings(): # basically just a place to hold these arrays which tell us the ordering of hands 
    HandValueOrder = ['High Card', 'Pair', 'Two Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House', 'Four of a kind', 'Straight Flush']
    CardValueOrder = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def getCrank():
        return Rankings.CardValueOrder
    def getHrank():
        return Rankings.HandValueOrder

class Card():
    # card objects have a value and suit which are the defining attributes 
    # they also contain a string which is just how a card would be said or writen down
    # can directly compare cards to see which one is a higher value
    def __init__(self, val, suit):
        self.Suit = suit
        self.Val = val
        self.string = f'{self.Val} of {self.Suit} '
        self.cr = Rankings.getCrank()
    def getVal(self):
        return self.Val
    def getValenum(self):
        if self.Val == 'Ace' :
            return '14'
        if self.Val == 'King' :
            return '13'
        if self.Val == 'Queen' :
            return '12'
        if self.Val == 'Jack':
            return '11'
        return self.Val
    def getSuit(self):
        return self.Suit
    def getStr(self):
        return self.string
    def __str__(self):
        return self.getStr()
    def __eq__(self, other):
        return self.cr.index(self.getVal()) == self.cr.index(other.getVal())
    def __ne__(self, other):
        return not self==other
    def __lt__(self, other):
        return self.cr.index(self.getVal()) < self.cr.index(other.getVal())
    def __gt__(self, other):
        return self.cr.index(self.getVal()) > self.cr.index(other.getVal())
    def __le__(self, other):
        return (self<other or self==other)
    def __ge__(self, other):
        return (self>other or self==other)       

class Hand():
    # hand objects contain a list of card objects
    # they also have a rank that depends on the cards in a players hand and the cards on the board 
    # we can add and remove cards from a hand, clear a hand, get and set the rank of a hand
    def __init__(self, cards, numboards):
        self.cards = list()
        self.rank = ['High Card']*max(numboards, 1) # default lowest value of a hand
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

    # think these two might have to change to accomodate multiple boards 
    # added the index part
    def setRank(self, rank, index):
        self.rank[index] = rank
    def getRank(self, index):
        return self.rank[index]
    def getRanks(self):
        return self.rank
      
    def __str__(self):
        toreturn = ('Hand is: ')
        for card in self.cards:
            toreturn += card.getStr()
        return toreturn
    
class Deck():
    # deck objects contain 52 cards, 4 suits, an 13, values
    # it contains lists of hands that players has
    # it keeps track of the current deck after being dealt and we can save what cards are burnt but there is no use for those yet
    # we have funcitons to deal hands to players, deal a board of shared cards, shuffle the deck, and calculate the rank of each hand

    def __init__(self, wild, dead): # creates a deck of 52 cards, 13 ranks and 4 suits
        self.deck = list()
        self.playerHands = list()
        self.boardList = []
        self.burnt = list()
        self.winnerstr = str()
        self.winningLevel = list()
        self.hr = Rankings.getHrank()
        self.cr = Rankings.getCrank()
        self.numBorads = int()
        self.dead = dead
        self.wild = wild

        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))

    def __str__(self):
        toprint = ''
        for card in self.deck:
            toprint += card.getStr()
        return(toprint)

    def shuffle(self): # shuffles a deck 
        shuffled = []
        while len(self.deck)>0:
            spot = r.randint(0, len(self.deck)-1)
            shuffled.append(self.deck.pop(spot))
        self.deck = shuffled
    
    def perfectShuffle(self, numtimes): 
        # shuffeles a deck as if someone spit it perfectly in have and alternated exactly between each half
        # probably just for fun 
        # split deck in half 
        # now we need to take one card from each half and add it back to the new shuffeled deck
        for time in range(numtimes):
            newdeck = []
            halflen = int(len(self.deck)/2)
            for card in range(halflen):
                halfway = self.deck.pop(int(len(self.deck)/2))
                first = self.deck.pop(0)
                newdeck.append(first)
                newdeck.append(halfway)
            self.deck = newdeck

    def deal(self, numPlayers, handsize, numboards): # deals to a numPlayers number of players a handsize sized hand from the top of the deck 
        for card in range(handsize):
            for player in range(numPlayers):
                if player < len(self.playerHands):
                    self.playerHands[player].addCard(self.deck.pop(0))
                else:
                    self.playerHands.append(Hand([self.deck.pop(0)], numboards))
        self.numBorads = numboards
        if numboards==1:
            self.dealSingleBoard()
        elif numboards==2:
            self.dealDoubleBoard()
        else:
            for i in range(numboards):
                self.dealSingleBoard()
                
    def dealSingleBoard(self): # deals a flop turn and river
        # want to figure out how to deal 2 boards 
        # we would need to store them in different places 
        boardDict = {'Flop':[], 'Turn':[], 'River':[]}
        self.burnt.append(self.deck.pop(0))
        for i in range(3):
            boardDict['Flop'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict['Turn'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict['River'].append(self.deck.pop(0))
        self.boardList.append([boardDict['Flop'] + boardDict['Turn'] + boardDict['River']])
    
    def dealDoubleBoard(self):
        # same logic as for single board but we need to do flop flopr, turn turn, river river
        boardDict1 = {'Flop':[], 'Turn':[], 'River':[]}
        boardDict2 = {'Flop':[], 'Turn':[], 'River':[]}
        self.burnt.append(self.deck.pop(0))
        for i in range(3):
            boardDict1['Flop'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        for i in range(3):
            boardDict2['Flop'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict1['Turn'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict2['Turn'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict1['River'].append(self.deck.pop(0))
        self.burnt.append(self.deck.pop(0))
        boardDict2['River'].append(self.deck.pop(0))
        self.boardList.append([boardDict1['Flop'] + boardDict1['Turn'] + boardDict1['River']])
        self.boardList.append([boardDict2['Flop'] + boardDict2['Turn'] + boardDict2['River']])
        
    def calcHandRanks(self): # figure out which hand has the best hand 
        # need to look at each hand in player hands and every card on the board

        # make a dicr that has all the players hand types originally set to high 
        # card then we will update their hand type if they make a better hand
        # since it is possible we did multiple baords we need to check if we did 1 or two 
        # if we did 1 nothing changes 
        # if we did 2 we have to calculate the hands on each board 
        for hand in self.playerHands:
            board=0
            for rank in hand.getRanks():
                # finding flushes 
                # instead of just adding to something telling us if we have the suits lets move the cards to be sorted by suit
                suitcount = {'Spades':[], 'Hearts':[], 'Clubs':[], 'Diamonds':[]}
                for card in hand.getCards():
                    if card.getVal() in self.dead:
                        continue
                    suitcount[card.getSuit()].append(card)
                if len(self.boardList) > 0:
                    for b in self.boardList[board]:
                        for card in b:
                            if card.getVal() in self.dead:
                                continue
                            suitcount[card.getSuit()].append(card)
                if any(len(x) > 4 for x in suitcount.values()):
                    # if we are here we know we have a flush now we want to check if those cards are in order 
                    # looking for straight flush
                    for key, value in suitcount.items():
                        rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
                         '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                        for card in value:
                            if card.getVal() in self.dead:
                                continue
                            rankcount[card.getVal()]+=1
                        straightlist = []
                        straightlist.append(rankcount['Ace'])
                        for value in rankcount.values():
                            straightlist.append(value)
                        straightLenghth = 5 # x = length of straight
                        for starter in range(len(straightlist)-straightLenghth):
                            if all(straightlist[starter:starter+straightLenghth]):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Straight Flush'):
                                    hand.setRank('Straight Flush', board)
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Flush'):
                        hand.setRank('Flush', board)

                # filling how many instances of a card value there are 
                rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
                             '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                if len(self.boardList) > 0:
                    for b in self.boardList[board]:
                        for card in b:
                            if card.getVal() in self.dead:
                                continue
                            rankcount[card.getVal()] += 1
                for card in hand.getCards():
                    if card.getVal() in self.dead:
                        continue
                    rankcount[card.getVal()]+=1

                # find straights
                straightlist = []
                straightlist.append(rankcount['Ace'])
                for value in rankcount.values():
                    straightlist.append(value)
                straightLenghth = 5 # x = length of straight
                for starter in range(len(straightlist)-straightLenghth):
                    if all(straightlist[starter:starter+straightLenghth]):
                        if self.hr.index(hand.getRank(board)) < self.hr.index('Straight'):
                            hand.setRank('Straight', board)

                # determining based off the number of instances of that card value what type of hand a player has
                # this is for pairs two pairs three of a kind full house and four of a kind
                if any(x==4 for x in rankcount.values()):
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Four of a kind'):
                        hand.setRank('Four of a kind', board)
                elif any(x==3 for x in rankcount.values()) and any(y==2 for y in rankcount.values()):
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Full House'):
                        hand.setRank('Full House', board)
                elif any(x==3 for x in rankcount.values()):
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Three of a kind'):
                        hand.setRank('Three of a kind', board)
                elif any(x==2 for x in rankcount.values()):
                    for key in rankcount.keys():
                        if rankcount[key] == 2:
                            smaller = {key: value for key, value in rankcount.items()}
                            smaller.pop(key)
                            if any(y==2 for y in smaller.values()):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Two Pair'):
                                    hand.setRank('Two Pair', board)
                                break 
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Pair'):
                        hand.setRank('Pair', board)
                board+=1  
            
    def calcWinner(self): # from the player hand ranks find which is the best
        toreturn = f'Dead cards were {self.dead} \nWild cards were {self.wild}\n'
        loopover = max(1, len(self.boardList))
        for boardIndex in range(loopover):
            winnershand = []
            winnerslevel = ''
            for playersHand in self.playerHands:
                if len(winnerslevel)==0:
                    winnerslevel=(playersHand.getRank(boardIndex))
                    winnershand.append(playersHand)
                else:
                    if (self.hr.index(playersHand.getRank(boardIndex)) 
                        > self.hr.index(winnerslevel)):
                        # we have a worse hand then the new one
                        winnerslevel = playersHand.getRank(boardIndex)
                        winnershand.clear()
                        winnershand.append(playersHand)
                    elif (self.hr.index(playersHand.getRank(boardIndex)) 
                        < self.hr.index(winnerslevel)):
                        # we have the better hand do nothing 
                        continue
                    elif (self.hr.index(playersHand.getRank(boardIndex)) 
                        == self.hr.index(winnerslevel)):
                        # we have equal rank hands
                        # we  then need to call the tiebreak function 
                        winnershand.append(playersHand)
                        winnershand = self.tiebreak(winnershand, winnerslevel, boardIndex)
            toreturn += f'Winning hand rank on Board number {boardIndex+1} was {winnerslevel} with a board of: \n'
            if len(self.boardList)>0:
                for b in self.boardList[boardIndex]:
                    for card in b:
                        toreturn += card.getStr()
            toreturn += '\nAnd a hand of: \n'
            for hand in winnershand:
                for card in hand.getCards():
                    toreturn += card.getStr()
                if len(winnershand) > 1 and not hand == winnershand[-1]:
                    toreturn += '\nand '
            toreturn += '\n'*2
            self.winningLevel.append(winnerslevel)
        self.winnerstr=toreturn
        
    def tiebreak(self, hands, level, boardIndex):
        # make a list that has all hands with all cards in a hand including board and hole cards
        fullHand = [[]]*len(hands)
        for hand in range(len(hands)):
            new = []
            if len(self.boardList)>0:
                for b in self.boardList[boardIndex]:
                    for card in b:
                        if card.getVal() in self.dead:
                            continue
                        new.append(card)
            for card in hands[hand].getCards():
                if card.getVal() in self.dead:
                    continue
                new.append(card)
            fullHand[hand] = new

        # sort that each list of cards in each hand so we can compare the lists easily
        for hand in fullHand:
            hand.sort(reverse=True)
        
        # seting how many cards make up a full hand if we have over 5+ cards we only 
        # look at 5 but if we have less than 5 we look at all of them
        checkmax = bool()
        if len(fullHand[0])>4 and len(fullHand[-1])>4:
            top = 5
            checkmax = True
        else:
            top = min(len(fullHand[0]), len(fullHand[-1])) 
            # we set the top to the minimum amount of cards then we know that if we check the min amount of cards in both we can say the one that has more cards wins
        
        # one case for each hand type
        match level:
            case 'High Card':
                #print('case High Card solved')  
                for i in range(0, top):
                    if fullHand[0][i] == fullHand[-1][i]:
                        continue
                    elif fullHand[0][i] > fullHand[-1][i]:
                        hands.pop(-1)
                        return hands
                    elif fullHand[0][i] < fullHand[-1][i]:
                        while len(hands) > 1:
                            hands.pop(0)
                        return hands
                # we have checked all cards in range top
                # check if both hands have lengths above 5
                if (checkmax):
                    pass
                elif (len(fullHand[0])==len(fullHand[-1])):
                    pass
                else:
                    # pop the hand with less cards 
                    # since we know we do not have the same amount of cards in both 
                    if len(fullHand[0]) > len(fullHand[-1]):
                        hands.pop(-1)
                        return hands
                    else:
                        while len(hands)>1:
                            hands.pop(0)
                        return hands
                pass
            case 'Pair':
                #print('case Pair solved')
                # need to find the cards that the players have pairs of and compare those first
                    # this works if one player wins directly from the pair they have
                    # but if players have the same pair we then need to check their highest cards that are not paired
                    # also need to keep in mind that we only want to check 5 cards max
                for cardSpot1 in range(len(fullHand[0])-1):
                    if fullHand[0][cardSpot1] == fullHand[0][cardSpot1+1]:
                        for cardSpot2 in range(len(fullHand[-1])-1):
                            if fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+1]:
                                # now we compare the pairs 
                                if fullHand[0][cardSpot1] == fullHand[-1][cardSpot2]:
                                    # here we now need to check their highest cards against each other
                                        # i just coppied the code from high card can we make that better somehow
                                    newcheck1 = [item for item in fullHand[0] if item!=fullHand[0][cardSpot1]]
                                    newcheck2 = [item for item in fullHand[-1] if item!=fullHand[-1][cardSpot2]]
                                    for i in range(min(len(newcheck1), len(newcheck2))):
                                        if newcheck1[i] == newcheck2[i]:
                                            continue
                                        elif newcheck1[i] > newcheck2[i]:
                                            hands.pop(-1)
                                            return hands
                                        elif newcheck1[i] < newcheck2[i]:
                                            while len(hands) > 1:
                                                hands.pop(0)
                                            return hands
                                    # we have checked all cards in range top
                                    # check if both hands have lengths above 5
                                    if (checkmax):
                                        pass
                                    elif (len(fullHand[0])==len(fullHand[-1])):
                                        pass
                                    else:
                                        # pop the hand with less cards 
                                        # since we know we do not have the same amount of cards in both 
                                        if len(fullHand[0]) > len(fullHand[-1]):
                                            hands.pop(-1)
                                            return hands
                                        else:
                                            while len(hands)>1:
                                                hands.pop(0)
                                            return hands
                                elif fullHand[0][cardSpot1] > fullHand[-1][cardSpot2]:
                                    hands.pop(-1)
                                    return hands
                                elif fullHand[0][cardSpot1] < fullHand[-1][cardSpot2]:
                                    while len(hands) > 1:
                                        hands.pop(0)
                                    return hands
                            else: continue
                    else: continue
                pass
            case 'Two Pair':
                #print('case Two Pair solved')
                # can use similar logic here as for the full house case
                for cardSpot1 in range(len(fullHand[0])-1):
                    if fullHand[0][cardSpot1] == fullHand[0][cardSpot1+1]:
                        for cardSpot2 in range(len(fullHand[-1])-1):
                            if fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+1]:
                                if fullHand[0][cardSpot1] == fullHand[-1][cardSpot2]: 
                                    #print('top pairs are the same')
                                    # since the higher pair is the same we need to check the lower pair
                                    # insetad of making things not to check make a new smaller list for each
                                    smaller1 = [item for item in fullHand[0] if item != fullHand[0][cardSpot1]]
                                    smaller2 = [item for item in fullHand[-1] if item != fullHand[-1][cardSpot2]]
                                    for secondCheck1 in range(len(smaller1)-1):
                                        if smaller1[secondCheck1] == smaller1[secondCheck1+1]:
                                            for secondCheck2 in range(len(smaller2)-1):
                                                if smaller2[secondCheck2] == smaller2[secondCheck2+1]:
                                                    # now we can actually compare
                                                    if smaller1[secondCheck1] == smaller2[secondCheck2]:
                                                        #print('bottom pairs are the same')
                                                        # for two pair we actually do care about the fifth card
                                                        # form all the avalible cards we want to remove ones that are paired
                                                        # then look at the biggested card which should be the first since we 
                                                        # sorted in reverse order 
                                                        tocheck1 = [item for item in smaller1 if item != smaller1[secondCheck1]]
                                                        tocheck2 = [item for item in smaller2 if item != smaller2[secondCheck2]]
                                                        if(len(tocheck1)>0 and len(tocheck2)>0):
                                                            pass
                                                        else:
                                                            # we know that one of the hands has no more cards remove that hand
                                                            if len(tocheck1)==0:
                                                                while len(hands)>1:
                                                                    hands.pop(0)
                                                                return hands
                                                            else:
                                                                hands.pop(-1)
                                                                return hands
                                                        if tocheck1[0] == tocheck2[0]:
                                                            #print('highest card outside of pair is the same')
                                                            return hands
                                                        elif tocheck1[0] < tocheck2[0]:
                                                            while len(hands)>1:
                                                                hands.pop(0)
                                                            return hands
                                                        elif tocheck1[0] > tocheck2[0]:
                                                            hands.pop(-1)
                                                            return hands
                                                    elif fullHand[0][secondCheck1] > fullHand[-1][secondCheck2]:
                                                        hands.pop(-1)
                                                        return hands
                                                    elif fullHand[0][secondCheck1] < fullHand[-1][secondCheck2]:
                                                        while len(hands) > 1:
                                                            hands.pop(0)
                                                        return hands
                                                else: continue
                                        else: continue
                                    pass
                                elif fullHand[0][cardSpot1] > fullHand[-1][cardSpot2]:
                                    hands.pop(-1)
                                    return hands
                                elif fullHand[0][cardSpot1] < fullHand[-1][cardSpot2]:
                                    while len(hands) > 1:
                                        hands.pop(0)
                                    return hands
                            else: continue
                    else: continue
                pass
            case 'Three of a kind':
                #print('case Three of a kind solved')
                # could be similary to pair except now we look at three at a time
                for cardSpot1 in range(len(fullHand[0])-2):
                    if fullHand[0][cardSpot1] == fullHand[0][cardSpot1+1] and fullHand[0][cardSpot1] == fullHand[0][cardSpot1+2]:
                        for cardSpot2 in range(len(fullHand[-1])-2):
                            if fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+1] and fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+2]:
                                # now we compare the pairs 
                                if fullHand[0][cardSpot1] == fullHand[-1][cardSpot2]:
                                    # here we now need to check their highest cards against each other
                                        # i just coppied the code from high card can we make that better somehow
                                    smaller1 = [item for item in fullHand[0] if item!=fullHand[0][cardSpot1]]
                                    smaller2 = [item for item in fullHand[-1] if item!=fullHand[-1][cardSpot2]]
                                    for i in range(min(len(smaller1), len(smaller2))):
                                        if smaller1[i] == smaller2[i]:
                                            continue
                                        elif smaller1[i] > smaller2[i]:
                                            hands.pop(-1)
                                            return hands
                                        elif smaller1[i] < smaller2[i]:
                                            while len(hands) > 1:
                                                hands.pop(0)
                                            return hands
                                    # we have checked all cards in range top
                                    # check if both hands have lengths above 5
                                    if (checkmax):
                                        pass
                                    elif (len(fullHand[0])==len(fullHand[-1])):
                                        pass
                                    else:
                                        # pop the hand with less cards 
                                        # since we know we do not have the same amount of cards in both 
                                        if len(fullHand[0]) > len(fullHand[-1]):
                                            hands.pop(-1)
                                            return hands
                                        else:
                                            while len(hands)>1:
                                                hands.pop(0)
                                            return hands
                                    
                                elif fullHand[0][cardSpot1] > fullHand[-1][cardSpot2]:
                                    hands.pop(-1)
                                    return hands
                                elif fullHand[0][cardSpot1] < fullHand[-1][cardSpot2]:
                                    while len(hands) > 1:
                                        hands.pop(0)
                                    return hands
                            else: continue
                    else: continue
                pass
            case 'Straight': 
                # count up the cards again find where the strihgt starts and then store the top number
                # we can get away with only storing the top number since both players will need 
                # 5 cards in a row so if they have the same top they have the same five
                topnums = [0 for _ in range(len(fullHand))]
                
                for hand in range(len(fullHand)):
                    rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
                     '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                    for card in fullHand[hand]:
                        rankcount[card.getVal()]+=1
                    straightlist = []
                    straightlist.append(rankcount['Ace'])
                    for value in rankcount.values():
                        straightlist.append(value)
                    straightlist.reverse()
                    for cardSpot in range(len(straightlist)-5):
                        if all(straightlist[x]!=0 for x in range(cardSpot, cardSpot+5)): 
                            # now we just put the highest card of the straight in some other place to check later
                            topnums[hand] = cardSpot
                            break

                if topnums[0] == topnums[-1]:
                    return hands
                if topnums[0] < topnums[-1]:
                    hands.pop(-1)
                    return hands
                if topnums[0] > topnums[-1]:
                    while len(hands) > 1:
                        hands.pop(0)
                    return hands

                pass
            case 'Flush':
                # read comments for straight
                # only difference is we will use the 5 cards that make the flush not the five cards that make teh straight
                #print('case Flush solved')
                tocompare = [[]]*len(fullHand) # the list that will hold the highest flush for all hands 
                for hand in range(len(fullHand)): # this loop is finding what cards in a hand are actually the ones that make the flush
                    suitcount = {'Spades':[], 'Hearts':[], 'Clubs':[], 'Diamonds':[]}
                    for card in fullHand[hand]:
                        suitcount[card.getSuit()].append(card)
                    maybeadd = []
                    for numSuited in suitcount.values():
                        if len(numSuited)>4:
                            maybeadd.append(numSuited[0:top])
                    while len(maybeadd)>1:
                        # need to compare the flushes in a single hand 
                        for card in range(len(maybeadd[0])):
                            if maybeadd[0][card] > maybeadd[-1][card]:
                                maybeadd.pop(-1)
                            elif maybeadd[0][card] < maybeadd[-1][card]:
                                maybeadd.pop(0)
                            elif maybeadd[0][card] == maybeadd[-1][card]:
                                continue
                    tocompare[hand] = maybeadd
                # now we have tocompare filled with the flushes from each hand so we need to compare them
                for card in range(len(tocompare[0])):
                    if tocompare[0][card] == tocompare[-1][card]:
                        continue
                    elif tocompare[0][card] > tocompare[-1][card]:
                        hands.pop(-1)
                        return hands
                    elif tocompare[0][card] < tocompare[-1][card]:
                        while len(hands) > 1:
                            hands.pop(0)
                        return hands
                pass
            case 'Full House':
                #print('case Full House solved')
                # can we use the same logic for three of a kind?
                # sorta but if the three of a kinds are the same then we have to check the pairs
                # so we can just use the code for 3 of a kind and then if those are the same use the code for pairs
                # problem with just copy and pasting the pair code is that it might just look at the three of a kind since we are
                # only looking at 2 so we also need to make sure the cards next to the 2 do not equal the 2
                for cardSpot1 in range(len(fullHand[0])-2):
                    if fullHand[0][cardSpot1] == fullHand[0][cardSpot1+1] and fullHand[0][cardSpot1] == fullHand[0][cardSpot1+2]:
                        for cardSpot2 in range(len(fullHand[-1])-2):
                            if fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+1] and fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+2]:
                                if fullHand[0][cardSpot1] == fullHand[-1][cardSpot2]: 
                                    # now we compare the pairs since the three of a kind parts were the same
                                    # so now we know that the 3 of a kind on both hands are the same 
                                    # we need to check which has a better pair 
                                    # make a new list that does not contain the three of a kind part
                                    smaller1 = [item for item in fullHand[0] if item != fullHand[0][cardSpot1]]
                                    smaller2 = [item for item in fullHand[-1] if item != fullHand[-1][cardSpot2]]
                                    for secondCheck1 in range(len(smaller1)-1):
                                        if smaller1[secondCheck1] == smaller1[secondCheck1+1]:
                                            for secondCheck2 in range(len(smaller2)-1):
                                                if smaller2[secondCheck2] == smaller2[secondCheck2+1]:
                                                    # now we can actually compare
                                                    if smaller1[secondCheck1] == smaller2[secondCheck2]:
                                                        # since we are looking at a full house which is a 5 card hand the high cards 
                                                        # do not matter to the ranking of the hand so we will just move on here 
                                                        # the players would chop
                                                        return hands
                                                    elif smaller1[secondCheck1] > smaller2[secondCheck2]:
                                                        hands.pop(-1)
                                                        return hands
                                                    elif smaller1[secondCheck1] < smaller2[secondCheck2]:
                                                        while len(hands) > 1:
                                                            hands.pop(0)
                                                        return hands
                                                else: continue
                                        else: continue
                                    pass
                                elif fullHand[0][cardSpot1] > fullHand[-1][cardSpot2]:
                                    hands.pop(-1)
                                    return hands
                                elif fullHand[0][cardSpot1] < fullHand[-1][cardSpot2]:
                                    while len(hands) > 1:
                                        hands.pop(0)
                                    return hands
                            else: continue
                    else: continue
                pass
            case 'Four of a kind':
                #print('case Four of a kind solved')
                # similar to both pair and 3 of a kind we just compare to 1 more card
                for cardSpot1 in range(len(fullHand[0])-3):
                    if fullHand[0][cardSpot1] == fullHand[0][cardSpot1+1] and fullHand[0][cardSpot1] == fullHand[0][cardSpot1+2] and fullHand[0][cardSpot1] == fullHand[0][cardSpot1+3]:
                        for cardSpot2 in range(len(fullHand[-1])-3):
                            if fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+1] and fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+2] and fullHand[-1][cardSpot2] == fullHand[-1][cardSpot2+3]:
                                # now we compare the pairs 
                                if fullHand[0][cardSpot1] == fullHand[-1][cardSpot2]:
                                    # here we now need to check their highest cards against each other
                                        # i just coppied the code from high card can we make that better somehow
                                    smaller1 = [item for item in fullHand[0] if item != fullHand[0][cardSpot1]]
                                    smaller2 = [item for item in fullHand[-1] if item != fullHand[-1][cardSpot2]]
                                    if(len(smaller1)>0 and len(smaller2)>0):
                                        pass
                                    else:
                                        # we know that one of the hands has no more cards remove that hand
                                        if len(smaller1)==0:
                                            while len(hands)>1:
                                                hands.pop(0)
                                            return hands
                                        else:
                                            hands.pop(-1)
                                            return hands
                                    if smaller1[0] == smaller2[0]:
                                        #print('highest card outside of pair is the same')
                                        return hands
                                    elif smaller1[0] < smaller2[0]:
                                        while len(hands)>1:
                                            hands.pop(0)
                                        return hands
                                    elif smaller1[0] > smaller2[0]:
                                        hands.pop(-1)
                                        return hands
                                elif fullHand[0][cardSpot1] > fullHand[-1][cardSpot2]:
                                    hands.pop(-1)
                                    return hands
                                elif fullHand[0][cardSpot1] < fullHand[-1][cardSpot2]:
                                    while len(hands) > 1:
                                        hands.pop(0)
                                    return hands
                            else: continue
                    else: continue
                pass
            case 'Straight Flush':
                # similar to straigth and flush but we need to do both 
                # first we should seperate the cards in each hand by suit
                # since we are sorting everyhting at the top of the function when we then seperate things into 
                # suits we will know they are in order
                # then for each suit we can do the thing we are doing in straights to see if there is a 
                # straight and if there is we can stroe the highest index
                #print('case Straight Flush solved')
                # first find the cards that make the flushes 
                tocompare = [0 for _ in range(len(fullHand))] # the list that will hold the highest flush for all hands 
                for hand in range(len(fullHand)): # this loop is finding what cards in a hand are actually the ones that make the flush
                    suitcount = {'Spades':[], 'Hearts':[], 'Clubs':[], 'Diamonds':[]}
                    for card in fullHand[hand]:
                        suitcount[card.getSuit()].append(card)
                    maybeadd = []
                    for numSuited in suitcount.values():
                        if len(numSuited)>4:
                            maybeadd.append(numSuited[0:top])
                    # now for every list of cards that makes a flush we need to see if there is a stright in them
                    topcard = []
                    for flush in maybeadd:
                        rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
                         '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                        for card in fullHand[hand]:
                            rankcount[card.getVal()]+=1
                        straightlist = []
                        straightlist.append(rankcount['Ace'])
                        for value in rankcount.values():
                            straightlist.append(value)
                        straightlist.reverse()
                        for cardSpot in range(len(straightlist)-5):
                            if all(straightlist[x]!=0 for x in range(cardSpot, cardSpot+5)):
                                # we found a straight flush 
                                # we can actually jut save the highest card rank in the straight flush 
                                topcard.append(cardSpot)
                                break
                    if len(topcard)<1:
                        topcard.append(99999)
                    tocompare[hand] = min(topcard)
                if tocompare[0] == tocompare[-1]:
                    return hands
                elif tocompare[0] < tocompare[-1]:
                    hands.pop(-1)
                    return hands
                elif tocompare[0] > tocompare[-1]:
                    while len(hands)>1:
                        hands.pop(0)
                pass
        return hands

def handelInput(L): # just makes sure all the values in the list are actual card values
    changed = []
    for value in L:
        match value:
            case 'two': changed.append('2'); pass
            case 'three':changed.append('3'); pass
            case 'four':changed.append('4'); pass
            case 'five':changed.append('5'); pass
            case 'six':changed.append('6'); pass
            case 'seven':changed.append('7'); pass
            case 'eight':changed.append('8'); pass
            case 'nine':changed.append('9'); pass
            case 'ten':changed.append('10'); pass
            case 'jack':changed.append('Jack'); pass
            case 'queen':changed.append('Queen'); pass
            case 'king':changed.append('King'); pass
            case 'ace':changed.append('Ace'); pass
            case _: changed.append(value); pass # default case 
    return changed 

if __name__ == '__main__':
    numhands = 0
    numrounds = 0
    while True:
        # getting user input
        try:
            numboards = int(input('How many boards should be played? '))
        except:
            print("must input a number")
            continue
        try:
            numplayers = int(input('How many players should there be? '))
        except:
            print("must input a number")
            continue
        try:
            numcards = int(input('How many cards should each player get? '))
        except:
            print("must input a number")
            continue

        try:
            dead = input('Are there any dead cards? Seperate the values with spaces. ')
            if len(dead)>0:
                dead = dead.split(' ')
                dead = [item.lower() for item in dead]
                dead = handelInput(dead)
                for i in range(len(dead)):
                    if (dead[i] not in Rankings.getCrank()):
                        raise KeyError
        except:
            print("Inproper input for dead cards.")
            continue
        try:
            wild = input('Are there any wild cards? Seperate the values with spaces. ')
            if len(wild):
                wild = wild.split(' ')
                wild = [item.lower() for item in wild]
                wild = handelInput(wild)
                for i in range(len(wild)):
                    if (wild[i] not in Rankings.getCrank()):
                        raise KeyError
        except:
            print("Inproper input for wild cards.")
            continue

        if (numplayers*numcards + 8*numboards<= 52):
            break
        else:
            print('There are now enough cards in a single deck for that to work enter different numbers.')

    tothanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0}
    winninghanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                    , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0}
    percentdict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                    , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0}
    for i in range(100000):
        # simulating a round of poker
        org = Deck(wild, dead)
        org.shuffle()
        org.deal(numplayers,numcards,numboards)
        org.calcHandRanks()
        org.calcWinner()

        # keep track of all the hands that were dealt
        for hand in org.playerHands:
            for rank in hand.getRanks():
                tothanddict[rank]+=1
        numrounds +=1
        numhands += len(org.playerHands)

        for level in org.winningLevel:
            winninghanddict[level]+=1

        #print(f'Round {i}')
        #for hand in org.playerHands:
        #    print('Hand: ')
        #    print(hand)
        #print(org.winnerstr)

    for key in percentdict.keys():
        try:
            percentdict[key] = (winninghanddict[key]/tothanddict[key])*100
        except ZeroDivisionError:
            print(f"Hand type -{key}- did not occur.")

    # if we want to see some stats on the hands 
    #print(f'Total number of hands {sum(tothanddict.values())}')
    #print(f'Total number of winning hands {sum(winninghanddict.values())}')
    print(f'Total number of each type of hand\n{tothanddict}')
    print(f'Number of times each type of hand won a round\n{winninghanddict}')
    print(f'The percent of a that the hand being this rank alone is enough to win.')
    toprint = ''
    for key, value in percentdict.items():
        toprint += (f'{key}: {value:.3f} ')
    print(toprint)