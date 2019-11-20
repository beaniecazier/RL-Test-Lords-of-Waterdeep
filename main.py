import random
import sys

import building
import pandas as pd
import player
from lord import Lord
from quest import Quest
from quest import Deck

typeslist = ['Building', 'Commerce',
             'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']
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

def checkArgs():
    return

def main():
    #shuffle decks using shuffle(deckobj, times) {for times random.shuffle(deck)}
    initializeGame()
    return

def initializeGame():
    #shuffle leader deck
    random.shuffle(lords)
    print(*lords)

    questdeck = Deck()
    print(*questdeck)
    for t in typeslist:
        print(t + ':' + str(sum(q.questtype == t for q in questdeck)))
    print(*list(str(l) + ' awards ' + str(l.award(questdeck))+' points for all quests in deck\n' for l in lords))
    return

initializeGame()

if '__name__' == '__main__':
    checkArgs()
    main()
