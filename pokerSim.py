# trying to make a poker simulator 
 
# currently we can 
    # deal hands to any number of players so long as we have enough cards
    # the hands can be any size as long as we have enough cards 
    # we can deal any number of boards of 5 cards
    # we can calculate the rank of each players hand on each board
    # break ties between players if they have te same hand rank
    # have dead cards

# working on 
    # i believe wild cards work for pair type hands now
    # think flushes work now
    
    # straights can be identified if the player has 1-2 wilds and 4 or 3 cards in a row but for gapers it does not work yet
    # and ties are not broken properly yet for straights with wilds completing them

# currently we can NOT
'''

WILD CARD TROUBLES 
if we use a new number to indicate how many wild cards a hand has but we still count the rank of those wild cards if we ever have 2 wild cards of the same rank the progrma will 
always think we have 4 of a kind since it is counting the rank of the wild cards and saying we need the number of wild cards less in a specific rank to have that type of hand 
then if we do not count the rank fewer straights will show up since we are removing an entire card rank from the ranks that can appear

THINGS THAT ARE NICE TO KNOW ABOUT WILD CARDS 
with wild cards if a hand has 1 they will never have 2 pair as their hand type becuase they could make a better hand by using thw wild cards in a different fashion


HOW i THOUGHT TO DO IT BUT DID NOT WORK YET AND SO I REMOVED IT
do not count the rank of wild cads just add to the numer of wild cards variable
when figuring out what hand type a card has 
    if a pair hand type - subtract the number of wild cards from the number of cards needed to make the hand 
    for straights - they can be the top or bottm of a straight easy but subtracting the number of wild cards needed for a straight 
                  - but to be the middle cards in a straight is weird
    for flushes - subtract number of wild cards from how many cards are needed to make a straigth
    for straight flushes - same logic as for a straight but just seperate into the suits first
'''


import random as r

class Rankings(): # basically just a place to hold these arrays which tell us the ordering of hands 
    HandValueOrder = ['High Card', 'Pair', 'Two Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House', 'Four of a kind', 'Straight Flush', 'Five of a kind']
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
    # rank is a list to accomodate having multiple baords 
    # we can add and remove cards from a hand, clear a hand, get and set the rank of a hand
    def __init__(self, cards, numboards):
        self.cards = list()
        self.rank = ['High Card']*max(numboards, 1) # default lowest value of a hand
        for card in cards:
            self.cards.append(card)
        self.cards.sort()
    def getCards(self):
        return self.cards
    def addCard(self, card):
        self.cards.append(card)
        self.cards.sort()
    def removeCard(self, index):
        try:
            self.cards.pop(index)
        except:
            print('There is no card at that index.')
    def clearHand(self):
        self.cards.clear()

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
            if card!=self.cards[-1]: toreturn+='& '
        return toreturn
    
