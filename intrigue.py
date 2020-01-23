import pandas as pd
from resourcevector import RVector
import quest
import player
import copy

def assignMandatory(player, group, deck, card):
    #get opponent choice
    opponent = group.players[0]
    quest = deck.mandatory.pop(quests.mandatory.index(quests.find(card.name)))
    opponent.gainQuest([quest])

def allOpponent(player, group, deck, card):
    ovec = copy.deepcopy(card.vector)
    ovec.coin = 0
    ovec.vp = 0
    ovec.intrigue = 0
    ovec.quest = 0
    ovec.choice = 0
    if card.vector.choice != 0:
        card.vector.white = 0
        card.vector.black = 0
        card.vector.orange = 0
        card.vector.purple = 0
        card.vector.choice = 0
    for p in group.players:
        if p != player:
            if p.resources < ovec:
                player.receiveResources([card.vector])
            else:
                p.receiveResources([ovec*-1])

def chooseOneOpponent(player, group, deck, card):
    #choose opponent
    opponent = group.players[1]
    player.receiveResources([card.vector])
    opponent.receiveResources([card.vector*(1/2)])

def allOpponentChoose(player, group, deck, card):
    ovpvec = RVector(0,0,0,0,0,card.vector.vp,0,0,0)
    card.vector.vp = 0
    ovec = copy.deepcopy(card.vector)
    if ovec.black > 0 or ovec.orange > 0:
        ovec = ovec * (1/2)
    player.receiveResources([card.vector])
    #offer choice
    for p in group.players:
        if p != player:
            player.receiveResources([ovec])
            p.receiveResources([ovec*-1,ovpvec])

def biddingWar(player, group, deck, card):
    quests = [deck.draw(), deck.draw()]
    if group.numplayers > 2:
        for i in range(group.numplayers-2):
            quests.append(deck.draw())
    #group.goToCurrent()
    for i in range(group.numplayers):
        group.getCurrent().chooseQuest(quests)
        group.nextPlayer()

""" def specialAssignment(player, group, deck, card):

def callInAFavor(player, group, deck, card):

def callForAdventurers(player, group, deck, card):

def bribeAgent(player, group, deck, card):

def freeDrinks(player, group, deck, card):

def acceleratePlans(player, group, deck, card):

def changeOfPlans(player, group, deck, card):

def realEstateDeal(player, group, deck, card):

def recallAgent(player, group, deck, card):

def sampleWares(player, group, deck, card): """

class Intrigue:
    def __init__(self, name, vector):
        self.name = name
        self.vector = vector
        self.effects = []
        return

    def addEffects(self, effects):
        self.effects.extend(effects)
    
    def doEffect(self, player, players, deck):
        for e in self.effects:
            e(player, players, deck, self)

    def __repr__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])

    def __str__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])

class Deck:
    def __init__(self):
        df = pd.read_csv('intrigue.csv')
        names = df['name'].tolist()
        cs = df['coin'].tolist()
        ws = df['white'].tolist()
        bs = df['black'].tolist()
        ons = df['orange'].tolist()
        ps = df['purple'].tolist()
        vps = df['vp'].tolist()
        intrigues = df['intrigue'].tolist()
        qs = df['quest'].tolist()
        choices = df['choice'].tolist()
        self.cards = [Intrigue(names[i],RVector(cs[i], ws[i], bs[i], ons[i], ps[i], vps[i], intrigues[i], qs[i], choices[i])) for i in range(len(names))]
        for c in self.cards:
            if c.name in ['Fend Off Bandits','Foil the Zhentarim','Placate Angry Merchants','Quell Riots','Repel Drow Invaders','Stamp Out Cultists']:
                c.addEffects([assignMandatory])
            if c.name == 'Call for Adventurers':
                c.addEffects([])
            if c.name == 'Bribe Agent':
                c.addEffects([])
            if c.name == 'Free Drinks':
                c.addEffects([])
            if c.name == 'Accelerate Plans':
                c.addEffects([])
            if c.name == 'Bidding War':
                c.addEffects([biddingWar])
            if c.name == 'Call in a Favor':
                c.addEffects([])
            if c.name == 'Change of Plans':
                c.addEffects([])
            if c.name == 'Real Estate Deal':
                c.addEffects([])
            if c.name == 'Recall Agent':
                c.addEffects([])
            if c.name == 'Sample Wares':
                c.addEffects([])
            if c.name == 'Special Assignment':
                c.addEffects([])
            if c.name in ['Ambush','Arcane Mishap','Assassination','Lack of Faith']:
                c.addEffects([allOpponent])
            if c.name in ['Conscription','Crime Wave','Good Faith','Graduation Day','Spread the Wealth']:
                c.addEffects([chooseOneOpponent])
            if c.name in ['Recruit Spies','Request Assistance','Research Agreement','Summon the Faithful','Tax Collection']:
                c.addEffects([allOpponentChoose])

deck = Deck()
quests = quest.Deck()
quests.shuffle()
group = player.Group(3, 3,['yellow','red','blue'])
playerA = group.players[0]
playerB = group.players[1]
playerC = group.players[2]
playerB.receiveResources([RVector(0,0,0,0,0,0,0,0,0)])
playerA.gainIntrigue([deck.cards[15]])
print(*(playerA.intrigues))
playerA.intrigues[0].doEffect(playerA,group,quests)
print('Player A:')
print(*playerA.quests)
print('Player B:')
print(*playerB.quests)
print('Player C:')
print(*playerC.quests)