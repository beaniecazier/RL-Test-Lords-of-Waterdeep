import random
import sys
import copy

import pandas as pd
from itertools import cycle

from deck import Deck
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

lords = Deck(pd.read_csv('lords.csv', index_col ='name'), 'lord', 'lord')
quests = Deck(pd.read_csv('quests.csv', index_col ='name'), 'quest', 'quest')
intrigues = Deck(pd.read_csv('intrigue.csv', index_col ='name'), 'intrigue', 'intrigue')
buildings = Deck(pd.read_csv('buildings.csv', index_col ='name'), 'building', 'building')
board = [buildings[buildings.remove(name)] for name in startingbuildings]
inn = []            # quests available in the inn
hall = []           # buildings in the builders hall
group = None        # players
GM = player.Player('gamemaster',0)

def setUpIntrigues():
    for c in intrigues.cards:
        if intrigues[c].name in ['Fend Off Bandits','Foil the Zhentarim','Placate Angry Merchants','Quell Riots','Repel Drow Invaders','Stamp Out Cultists']:
            intrigues[c].addEffects([assignMandatory])
        if intrigues[c].name == 'Call for Adventurers':
            intrigues[c].addEffects([callForAdventurers])
        if intrigues[c].name == 'Bribe Agent':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Free Drinks':
            intrigues[c].addEffects([freeDrinks])
        if intrigues[c].name == 'Accelerate Plans':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Bidding War':
            intrigues[c].addEffects([biddingWar])
        if intrigues[c].name == 'Call in a Favor':
            intrigues[c].addEffects([callInAFavor])
        if intrigues[c].name == 'Change of Plans':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Real Estate Deal':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Recall Agent':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Sample Wares':
            intrigues[c].addEffects([])
        if intrigues[c].name == 'Special Assignment':
            intrigues[c].addEffects([specialAssignment])
        if intrigues[c].name in ['Ambush','Arcane Mishap','Assassination','Lack of Faith']:
            intrigues[c].addEffects([allOpponent])
        if intrigues[c].name in ['Conscription','Crime Wave','Good Faith','Graduation Day','Spread the Wealth']:
            intrigues[c].addEffects([chooseOneOpponent])
        if intrigues[c].name in ['Recruit Spies','Request Assistance','Research Agreement','Summon the Faithful','Tax Collection']:
            intrigues[c].addEffects([allOpponentChoose])

def roll():
    return random.randint(0,5)

def checkArgs():
    #whether tokens and resources should be limited or unlimited
    return

def buildCallBacks():
    buildings['The Stone House'].extraeffects[lambda board, player: player.receiveResources(RVector(len(board) - 13,0,0,0,0,0,0,0,0))] = [board]
    buildings['The Waymoot'].extraeffects[lambda skip, player: player.receiveResources(RVector(0,0,0,0,0,0,0,1,0))] = [None]
    buildings['The Zoarstar'].extraeffects[lambda board, player:player.chooseBuilding(
        [b for b in board if b.occupant != player])] = [board]
    buildings['The Palace of Waterdeep'].extraeffects[palaceOfWaterDeep] = [group]
    buildings['Heroes\' Garden'].extraeffects[heroesGarden] = [inn]

def pickFirstPlayer():
    #determine first player
        #pick someone
        #cycle list to that person
        #has to come before money handout
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

    lords.reshuffle()
    quests.reshuffle()
    intrigues.reshuffle()
    buildings.reshuffle()
    board.clear()
    board = [buildings[buildings.remove(name)] for name in startingbuildings]
    group = player.Group(numplayers, numai, lords)
    pickFirstPlayer()
    startingGold = RVector(4,0,0,0,0,0,0,0,0)
    group.goToFirst()
    for i in range(numplayers):
        group.getCurrent().receiveResources([startingGold])
        group.getCurrent().gainQuest([quests.draw() for i in range(startingQuests)])
        group.getCurrent().gainIntrigue([intrigues.draw() for i in range(startingIntrigue)])
        startingGold.coin += 1
        group.nextPlayer()
    inn = [quests.draw() for i in range(innSize)]
    hall = {buildings.draw():RVector(0,0,0,0,0,0,0,0,0) for i in range(hallSize)}
    buildCallBacks()
    return 0

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

# initializeGame(2, 2)
# board[0].use(group.players[0])
# print(group)
# print('Buildings on the board:')
# print(board)
# print('These buildings are available in the BUILDER\'S HALL')
# print('\n'.join(str(b) for b in hall))
# resetPhase()
# print('Buildings on the board after reset:')
# print(board)
# updatePhase(5)

if '__name__' == '__main__':
    checkArgs()

    print('Welcome to Lords of Waterdeep RL Experiment')
    print('Let\'s start by selecting the total number of players that are going to play')
    numplayers = input('Please enter your selection(2-5):')
    print('Great, it seems you selected {numplayers} total players')
    numai = input('Now how many of these will be AIs?')

    main(numplayers, numai)