class Deck():
    # deck objects contain 52 cards, 4 suits, and 13 values
    # it contains lists of hands that players has
    # it keeps track of the current deck after being dealt and we can save what 
    # cards are burnt but there is no use for those yet
    # we have funcitons to deal hands to players, deal a board of shared cards, 
    # shuffle the deck ( in two different ways ), and calculate the rank of each hand

    def __init__(self, wild=[], dead=[], numdecks=1): # creates a deck of 52 cards, 13 ranks and 4 suits
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
        for deck in range(numdecks):
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
            # dealing more than 2 boards deals them in a different way than dealing 1 or 2 boards
            # but it would be annoying to write a function that would deal any number of boards the same way
            # lot of work for minimaul results probably will not do
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
        # card then we will update their hand type if they make a better hand
        # since it is possible we did multiple baords we add a rank for each board to each hand
        for hand in self.playerHands:
            board=0
            for rank in hand.getRanks():
                # finding flushes 
                numwilds = 0
                suitcount = {'Spades':[], 'Hearts':[], 'Clubs':[], 'Diamonds':[]}
                for card in hand.getCards():
                    if card.getVal() in self.dead:
                        continue
                    if card.getVal() in self.wild:
                        numwilds+=1
                        continue
                    suitcount[card.getSuit()].append(card)
                if len(self.boardList) > 0:
                    for b in self.boardList[board]:
                        for card in b:
                            if card.getVal() in self.dead:
                                continue
                            if card.getVal() in self.wild:
                                numwilds+=1
                                continue
                            suitcount[card.getSuit()].append(card)
                if any(len(x) > 4-numwilds for x in suitcount.values()):
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
                        straightLenghth = 5 # length of straight
                        for starter in range(len(straightlist)-straightLenghth):
                            if all(straightlist[starter:starter+straightLenghth-numwilds]):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Straight Flush'):
                                    hand.setRank('Straight Flush', board)
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Flush'):
                        hand.setRank('Flush', board)

                # filling how many instances of a card value there are 
                # before wilds 
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
                    if all(straightlist[starter:starter+straightLenghth-numwilds]):
                        if self.hr.index(hand.getRank(board)) < self.hr.index('Straight'):
                            hand.setRank('Straight', board)

                # after wilds 
                # this is so wilds are not counted ontop of themselves
                if numwilds>0:
                    for key in rankcount.keys():
                        if key in self.wild:
                            rankcount[key] = 0

                # determining based off the number of instances of that card value what type of hand a player has
                # this is for pairs two pairs three of a kind full house and four of a kind
                if any(x>=5-numwilds for x in rankcount.values()):
                    # this is the 5 of a kind case 
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Five of a kind'):
                        hand.setRank('Five of a kind', board)
                elif any(x==4-numwilds for x in rankcount.values()):
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Four of a kind'):
                        hand.setRank('Four of a kind', board)
                elif any(x==3-numwilds for x in rankcount.values()):
                    for key in rankcount.keys():
                        if rankcount[key] == 3-numwilds:
                            smaller = {key: value for key, value in rankcount.items()}
                            smaller.pop(key)
                            if any(y==2 for y in smaller.values()):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Full House'):
                                    hand.setRank('Full House', board)
                            if self.hr.index(hand.getRank(board)) < self.hr.index('Three of a kind'):
                                hand.setRank('Three of a kind', board)
                elif any(x==2-numwilds for x in rankcount.values()):
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
                        if card != b[-1]: toreturn +='& '
            toreturn += '\nAnd a hand of: \n'
            for hand in winnershand:
                for card in hand.getCards():
                    toreturn += card.getStr()
                    if card != hand.getCards()[-1]:
                        toreturn += '& '
                if len(winnershand) > 1 and not hand == winnershand[-1]:
                    toreturn += '\nand '
            toreturn += '\n'
            self.winningLevel.append(winnerslevel)
        self.winnerstr=toreturn
        
    def tiebreak(self, hands, level, boardIndex):
        # make a list that has all hands with all cards in a hand including board and hole cards
        fullHand = [[]]*len(hands)
        wilds = [[]]*len(hands)
        for hand in range(len(hands)):
            new = []
            wild = 0
            if len(self.boardList)>0:
                for b in self.boardList[boardIndex]:
                    for card in b:
                        if card.getVal() in self.dead:
                            continue
                        if card.getVal() in self.wild and (level!='Straight' and level!='Straight Flush'):
                            wild+=1
                            continue
                        new.append(card)
            for card in hands[hand].getCards():
                if card.getVal() in self.dead:
                    continue
                if card.getVal() in self.wild and (level!='Straight' and level!='Straight Flush'):
                    wild+=1
                    continue
                new.append(card)
            fullHand[hand] = new
            wilds[hand] = wild

        #getting the exact number of each rank card in the first and last hand
        # this is the most helpful for hands that need 5 cards it does not do much use otherwise but still worth keeping
        ranknums = [{'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0},
                    {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}]
        for card in fullHand[0]:
            ranknums[0][card.getVal()]+=1
        for card in fullHand[-1]:
            ranknums[-1][card.getVal()]+=1 
        counts1 = [value for value in ranknums[0].values()]
        counts2 = [value for value in ranknums[-1].values()] 
        counts1.reverse()
        counts2.reverse()

        # this uses the wilds in a hand to make that hand better for pairs
        # it is repeat code I want to make it better not sure how
        if level != 'Straight' and level != 'Flush' and level != 'Straight Flush':
            maximum = 0
            maxIndex = 0
            for index in range(len(counts1)):
                if counts1[index]+wilds[0] > maximum:
                    maximum = counts1[index]+wilds[0]
                    maxIndex = index
            counts1[maxIndex] = maximum
            maximum = 0
            maxIndex = 0
            for index in range(len(counts2)):
                if counts2[index]+wilds[-1] > maximum:
                    maximum = counts2[index]+wilds[-1]
                    maxIndex = index
            counts2[maxIndex] = maximum

        # sort that each list of cards in each hand so we can compare the lists easily
        for hand in fullHand:
            hand.sort(reverse=True)
        
        # seting how many cards make up a full hand if we have over 5+ cards we only 
        # look at 5 but if we have less than 5 we look at all of them
        if len(fullHand[0])>4 and len(fullHand[-1])>4:
            top = 5
        else:
            top = min(len(fullHand[0]), len(fullHand[-1])) 
            # we set the top to the minimum amount of cards then we know that if we check the min amount of cards in both we can say the one that has more cards wins
        
        # one case for each hand type
        match level:
            case 'High Card':
                #print('case High Card solved') 
                ties = 0
                for highspot1 in range(len(counts1)):
                    if counts1[highspot1]!=0:
                        for highspot2 in range(len(counts2)):
                            if counts2[highspot2]!=0:
                                if highspot1==highspot2:
                                    # come back to this case since we need to keep track 
                                    # that we have looked at another high card
                                    ties+=1
                                    if ties==5:
                                        return hands
                                    continue
                                elif highspot1>highspot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                elif highspot1<highspot2:
                                    hands.pop(-1)
                                    return hands
                pass
            case 'Pair':
                #print('case Pair solved')
                # need to find the cards that the players have pairs of and compare those first
                    # this works if one player wins directly from the pair they have
                    # but if players have the same pair we then need to check their highest cards that are not paired
                    # also need to keep in mind that we only want to check 5 cards max
                # what would this look like with the logic from full house
                # we now need to keep track of how many cards we check we only want to chec k5 cards max so we need to keep track
                # of how many high cards we look at after the pair
                ties = 0 # number that stops us from checking more than 5 cards 
                for spot1 in range(len(counts1)):
                    if counts1[spot1] == 2:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 2:
                                if spot1==spot2:
                                    # now we look for the highest card 
                                    counts1.pop(spot1)
                                    counts2.pop(spot2)
                                    for highspot1 in range(len(counts1)):
                                        if counts1[highspot1]!=0:
                                            for highspot2 in range(len(counts2)):
                                                if counts2[highspot2]!=0:
                                                    if highspot1==highspot2:
                                                        # come back to this case since we need to keep track 
                                                        # that we have looked at another high card
                                                        ties+=1
                                                        if ties==3:
                                                            return hands
                                                        continue
                                                    elif highspot1>highspot2:
                                                        while len(hands)>1:
                                                            hands.pop(0)
                                                        return hands
                                                    elif highspot1<highspot2:
                                                        hands.pop(-1)
                                                        return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
                pass
            case 'Two Pair':
                #print('case Two Pair solved')
                # can use similar logic here as for the full house case
                for spot1 in range(len(counts1)):
                    if counts1[spot1] == 2:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 2:
                                if spot1==spot2:
                                    counts1.pop(spot1)
                                    counts2.pop(spot2)
                                    for pairspot1 in range(len(counts1)):
                                        if counts1[pairspot1]==2:
                                            for pairspot2 in range(len(counts2)):
                                                if counts2[pairspot2]==2:
                                                    if pairspot1 == pairspot2:
                                                        # need more since we need to look at the high card 
                                                        counts1.pop(pairspot1)
                                                        counts2.pop(pairspot2)
                                                        for high1 in range(len(counts1)):
                                                            if counts1[high1]!=0:
                                                                for high2 in range(len(counts2)):
                                                                    if counts2[high2]!=0:
                                                                        if high1==high2:
                                                                            return hands
                                                                        elif high1>high2:
                                                                            while len(hands)>1:
                                                                                hands.pop(0)
                                                                            return hands
                                                                        elif high1<high2:
                                                                            hands.pop(-1)
                                                                            return hands
                                                    elif pairspot1>pairspot2:
                                                        while len(hands)>1:
                                                            hands.pop(0)
                                                        return hands
                                                    elif pairspot1<pairspot2:
                                                        hands.pop(-1)
                                                        return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
                pass
            case 'Three of a kind':
                #print('case Three of a kind solved')
                # could be similary to pair except now we look at three at a time
                ties = 0 # number that stops us from checking more than 5 cards 
                for spot1 in range(len(counts1)):
                    if counts1[spot1] == 3:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 3:
                                if spot1==spot2:
                                    # now we look for the highest card 
                                    counts1.pop(spot1)
                                    counts2.pop(spot2)
                                    for highspot1 in range(len(counts1)):
                                        if counts1[highspot1]!=0:
                                            for highspot2 in range(len(counts2)):
                                                if counts2[highspot2]!=0:
                                                    if highspot1==highspot2:
                                                        # come back to this case since we need to keep track 
                                                        # that we have looked at another high card
                                                        ties+=1
                                                        if ties==2:
                                                            return hands
                                                        continue
                                                    elif highspot1>highspot2:
                                                        while len(hands)>1:
                                                            hands.pop(0)
                                                        return hands
                                                    elif highspot1<highspot2:
                                                        hands.pop(-1)
                                                        return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
                pass
            case 'Straight': 
                # count up the cards again find where the strihgt starts and then store the top number
                # we can get away with only storing the top number since both players will need 
                # 5 cards in a row so if they have the same top they have the same five
                # even though we could be compairing more than 2 hands we know that they first 2 hands will have exact
                # same ranking since they would have needed to tie to get back into here with more than 2 hands so we 
                # only need to look at the first and last hands to accuratly judge them all 
                topnums = [0,0]  
                uses = [counts1, counts2]
                for hand in range(2):
                    straightlist = [num for num in uses[hand]]
                    straightlist.append(straightlist[0])
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
                    for number in range(wilds[hand]):
                        for key in suitcount.keys():
                            suitcount[key].append(Card('Ace', key))
                            suitcount[key].sort(reverse=True)
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
                # find the highest 3 of a kind for each hand and compare them 
                # if equal value compare highest paired card 
                for spot1 in range(len(counts1)):
                    if counts1[spot1] == 3:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 3:
                                if spot1==spot2:
                                    counts1.pop(spot1)
                                    counts2.pop(spot2)
                                    for pairspot1 in range(len(counts1)):
                                        if counts1[pairspot1]>=2:
                                            for pairspot2 in range(len(counts2)):
                                                if counts2[pairspot2]>=2:
                                                    if pairspot1 == pairspot2:
                                                        return hands
                                                    elif pairspot1>pairspot2:
                                                        while len(hands)>1:
                                                            hands.pop(0)
                                                        return hands
                                                    elif pairspot1<pairspot2:
                                                        hands.pop(-1)
                                                        return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
                pass
            case 'Four of a kind':
                #print('case Four of a kind solved')
                # similar to both pair and 3 of a kind we just compare to 1 more card
                for spot1 in range(len(counts1)):
                    if counts1[spot1] == 4:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 4:
                                if spot1==spot2:
                                    # now we look for the highest card 
                                    counts1.pop(spot1)
                                    counts2.pop(spot2)
                                    for highspot1 in range(len(counts1)):
                                        if counts1[highspot1]!=0:
                                            for highspot2 in range(len(counts2)):
                                                if counts2[highspot2]!=0:
                                                    if highspot1==highspot2:
                                                        # for 4 of a kind only 1 card matters so 
                                                        # if the high card matches we can return rieght away 
                                                        return hands
                                                    elif highspot1>highspot2:
                                                        while len(hands)>1:
                                                            hands.pop(0)
                                                        return hands
                                                    elif highspot1<highspot2:
                                                        hands.pop(-1)
                                                        return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
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
                        topcard.append(999999)
                    tocompare[hand] = min(topcard)
                if tocompare[0] == tocompare[-1]:
                    return hands
                elif tocompare[0] < tocompare[-1]:
                    hands.pop(-1)
                    return hands
                elif tocompare[0] > tocompare[-1]:
                    while len(hands)>1:
                        hands.pop(0)
                    return hands
                pass
            case 'Five of a kind':
                #print('case Five of a kind') 
                for spot1 in range(len(counts1)):
                    if counts1[spot1] >= 5:
                        for spot2 in range(len(counts2)):
                            if counts2[spot2] == 5:
                                if spot1==spot2:
                                    return hands
                                elif spot1>spot2:
                                    while len(hands)>1:
                                        hands.pop(0)
                                    return hands
                                elif spot1<spot2:
                                    hands.pop(-1)
                                    return hands
                pass
                
        return hands

def handelInput(L:list): # just makes sure all the values in the list are actual card values
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

def simPrint(deck:Deck): # printing the results as if we are just simulating the hand
    for hand in deck.playerHands:
        print(f'{hand}- Ranks are {hand.getRanks()}')
    print(deck.winnerstr)

def printStats(tot:dict, win:dict):
    percentdict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                    , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0, 'Five of a kind':0}
    print('\nStats of all hands played.')
    for key in percentdict.keys():
        try:
            percentdict[key] = (win[key]/tot[key])*100
        except ZeroDivisionError:
            print(f"Hand type -{key}- did not occur.")

    # if we want to see some stats on the hands 
    #print(f'Total number of hands {sum(tot.values())}')
    #print(f'Total number of winning hands {sum(win.values())}')
    print(f'Total number of each type of hand\n{tot}')
    print(f'Number of times each type of hand won a round\n{win}')
    print(f'The percent of a that the hand being this rank alone is enough to win. (Tie breakers not needed)')
    toprint = ''
    for key, value in percentdict.items():
        toprint += (f'{key}: {value:.3f} ')
    print(toprint)

