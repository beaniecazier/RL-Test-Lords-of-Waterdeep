import random
import sys

import pandas as pd
from itertools import cycle

import building
import player
import quest
import lord
import intrigue
from resourcevector import RVector

#Builder's hall is a list of length 4 containing tuples
#ele0: building; ele1: cost; ele2:vp; ele3; buy effects

typeslist = ['Building', 'Commerce',
             'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']
startingbuildings = ['Cliffwatch Inn1', 'Cliffwatch Inn2', 'Cliffwatch Inn3', 'Waterdeep Harber1',
                    'Waterdeep Harber2', 'Waterdeep Harber3', 'Field of Triumph', 'Blackstaff Tower',
                    'Castle Waterdeep', 'Builder\'s Hall', 'Aurora\'s Realms Shop',
                    'The Plinth', 'The Grinning Lion Tavern']
startingQuests = 2
startingIntrigue = 2
innSize = 4
hallSize = 3
vproundamount = RVector(0,0,0,0,0,1,0,0,0)
lords = None        # pile of lord cards
quests = None       # quest deck
intrigues = None    # intrigue deck
buildings = []      # building deck
board = None        # buildings in play
inn = []            # quests available in the inn
hall = []           # buildings in the builders hall
group = None        # players
GM = player.Player('black',0)

#def sendAid(quest, player, group, deck):
#def establishSafeHouse(quest, player, group, deck):
#def prisonBreak(quest, player, group, deck):
#def lootCyrpt(quest, player, group, deck):
#def researchChronomancy(quest, player, group, deck):
#def lureArtisans(quest, player, group, deck):
#def placateWalkingStatue(quest, player, group, deck):
#def recruitLieutenant(quest, player, group, deck):

def roll():
    return random.randint(0,5)

def checkArgs():
    #whether tokens and resources should be limited or unlimited
    return

def palaceOfWaterDeep(group, player):
    for p in group.players:
        p.setAmbassador(p == player)

def heroesGarden(deck, player):
    print('ERROR, Heroes\' Garden is an uncompleted building. main.py Line 53')

def buildersHall():
    # choose and buy a building from the builder's hall
    # check if player has the plot quest INFILTRATE BUILDER"S HALL completed
    return
            
def initializeGame(numplayers, numai):
    global lords
    global quests
    global intrigues
    global buildings
    global board
    global group
    global inn
    global hall

    lords = lord.Deck()
    quests = quest.Deck()
    intrigues = intrigue.Deck()
    buildings = building.Deck()
    board = buildings.grabInitialBuildings(startingbuildings)
    #shuffle decks
    lords.shuffle()
    quests.shuffle()
    intrigues.shuffle()
    buildings.shuffle()
    #make players
    group = player.Group(numplayers, numai, lords, ['yellow', 'red'])
    #determine first player
        #pick someone
        #cycle list to that person
        #has to come before money handout
    #deal quests
    for p in group.players:
        p.gainQuest([quests.draw() for i in range(startingQuests)])
    #deal intrigue
    for p in group.players:
        p.gainIntrigue([intrigues.draw() for i in range(startingIntrigue)])
    #hand out initial currency
    startingGold = RVector(4,0,0,0,0,0,0,0,0)
    group.goToFirst()
    for i in range(numplayers):
        group.getCurrent().receiveResources([startingGold])
        startingGold.coin += 1
        group.nextPlayer()
    #add quests to the inn
    inn = [quests.draw() for i in range(innSize)]
    #builders hall
    hall = {buildings.draw():RVector(0,0,0,0,0,0,0,0,0) for i in range(hallSize)}
    #finally add callbacks
    buildings.buildings['The Stone House'].extraeffects[lambda board, player: player.receiveResources(RVector(len(board) - 13,0,0,0,0,0,0,0,0))] = [board]
    buildings.buildings['The Waymoot'].extraeffects[lambda skip, player: player.receiveResources(RVector(0,0,0,0,0,0,0,1,0))] = [None]
    buildings.buildings['The Zoarstar'].extraeffects[lambda board, player:player.chooseBuilding(
        [b for b in board if b.occupant != player])] = [board]
    buildings.buildings['The Palace of Waterdeep'].extraeffects[palaceOfWaterDeep] = [group]
    buildings.buildings['Heroes\' Garden'].extraeffects[heroesGarden] = [inn]
    return

def agentsLeft():
    global group
    return (sum([p.numAgents for p in group.players]) > 0)

def updatePhase(round):
    global board
    global group
    global hall
    print('Now starting Update phase for round {}'.format(round))
    print('doing all beginning of round effects for buildings')
    for b in hall:
        hall[b] = hall[b] + vproundamount
    for b in board:
        b.updatePile()
    if round == 5:
        print('adding round 5 AGENTS to each players pool')
        group.roundFive()

def resetPhase():
    global board
    global group
    global hall
    print('Now starting Reset phase for round {}'.format(round))
    print('clearing all AGENTS from board')
    group.resetAgents()
    for b in board:
        b.clear()
    for b in hall:
        b.clear()

def ambassadorPhase():
    global buildings
    global board
    global group
    print('Now starting Ambassador phase for round {}'.format(round))
    group.goToFirst()
    for i in range(group.numplayers):
        p = group.getCurrent()
        if p.hasambassador:
            p.playAmbassador().occupant = GM
        group.nextPlayer()

def playPhase():
    global quests
    global intrigues
    global buildings
    global board
    global group
    global inn
    global hall
    group.goToFirst()
    #cycle through once all player
    #check if anyone has the plot quest DEFEND THE TOWER OF LUCK as a completed quest
    #if so then use
    print('Now starting PLay phase for round {}'.format(round))
    while agentsLeft():
        p = group.getCurrent()
        if p.numagents > 0:
            print('It is now {} player\'s turn'.format(p.color))
            choice = p.playAgent(board)
            board[choice].use(p)
            #deal with new resource
            #hand out quests and intrigue
            choice = p.chooseQuest()
            if choice >= 0:
                p.completeQuest(choice)
                #deal with new resource
                #hand out quests and intrigue
        group.nextPlayer()
        # if no buildings left then end round

def reassignPhase():
    global lords
    global quests
    global intrigues
    global buildings
    global board
    global group
    global inn
    global hall
    print('Now starting Reassign phase for round {}'.format(round))

def endGame():
    return
    
def main(numplayers, numai):
    #shuffle decks using shuffle(deckobj, times) {for times random.shuffle(deck)}
    initializeGame(numplayers, numai)
    for round in range(1,9):
        #update phase
        updatePhase(round)
        #reset phase
        resetPhase()
        #ambassador phase
        ambassadorPhase()
        #play phase
        playPhase()
        #reassign phase
        reassignPhase()
    endGame()
    return

initializeGame(2, 2)
board[0].use(group.players[0])
print(group)
print('Buildings on the board:')
print(board)
print('These buildings are available in the BUILDER\'S HALL')
print('\n'.join(str(b) for b in hall))
resetPhase()
print('Buildings on the board after reset:')
print(board)
updatePhase(5)

if '__name__' == '__main__':
    checkArgs()

    print('Welcome to Lords of Waterdeep RL Experiment')
    print('Let\'s start by selecting the total number of players that are going to play')
    numplayers = input('Please enter your selection(2-5):')
    print('Great, it seems you selected {numplayers} total players')
    numai = input('Now how many of these will be AIs?')

    main(numplayers, numai)
