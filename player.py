from resourcevector import RVector
import sys

numagents = [None,4,3,2,2]
names = {'yellow':'Knights of the Shield', 'grey':'City Guard', 'blue':'Silverstars', 'green':'Harpers', 'red':'Red Sashes'}

class Player:
    lord = None
    quests = []
    intriguecards = []
    buildings = []

    def __init__(self, color, totalagents):
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

    def drawIntrigue(self, num):
        return

    def drawQuest(self, num):
        return

    def buyBuilding(self, building):
        building.buy(self)
        self.buildings.append(building)
    
    def receiveResources(self, effects):
        increment = RVector(0,0,0,0,0,0,0,0,0)
        for e in effects:
            for i in range(e.choice):
                increment = self.chooseToken(increment, e.white, e.black, e.orange, e.purple)
            self.drawQuest(e.quest)
            self.drawIntrigue(e.intrigue)
            if e.choice == 0:
                increment.white += e.white
                increment.black += e.black
                increment.orange += e.orange
                increment.purple += e.purple
            increment.coin += e.coin
            increment.vp += e.vp
        self.resources += increment

    def chooseToken(self, w, b, o, p):
        return

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
        current = self.current + 1 if self.current < self.numplayers else 0