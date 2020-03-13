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
from extras import sync

#Builder's hall is a list of length 4 containing tuples
#ele0: building; ele1: cost; ele2:vp; ele3; buy effects

typeslist = ['Building', 'Commerce',
             'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']
startingbuildings = ['Cliffwatch Inn1', 'Cliffwatch Inn2', 'Cliffwatch Inn3', 'Waterdeep Harber1',
                    'Waterdeep Harber2', 'Waterdeep Harber3', 'Field of Triumph', 'Blackstaff Tower',
                    'Castle Waterdeep', 'Builder\'s Hall', 'Aurora\'s Realms Shop',
                    'The Plinth', 'The Grinning Lion Tavern']
mandatoryquests = ['Fend Off Bandits','Foil the Zhentarim','Placate Angry Merchants','Quell Riots','Repel Drow Invaders','Stamp Out Cultists']
startingQuests = 2
startingIntrigue = 2
innSize = 4
hallSize = 3
vproundamount = RVector(0,0,0,0,0,1,0,0,0)

lords = Deck(pd.read_csv('lords.csv', index_col ='name'), 'lord', 'lord')
quests = Deck(pd.read_csv('quests.csv', index_col ='name'), 'quest', 'quest')
mandatory = []
intrigues = Deck(pd.read_csv('intrigue.csv', index_col ='name'), 'intrigue', 'intrigue')
buildings = Deck(pd.read_csv('buildings.csv', index_col ='name'), 'building', 'building')
board = [buildings[buildings.remove(name)] for name in startingbuildings]
inn = []            # quests available in the inn
hall = []           # buildings in the builders hall
group = None        # players
GM = player.Player('gamemaster',0)

def roll():
    return random.randint(0,5)

def checkArgs():
    #whether tokens and resources should be limited or unlimited
    return

def camelCase(name):
    output = ''.join((''.join(c for c in w if c.isalnum())).capitalize() for w in name.split())
    return output[0].lower() + output[1:]

def buildCallBacks():
    # link extras to main objects
    # import extras
    # loop quests then intrigue then buildings
    # get function but cammel case of oject name
    # assign to object extraseffects
    extraslist = (pd.read_csv('extra.csv'))['name]'].values.tolist()
    module = __import__('extras')

    for name in quests.cards:
        if name in extraslist:
            try:
                func = getattr(module, camelCase(name))
                quests[name].addEffects(func, '')
            except AttributeError:
                print('ERROR')
    for name in intrigues.cards:
        try:
            func = getattr(module, camelCase(name))
            intrigues[name].addEffects(func, '')
        except AttributeError:
            print('ERROR')
    for name in buildings.cards:
        if name in extraslist:
            try:
                func = getattr(module, camelCase(name))
                buildings[name].addEffects(func, '')
            except AttributeError:
                print('ERROR')

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
        group.getCurrent().gainQuest([quests.draw().reveal() for i in range(startingQuests)])
        group.getCurrent().gainIntrigue([intrigues.draw().reveal() for i in range(startingIntrigue)])
        startingGold.coin += 1
        group.nextPlayer()
    inn.clear()
    inn.extend([quests.draw().reveal() for i in range(innSize)])
    hall = {buildings.draw().reveal():RVector(0,0,0,0,0,0,0,0,0) for i in range(hallSize)}
    mandatory.clear()
    mandatory.extend([quests.remove(q) for q in quests])
    sync(group, quests, intrigues, buildings, inn, hall, board, mandatory)
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

names = pd.read_csv('extra.csv')
print(*(names['name'].values.tolist()))

if '__name__' == '__main__':
    checkArgs()

    print('Welcome to Lords of Waterdeep RL Experiment')
    print('Let\'s start by selecting the total number of players that are going to play')
    numplayers = input('Please enter your selection(2-5):')
    print('Great, it seems you selected {numplayers} total players')
    numai = input('Now how many of these will be AIs?')

    main(numplayers, numai)