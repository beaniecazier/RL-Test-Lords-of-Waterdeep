from resourcevector import RVector
import sys

class Player:
    def __init__(self, lord, totalagents, hand, quests):
        self.resources = RVector(0,0,0,0,0,0,0,0,0)
        self.fp = False
        self.haslieutenant = False
        self.hasambassador = False
        self.lord = lord
        self.numagents = totalagents
        self.buildings = []
        self.quests = quests
        self.intriguecards = hand
        self.totalagents = totalagents
        return

    def incrementWhite(self, amount):
        self.white += amount
        return

    def incrementBlack(self, amount):
        self.black += amount
        return

    def incrementOrange(self, amount):
        self.coin += amount
        return

    def incrementPurple(self, amount):
        self.coin += amount
        return

    def incrementCoin(self, amount):
        self.coin += amount
        return

    def incrementVP(self, amount):
        self.score += amount
        return

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