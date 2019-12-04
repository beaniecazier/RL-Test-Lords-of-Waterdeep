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

typeslist = ['commerce', 'skullduggery', 'warfare', 'piety', 'arcana']

class Quest:
    name = "unnamed quest"
    plotquest = False
    mandatory = False
    coincost = 0
    coinreward = 0
    whitecost = 0
    whitereward = 0
    blackcost = 0
    blackreward = 0
    orangecost = 0
    orangereward = 0
    purplecost = 0
    purplereward = 0
    vpreward = 0
    intrigue = 0

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
    def __init__(self, questname, questtype, cc, cr, wc, wr, bc, br, onc, onr, pc, pr, vp, plot, intrigue, verbose=False):
        self.name = questname
        self.questtype = questtype
        self.coincost = int(cc)
        self.coinreward = int(cr)
        self.whitecost = int(wc)
        self.whitereward = int(wr)
        self.blackcost = int(bc)
        self.blackreward = int(br)
        self.orangecost = int(onc)
        self.orangereward = int(onr)
        self.purplecost = int(pc)
        self.purplereward = int(pr)
        self.vpreward = int(vp)
        self.plotquest = plot
        self.intrigue = int(intrigue)
        if verbose:
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
            print('Intrigue: '+ str(self.intrigue) + ' is a ' + str(type(self.intrigue)))
        return

    def __repr__(self):
        cost = []
        if self.coincost > 0:
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
        
        return "this is a " + self.questtype +  ' quest that costs ' + ', '.join(cost) + ' and rewards ' + ', '.join(reward) +'\n'

class Deck(list):

    drawcallback = []
    shufflecallback = []

    def __init__(self, iterable):
        questdf = pd.read_csv('quest_cards.csv')
        quests = [Quest(questdf.iloc[i, 0], questdf.iloc[i, 1], questdf.iloc[i, 2], questdf.iloc[i, 3], 
                        questdf.iloc[i, 4], questdf.iloc[i, 5], questdf.iloc[i, 6], questdf.iloc[i, 7], 
                        questdf.iloc[i, 8], questdf.iloc[i, 9], questdf.iloc[i, 10], questdf.iloc[i, 11], 
                        questdf.iloc[i, 12], questdf.iloc[i, 13], questdf.iloc[i, 14], True) for i in range(35)]

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