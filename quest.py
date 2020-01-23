# plot quests and reqular quests
# # quests have
# cost
#   - adventures
#   - coins
# reward
#   - victory points
#   - static set adventurers
#   - agents
#   - draw intrigue
#   - coins
#   - dynamic victory points
#   - give opponent coins
#   - choose quest
#   - set choice adventurers
#   - gain a free building
#   - play intrique
# plot quests
#   - vp for completing quests of a type
#   - lieutenant
#   - vp for buying buildings
#   - vp for plaing intrigue
#   - start of round choose set adventurers
#   - take action that provides some kind of adventurer or coin -> gain coin, draw intrigueor set static adventurer
#       * white -> replace orange, black or purple with white
#       * purple -> draw intrigue
#       * coin -> black
#       * black -> 2 coin
#       * orange -> orange
# type

import pandas as pd
from resourcevector import RVector

typeslist = ['Commerce', 'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']

class Quest:
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
    def __init__(self, questname, questtype, plot, cost, reward, verbose=False):
        self.name = questname
        self.questtype = questtype
        self.mandatory = questtype == 'Mandatory'
        self.plotquest = plot
        self.cost = cost
        self.reward = reward

        if verbose:
            print('Name: '+ str(self.name) + ' is a ' + str(type(self.name)))
            print('QuestType: '+ str(self.questtype) + ' is a ' + str(type(self.questtype)))
            print('PlotQuest: '+ str(self.plotquest) + ' is a ' + str(type(self.plotquest)))
        return

    def __repr__(self):
        return self.name + " is a " + self.questtype + ' quest that costs ' + str(self.cost) + ' and rewards ' + str(self.reward) +'\n'

class Deck():

    drawcallback = []
    shufflecallback = []

    def __init__(self):
        qdf = pd.read_csv('quest_cards.csv')
        names = qdf['name'].tolist()
        questtypes = qdf['questtype'].tolist()
        plots = qdf['plot'].tolist()
        ccs = qdf['cc'].tolist()
        wcs = qdf['wc'].tolist()
        bcs = qdf['bc'].tolist()
        oncs = qdf['onc'].tolist()
        pcs = qdf['pc'].tolist()
        crs = qdf['cr'].tolist()
        wrs = qdf['wr'].tolist()
        brs = qdf['br'].tolist()
        onrs = qdf['onr'].tolist()
        prs = qdf['pr'].tolist()
        vps = qdf['vp'].tolist()
        intrigues = qdf['intrigue'].tolist()
        qs = qdf['quest'].tolist()
        choices = qdf['choice'].tolist()
        costs = [RVector(ccs[i], wcs[i], bcs[i], oncs[i], pcs[i], 0, 0, 0, 0) for i in range(len(names))]
        rewards = [RVector(crs[i], wrs[i], brs[i], onrs[i], prs[i], vps[i], intrigues[i], qs[i], choices[i]) for i in range(len(names))]
        self.quests = [Quest(names[i], questtypes[i], plots[i], costs[i], rewards[i]) for i in range(len(names))]
        self.mandatory = [q for q in self.quests if q.questtype == 'Mandatory']
        for q in self.mandatory:
            if q in self.quests:
                self.quests.remove(q)
            else:
                print('ERROR line 91 mandatory quest not found in quest list')

    def __repr__(self):
        return super().__repr__()

    def draw(self):
        return self.pop()

    def subscribedrawevent(self):
        return

    def subscribeshuffleevent(self):
        return

    def firecallbacks(self, callbacklist):
        for c in callbacklist:
            c()
        return

    def find(self, name):
        for q in self.mandatory: 
            if q.name == name:
                return q
        for q in self.quests: 
            if q.name == name:
                return q
        print('ERROR quest not found in deck')
        return None