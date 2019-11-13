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
    random.shuffle(quests)
    print(*quests)
    return

initializeGame()
for t in typeslist:
    print(t + ':' + str(sum(q.questtype == t for q in quests)))
print(*list(str(l) + ' awards ' + str(l.award(quests))+' points for all quests in deck\n' for l in lords))

if '__name__' == '__main__':
    checkArgs()
    main()
