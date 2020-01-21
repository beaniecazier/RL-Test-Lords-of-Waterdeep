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
    name = "unnamed quest"

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
    def __init__(self, questname, questtype, plot, cost, reward, verbose=False):
        self.name = questname
        self.questtype = questtype
        self.mandatory = questtype == 'Mandatory'
        self.plotquest = plot
        self.cost = RVector()
        self.reward = RVector()

        """ if verbose:
            print('Name: '+ str(self.name) + ' is a ' + str(type(self.name)))
            print('QuestType: '+ str(self.questtype) + ' is a ' + str(type(self.questtype)))
            print('CoinCost: '+ str(self.coincost) + ' is a ' + str(type(self.coincost)))
            print('CoinReward: '+ str(self.coinreward) + ' is a ' + str(type(self.coinreward)))
            print('WhiteCost: '+ str(self.whitecost) + ' is a ' + str(type(self.whitecost)))
            print('WhiteReward: '+ str(self.whitereward) + ' is a ' + str(type(self.whitereward)))
            print('BlackCost: '+ str(self.blackcost) + ' is a ' + str(type(self.blackcost)))
            print('BlackReward: '+ str(self.blackreward) + ' is a ' + str(type(self.blackreward)))
            print('OrangeCost: '+ str(self.orangecost) + ' is a ' + str(type(self.orangecost)))
            print('OrangeReward: '+ str(self.orangereward) + ' is a ' + str(type(self.orangereward)))
            print('PurpleCost: '+ str(self.purplecost) + ' is a ' + str(type(self.purplecost)))
            print('PurpleReward: '+ str(self.purplereward) + ' is a ' + str(type(self.purplereward)))
            print('VPReward: '+ str(self.vpreward) + ' is a ' + str(type(self.vpreward)))
            print('PlotQuest: '+ str(self.plotquest) + ' is a ' + str(type(self.plotquest)))
            print('Intrigue: '+ str(self.intrigue) + ' is a ' + str(type(self.intrigue))) """
        return

    def __repr__(self):
        cost = []
        """ if self.coincost > 0:
            cost.append(str(self.coincost) + ' coin' + 's' if self.coincost > 1 else '')
        if self.whitecost > 0:
            cost.append(str(self.whitecost) + ' cleric' + ('s' if self.whitecost > 1 else ''))
        if self.blackcost > 0:
            cost.append(str(self.blackcost) + ' rogue' + ('s' if self.blackcost > 1 else ''))
        if self.orangecost > 0:
            cost.append(str(self.orangecost) + ' warrior' + ('s' if self.orangecost > 1 else ''))
        if self.purplecost > 0:
            cost.append(str(self.purplecost) + ' wizard' + ('s' if self.purplecost > 1 else ''))
        
        reward = []
        if self.coinreward > 0:
            reward.append(str(self.coinreward) + ' coin' + ('s' if self.coinreward > 1 else ''))
        if self.whitereward > 0:
            reward.append(str(self.whitereward) + ' cleric' + ('s' if self.whitereward > 1 else ''))
        if self.blackreward > 0:
            reward.append(str(self.blackreward) + ' rogue' + ('s' if self.blackreward > 1 else ''))
        if self.orangereward > 0:
            reward.append(str(self.orangereward) + ' warrior' + ('s' if self.orangereward > 1 else ''))
        if self.purplereward > 0:
            reward.append(str(self.purplereward) + ' wizard' + ('s' if self.purplereward > 1 else ''))
        if self.vpreward > 0:
            reward.append(str(self.vpreward) + ' victory point' + ('s' if self.vpreward > 1 else ''))
        print(self.name)
        print(cost)
        print(reward)
        
        return "this is a " + self.questtype +  ' quest that costs ' + ', '.join(cost) + ' and rewards ' + ', '.join(reward) +'\n' """
        return

class Deck(list):

    drawcallback = []
    shufflecallback = []

    def __init__(self, iterable):
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
        quests = [Quest(names[i], questtypes[i], plots[i], costs[i], rewards[i], True) for i in range(len(names))]
        mandatory = [q for q in quests if q.questtype == 'Mandatory']
        quests.remove(mandatory)

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