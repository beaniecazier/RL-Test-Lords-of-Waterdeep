from resourcevector import RVector
import sys
from quest import Quest

numagents = [None,4,3,2,2]
names = {'yellow':'Knights of the Shield', 'grey':'City Guard', 'blue':'Silverstars', 'green':'Harpers', 'red':'Red Sashes'}


# complete order
# add draw function to main game loop after each action to reduce player resource pool and add cards to player's lists
# move onto intrigue cards


class Player:

    def __init__(self, color, totalagents):
        self.lord = None
        self.quests = []
        self.completed = []
        self.intrigues = []
        self.buildings = []
        self.name = names[color]
        self.color = color
        self.resources = RVector(0,0,0,0,0,0,0,0,0)
        self.fp = False
        self.haslieutenant = False
        self.hasambassador = False
        self.numagents = totalagents
        self.totalagents = totalagents
        return

    def assignLord(self, lord):
        self.lord = lord

    def gainLieutenant(self):
        self.haslieutenant = True
        return

    def setAmbassador(self, value):
        self.hasambassador = value
        return

    def gainIntrigue(self, cards):
        self.intrigues.extend(cards)
        return

    def gainQuest(self, cards):
        self.quests.extend(cards)
        return

    def completeQuest(self, index):
        if self.resources < self.quests[index].cost:
            print('ERROR quest cost too high')
            return
        quest = self.quests.pop(index)
        self.resources = self.resources - quest.cost
        self.resources = self.resources + quest.reward
        #do callbacks?
        self.completed.append(quest)
        return

    def buyBuilding(self, building):
        building.buy(self)
        self.buildings.append(building)
    
    def receiveResources(self, effects):
        increment = RVector(0,0,0,0,0,0,0,0,0)
        for e in effects:
            if e.choice == 0:
                increment = increment + RVector(0,e.white,e.black,e.orange,e.purple,0,0,0,0)
            else:
                for i in range(e.choice):
                    increment = self.chooseToken(increment, e.white, e.black, e.orange, e.purple)
            increment = increment + RVector(e.coin,0,0,0,0,e.vp,e.intrigue,e.quest,0)
        self.resources = self.resources + increment

    def chooseToken(self, pool, w, b, o, p):
        return pool
    
    def chooseQuest(self, quests):
        #pick a quest
        #add quest to open quests
        #return remaining
        self.gainQuest([quests.pop()])
        return quests

    def chooseQuestType(self):
        #have current player choose a quest type
        return 'Arcana'

class Group():
    #AI models will be tied to a player color,
    # order will be randomized?
    #first is a color
    def __init__(self, numplayers, numai, colors = ['yellow','grey','blue','green','red'], pcs = []):
        if len(colors) != numplayers:
            print('ERROR player.py line 70 Group __init__ list length mismatch')
            return
        if numplayers != numai + len(pcs):
            print('ERROR player.py line 73 Group __init__ group size mismatch')
        
        self.numplayers = numplayers
        for pc in pcs:
            if pc.color not in colors:
                print('ERROR')
                return
            colors.remove(pc.color)
        self.colors = colors
        self.players = [Player(color, numagents[numplayers]) for color in self.colors]
        self.players.extend(pcs)
        self.first = 0
        self.current = self.first
    
    def getSpecific(self, color):
        return self.players[self.colors.index(color)]

    def getCurrent(self):
        return self.players[self.current]

    def goTo(self, color):
        self.current = self.colors.index(color)

    def goToFirst(self):
        self.current = self.first

    def goToLast(self):
        self.current = self.numplayers - 1
    
    def nextPlayer(self):
        self.current = self.current + 1 
        if self.current >= self.numplayers:
            self.current = 0