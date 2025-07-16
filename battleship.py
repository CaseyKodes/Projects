# making a two player battle ship game

# each player has a grid of where they put theri boats and a grip of where the have tried to hit the other players boats
# makring misses as m and hits as h 
# if a boat is sunk we shoudl tell the player they sunk a boat
# do we want to tell them anything else?
# players input where they put their boats 
# with start and end coords 
# need to check if any of the cords of boats over lap if they do retry the current boat
# need to make sure the coords are in a stright line if not restart current boat
# need to make sure coords for start and edn are the length of the baot apart if not restart current boat

# if we make it all just one functino it will be messy
# if we have player objects who have 2 2D arrays each one refering to where their ships are and one refering 
# to where they have attacked it might be easyer

import os
validcords = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
validcordsString = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class player():
    def __init__(self):
        # init should not take params 
        # in the function is where we decide where the boats are
        self.attacks = [['-' for i in range(10)] for j in range(10)] # text here bc this is what we will show a user
        self.ships = [[0 for i in range(10)] for j in range(10)] # numbers here bc this is what we will use for logic 
        self.turn = True
        shipLens = [5, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1]
        print('Grid size is 10x10.')
        for num in shipLens:
            print('Updated grid')
            self.printMap(self.ships)
            print(f'Current ship length {num}.')
            while True:
                try:
                    startX = int(input('X start coord of the current ship. '))
                    startY = int(input('Y start coord of the current ship. '))
                    direction = int(input('What direction from the start should the ship go?\n1 - Up, 2 - Down, 3 - Right, 4 - Left. '))
                    if startX not in validcords: 
                        raise Exception('This is not a valid starting location.')
                    if startY not in validcords: 
                        raise Exception('This is not a valid starting location.')
                    if direction not in [1, 2, 3, 4]:
                        raise Exception('This is not a valid direction.')
                    match direction: # in each case we need to see if all the indexes in direction are unoccupided and are inbetween 1-10
                        case 1:
                            if (startY - num +1) not in validcords:
                                raise Exception('Boat would go off screen try again.')
                            for i in range(num):
                                #need to check if each point the boat will be on is valid 
                                #if it is valid we should store the coords if not we throw an error
                                if(self.ships[startY - i][startX]):
                                    raise Exception('Boat would go onto another boat.')
                            # if we get out here we know that all pints the boat will be on are vlaid so now we should place the baot on those points 
                            for i in range(num):
                                self.ships[startY-i][startX] = 1
                            pass
                        case 2:
                            if (startY + num -1) not in validcords:
                                raise Exception('Boat would go off screen try again.')
                            for i in range(num):
                                if(self.ships[startY + i][startX]):
                                    raise Exception('Boat would go onto another boat.')
                            for i in range(num):
                                self.ships[startY+i][startX] = 1
                            pass
                        case 3:
                            if (startX + num -1) not in validcords:
                                raise Exception('Boat would go off screen try again.')
                            for i in range(num):
                                if(self.ships[startY][startX+i]):
                                    raise Exception('Boat would go onto another boat.')
                            for i in range(num):
                                self.ships[startY][startX+i] = 1
                            pass
                        case 4:
                            if (startX - num +1) not in validcords:
                                raise Exception('Boat would go off screen try again.')
                            for i in range(num):
                                if(self.ships[startY][startX-i]):
                                    raise Exception('Boat would go onto another boat.')
                            for i in range(num):
                                self.ships[startY][startX-i] = 1
                            pass
                except Exception as e:
                    print(f'An error occured try again, {e}')
                    continue
                break

    def tryAttack(self, other, x, y):
        if self.attacks[y][x] == '-':
            if other.ships[y][x]:
                print('Target is a hit!')
                self.attacks[y][x] = 'H'
                other.ships[y][x] = 0
                return True
            else:
                print('Target is a miss.')
                self.attacks[y][x] = 'M'
                return False
        else:
            print('Target has already been attacked, pick a different location.')
            return True

    def stillAlive(self):
        toreturn = False
        for row in self.ships:
            for x in row:
                if x:
                    toreturn = True
                    break
            if toreturn:
                break
        return toreturn
    
    def printMap(self, map):
        coords = []
        if (type(map[0][0]) is int):
            coords = validcords
        else:
            coords = validcordsString
        print(f'Y/X {coords}')
        for row in range(len(map)):
            print(f'{row} - {map[row]}')

def game():
    GOON = input('Player 1\'s turn to enter boats')
    p1 = player()
    os.system('cls')
    GOON = input('Player 2\'s turn to enter boats')
    p2 = player()
    os.system('cls')
    playerArry = [p1, p2]
    p = 0
    notp = 1
    while(p1.stillAlive() and p2.stillAlive()):
        print(f'Player {p+1}\'s turn.')
        print('Your boats')
        playerArry[p].printMap(playerArry[p].ships)
        print('Your attacks.')
        playerArry[p].printMap(playerArry[p].attacks)
        try:
            attaX = int(input('X coord to attack. '))
            attaY = int(input('Y coord to attack. '))
            if attaX not in validcords: 
                raise Exception('This is not a valid target location.')
            if attaY not in validcords: 
                raise Exception('This is not a valid target location.')
        except Exception as e:
            print(f'An error occured try again, {e}')
            continue
        playerArry[p].turn = playerArry[p].tryAttack(playerArry[notp], attaX, attaY)
        if playerArry[p].turn:
            # we know we had a hit
            if playerArry[notp].stillAlive(): continue
            else: break
        else:
            hold = p
            p = notp
            notp = hold
            os.system('cls')
            print('Last attack was a miss next players turn.')
            ready = input('next player ready. ')
            os.system('cls')
    toprint = 'Game over '
    if p1.stillAlive(): toprint += 'Player 1 won.'
    if p2.stillAlive(): toprint += 'Player 2 won.'
    print(toprint)

game()