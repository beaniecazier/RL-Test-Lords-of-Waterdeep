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
    def __init__(self, numplayers, numai, colors = ['yellow','grey','blue','green','red']):
        self.names = colors
        self.players = {}
        for i in numplayers:
            self.players[colors[i]] = Player(None, numagents[numplayers], None, None)
        self.first = colors[0]