def game():
    numhands = 0
    numrounds = 0

    # default values
    numdecks = 1
    numboards = 1
    numplayers = 6
    numcards = 2
    handsAtaTime = 1
    printStyle = 's'
    while True:
        # getting user input
        try: 
            numdecks = int(input("How many decks are we playing with? "))
        except:
            print("Must input a number.")
            continue
        try:
            numboards = int(input('How many boards should be played? '))
        except:
            print("Must input a number.")
            continue
        try:
            numplayers = int(input('How many players should there be? '))
        except:
            print("Must input a number.")
            continue
        try:
            numcards = int(input('How many cards should each player get? '))
        except:
            print("Must input a number.")
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
        try:
            handsAtaTime = int(input('How many hands should be dealt at a time? '))
        except:
            print("Must input a number.")
            continue
        try: 
            printStyle = input('How should the hand be shown? As a simulation or no print? ')
            printStyle = printStyle.lower()
            if printStyle != 's' and printStyle != 'n':
                raise KeyError
        except:
            print('Enter S for simulation or P for play or N for no print.')
        if (numplayers*numcards + 8*numboards<= 52*numdecks):
            break
        else:
            print(f'There are not enough cards in {numdecks} deck for that to work enter different numbers.')

    tothanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0, 'Five of a kind':0}
    winninghanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                    , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0, 'Five of a kind':0}
    
    con = 'yes'
    i = 0
    while con != 'n':
        i+=1
        # simulating a round of poker
        for handnum in range(handsAtaTime):
            org = Deck(wild, dead, numdecks)
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

            if printStyle == 's':
                print(f'Round {i}')
                simPrint(org)
            elif printStyle == 'n':
                pass

        con = input('Do you want to continue? Y/N ')
        con = con.lower()

    printStats(tothanddict, winninghanddict)
    

game()
