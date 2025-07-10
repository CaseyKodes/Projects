# Poker simulator
 
# things that are possible
    # as long as there are enough cards in the deck
        # deal hands to any number of players 
        # the hands can be any size 
        # we can deal any number of boards of 5 cards (3 flop, 1 turn, 1 river)
    # we can calculate the rank of each players hand on each board
    # break ties between players if they have the same hand rank
    # have dead and or wild cards

import random as r

class Rankings(): # basically just a place to hold these arrays which tell us the ordering of hands 
    HandValueOrder = ['High Card', 'Pair', 'Two Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House', 'Four of a kind', 'Straight Flush', 'Five of a kind']
    CardValueOrder = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def getCrank(): return Rankings.CardValueOrder
    def getHrank(): return Rankings.HandValueOrder

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
    # it contains lists of hands that players have
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
        self.dealboards(numboards)
                
    def dealboards(self, numB):
        flops = []
        turns = []
        rivers = []
        for i in range(numB):
            toaddF = []
            self.burnt.append(self.deck.pop(0))
            for card in range(3):
                toaddF.append(self.deck.pop(0))
            flops.append(toaddF)
        for i in range(numB):
            self.burnt.append(self.deck.pop(0))
            toaddT = []
            toaddT.append(self.deck.pop(0))
            turns.append(toaddT)
        for i in range(numB):
            self.burnt.append(self.deck.pop(0))
            toaddR = []
            toaddR.append(self.deck.pop(0))
            rivers.append(toaddR)
        for board in range(numB):
            b = [flops[board]+turns[board]+rivers[board]]
            self.boardList.append(b)    
        
    def calcHandRanks(self): # figure out which hand has the best hand 
        # need to look at each hand in player hands and every card on the board
        # card then we will update their hand type if they make a better hand
        # since it is possible we did multiple baords we add a rank for each board to each hand
        for hand in self.playerHands:
            board=-1
            for rank in hand.getRanks():
                board+=1 
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
                        rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, 
                                    '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                        for card in value:
                            if card.getVal() in self.dead or card.getVal() in self.wild:
                                continue
                            rankcount[card.getVal()]+=1
                        straightlist = []
                        straightlist.append(rankcount['Ace'])
                        for value in rankcount.values():
                            straightlist.append(value)
                        TruestraightLength = 5 
                        for beg in range(len(straightlist)-TruestraightLength):
                            gaps = 0
                            for i in range(TruestraightLength):
                                if not straightlist[beg+i]: gaps+=1
                            if gaps<=numwilds:
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Straight Flush'):
                                    hand.setRank('Straight Flush', board)
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Flush'):
                        hand.setRank('Flush', board)

                # filling how many instances of a card value there are 
                # this works to find natural straights and straights that are 5-the number of wilds in a hand 
                # where the wilds are then used to be the finishing cards on the outside of the straight
                # TODO it does not work for using wilds to fill gaps so I think i just make a functionality for that
                rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, 
                             '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                if len(self.boardList) > 0:
                    for b in self.boardList[board]:
                        for card in b:
                            if card.getVal() in self.dead or card.getVal() in self.wild:
                                continue
                            rankcount[card.getVal()] += 1
                for card in hand.getCards():
                    if card.getVal() in self.dead or card.getVal() in self.wild:
                        continue
                    rankcount[card.getVal()]+=1
                # find straights
                straightlist = []
                straightlist.append(rankcount['Ace'])
                for value in rankcount.values():
                    straightlist.append(value)

                # this works by taking sections of 5 out of the array of numbers
                # if there are 0s in that gaps in increased 
                # we then check to see if the number of gaps is less than or equal to the number of wilds
                # if it is we know we can fill all the gaps with wilds so we have a straight
                TruestraightLength = 5 
                for beg in range(len(straightlist)-TruestraightLength):
                    if self.hr.index(hand.getRank(board))>self.hr.index('Straight'): break
                    gaps = 0
                    for i in range(TruestraightLength):
                        if not straightlist[beg+i]: gaps+=1
                    if gaps<=numwilds:
                        if self.hr.index(hand.getRank(board)) < self.hr.index('Straight'):
                            hand.setRank('Straight', board)

                # determining based off the number of instances of that card value what type of hand a player has
                # this is for pairs two pairs three of a kind full house and four of a kind
                if any(x>=5-numwilds for x in rankcount.values()):
                    # this is the 5 of a kind case 
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Five of a kind'):
                        hand.setRank('Five of a kind', board)
                        continue
                elif any(x==4-numwilds for x in rankcount.values()):
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Four of a kind'):
                        hand.setRank('Four of a kind', board)
                        continue
                elif any(x==3-numwilds for x in rankcount.values()):
                    for key in rankcount.keys():
                        if rankcount[key] == 3-numwilds:
                            smaller = {key: value for key, value in rankcount.items()}
                            smaller.pop(key)
                            if any(y==2 for y in smaller.values()):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Full House'):
                                    hand.setRank('Full House', board)
                                    continue
                            if self.hr.index(hand.getRank(board)) < self.hr.index('Three of a kind'):
                                hand.setRank('Three of a kind', board)
                                continue
                elif any(x==2-numwilds for x in rankcount.values()):
                    for key in rankcount.keys():
                        if rankcount[key] == 2:
                            smaller = {key: value for key, value in rankcount.items()}
                            smaller.pop(key)
                            if any(y==2 for y in smaller.values()):
                                if self.hr.index(hand.getRank(board)) < self.hr.index('Two Pair'):
                                    hand.setRank('Two Pair', board)
                                    continue
                                break 
                    if self.hr.index(hand.getRank(board)) < self.hr.index('Pair'):
                        hand.setRank('Pair', board) 
            
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
            toreturn += f'Winning hand had rank of {winnerslevel} '
            if len(self.boardList)>0:
                toreturn += f'on Board number {boardIndex+1}, with board of: \n'
                if len(self.boardList)>0:
                    for b in self.boardList[boardIndex]:
                        for card in b:
                            toreturn += card.getStr()
                            if card != b[-1]: toreturn +='& '
            toreturn += '\nWith a hand of: \n'
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
                        if card.getVal() in self.wild:
                            wild+=1
                            continue
                        new.append(card)
            for card in hands[hand].getCards():
                if card.getVal() in self.dead:
                    continue
                if card.getVal() in self.wild:
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
        # only doing for pair type hands since for the ther types we only need 1 of a card value
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
                spot1 = counts1.index(2)
                spot2 = counts2.index(2)
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
                    # if we got here we know the hands are only 4 cards long so we need to check the lengths of the hands now
                    if len(counts1)>len(counts2):
                        hands.pop(-1)
                        return hands
                    elif len(counts1)<len(counts2):
                        while len(hands)>1:
                            hands.pop(0)
                        return hands
                    else:
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
                spot1 = counts1.index(2)
                spot2 = counts2.index(2)
                if spot1==spot2:
                    counts1.pop(spot1)
                    counts2.pop(spot2)
                    pairspot1 = counts1.index(2)
                    pairspot2 = counts2.index(2)
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
                        # if we got here we know the hands are only 4 cards long so we need to check the lengths of the hands now
                        if len(counts1)>len(counts2):
                            hands.pop(-1)
                            return hands
                        elif len(counts1)<len(counts2):
                            while len(hands)>1:
                                hands.pop(0)
                            return hands
                        else:
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
                spot1 = counts1.index(3)
                spot2 = counts2.index(3)
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
                    # if we got here we know the hands are only 4 cards long so we need to check the lengths of the hands now
                    if len(counts1)>len(counts2):
                        hands.pop(-1)
                        return hands
                    elif len(counts1)<len(counts2):
                        while len(hands)>1:
                            hands.pop(0)
                        return hands
                    else:
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
                topnums = [-1,-1] # start at -1 so if we need to test it will be easier to see when it is not overridden  
                uses = [counts1, counts2]
                wuse = [0,-1]

                # updated logic now works to break ties 
                # straights can use wilds in the middle or on the outsides or not at all and it still works
                for hand in range(2):
                    straightlist = [num for num in uses[hand]]
                    straightlist.append(straightlist[0])
                    for cardSpot in range(len(straightlist)-5):
                        gaps = 0
                        for i in range(5):
                            if straightlist[cardSpot+i]==0:gaps+=1
                        if gaps<=wilds[wuse[hand]]: 
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
                spot1 = counts1.index(3)
                spot2 = counts2.index(3)
                if spot1==spot2:
                    counts1.pop(spot1)
                    counts2.pop(spot2)
                    pairspot1 = counts1.index(2)
                    pairspot2 = counts2.index(2)
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
                spot1 = counts1.index(4)
                spot2 = counts2.index(4)
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
                                        # if the high card matches we can return right away 
                                        return hands
                                    elif highspot1>highspot2:
                                        while len(hands)>1:
                                            hands.pop(0)
                                        return hands
                                    elif highspot1<highspot2:
                                        hands.pop(-1)
                                        return hands
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
                        if len(numSuited)>4-wilds[hand]:
                            maybeadd.append(numSuited)
                    # now for every list of cards that makes a flush we need to see if there is a stright in them
                    topcard = []
                    for flush in maybeadd:
                        rankcount = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
                         '8':0, '9':0, '10':0, 'Jack':0, 'Queen':0, 'King':0, 'Ace':0}
                        for card in flush:
                            rankcount[card.getVal()]+=1
                        straightlist = []
                        straightlist.append(rankcount['Ace'])
                        for value in rankcount.values():
                            straightlist.append(value)
                        straightlist.reverse()
                        for cardSpot in range(len(straightlist)-4):
                            gaps = 0
                            for i in range(5):
                                if straightlist[cardSpot+i]==0:gaps+=1
                            if gaps<=wilds[hand]: 
                                topcard.append(cardSpot)
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
                            if counts2[spot2] >= 5:
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
            
    print(f'Total number of each type of hand\n{tot}')
    print(f'Number of times each type of hand won a round\n{win}')
    print(f'The percent of a time that the hand being this rank alone is enough to win.')
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

    tothanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0, 'Five of a kind':0}
    winninghanddict = {'High Card':0, 'Pair':0, 'Two Pair':0, 'Three of a kind':0, 'Straight':0
                    , 'Flush':0, 'Full House':0, 'Four of a kind':0, 'Straight Flush':0, 'Five of a kind':0}
    
    con = 'yes'
    round = 0
    changeDets = 'y'
    while con != 'n':
        if changeDets == 'y':
            while True:
                # getting user input
                '''try: 
                    numdecks = int(input("How many decks are we playing with? "))
                except:
                    print("Must input a number.")
                    continue'''
                try:
                    numboards = int(input('How many boards should be played? \n(8 Cards per board) '))
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
                if (numplayers*numcards + 8*numboards<= 52*numdecks):
                    break
                else:
                    print(f'There are not enough cards in {numdecks} deck(s) for that to work enter different numbers.')

            while True:
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
                break

            while True:
                try:
                    handsAtaTime = int(input('How many hands should be dealt at a time? '))
                except:
                    print("Must input a number.")
                    continue
                try: 
                    printStyle = input('How should the hand be shown? As a simulation or no print? ')
                    printStyle = printStyle.lower()
                    if printStyle[0] != 's' and printStyle[0] != 'n':
                        raise KeyError
                except:
                    print('Enter S for simulation or N for no print.')
                    continue
                break
        
        print()
        # simulating a round of poker
        for handnum in range(handsAtaTime):
            round+=1
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

            if printStyle[0] == 's':
                print(f'Round {round}')
                simPrint(org)

        changeDets = input('Do you want to change the format of the hands? Y/N ')
        changeDets = changeDets.lower()
        con = input('Do you want to continue? Y/N ')
        con = con.lower()

    printStats(tothanddict, winninghanddict)

game()