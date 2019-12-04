import player
import building
import sys
import random
from lord import Lord
from quest import Quest

typeslist = ['building', 'commerce',
             'skullduggery', 'warfare', 'piety', 'arcana']
#create deck of leaders
lords = [Lord([typeslist[1], typeslist[2]]),
            Lord([typeslist[1], typeslist[3]]), 
            Lord([typeslist[1], typeslist[4]]), 
            Lord([typeslist[1], typeslist[5]]), 
            Lord([typeslist[2], typeslist[3]]),
            Lord([typeslist[2], typeslist[4]]), 
            Lord([typeslist[2], typeslist[5]]), 
            Lord([typeslist[3], typeslist[4]]), 
            Lord([typeslist[3], typeslist[5]]), 
            Lord([typeslist[4], typeslist[5]]),
            Lord([typeslist[0]])]

def roll():
    return random.randint(0,5)

quests = [Quest(str(i), typeslist[random.randint(1, 5)], roll(), roll(), roll(), 
                                    roll(), roll(), roll(), roll(), roll(), roll(), 
                                    roll(), random.randint(0, 25)) for i in range(60)]

#players = []

def checkArgs():
    return

def main():
    #shuffle decks using shuffle(deckobj, times) {for times random.shuffle(deck)}
    initializeGame()
    return

def palaceOfWaterDeep(players, player):
    for p in players:
        p.setAmbassador(p == player)

def buildersHall():
    
    return
            
def initializeGame():
    players = [player.Player(None, 5, None, None) for i in range(4)]
    deck = building.Deck()
    startingbuildings = ['Cliffwatch Inn1', 'Cliffwatch Inn2', 'Cliffwatch Inn3', 'Waterdeep Harber1',
                        'Waterdeep Harber2', 'Waterdeep Harber3', 'Field of Triumph', 'Blackstaff Tower',
                        'Castle Waterdeep', 'Builder\'s Hall', 'Aurora\'s Realms Shop',
                        'The Plinth', 'The Grinning Lion Tavern']
    board = deck.grabInitialBuildings(startingbuildings)
    deck.shuffle()
    buildhall = {deck.draw():3 for i in range(4)}
    deck.buildings['The Stone House'].extraeffects[lambda board, player: len(board) - 13] = [board]
    deck.buildings['The Zoarstar'].extraeffects[lambda board, player:player.chooseBuilding(
        [b for b in board if b.occupant != player])] = [board]
    deck.buildings['The Palace of Waterdeep'].extraeffects[palaceOfWaterDeep] = [
        players]
    print(*board)
    print(*buildhall)
    print(deck)
    deck.buildings['The Stone House'].use(players[0])
    return

initializeGame()

if '__name__' == '__main__':
    checkArgs()
    main()
