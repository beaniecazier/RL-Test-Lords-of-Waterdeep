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

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
    def __init__(self, name, questtype, cc, cr, wc, wr, bc, br, onc, onr, pc, pr, vp):
        self.name = name
        self.questtype = questtype
        self.coincost = cc
        self.coinreward = cr
        self.whitecost = wc
        self.whitereward = wr
        self.blackcost = bc
        self.blackreward = br
        self.orangecost = onc
        self.orangereward = onr
        self.purplecost = pc
        self.purplereward = pr
        self.vpreward = vp
        return

    def __repr__(self):
        cost = []
        if self.coincost > 0:
            cost.append(str(self.coincost) + ' coin' + 's' if self.coincost > 1 else '')
        if self.whitecost > 0:
            cost.append(str(self.whitecost) + ' clerics' + 's' if self.whitecost > 1 else '')
        if self.blackcost > 0:
            cost.append(str(self.blackcost) + ' rogues' + 's' if self.blackcost > 1 else '')
        if self.orangecost > 0:
            cost.append(str(self.orangecost) + ' warriors' + 's' if self.orangecost > 1 else '')
        if self.purplecost > 0:
            cost.append(str(self.purplecost) + ' wizards' + 's' if self.purplecost > 1 else '')
        
        reward = []
        if self.coinreward > 0:
            reward.append(str(self.coinreward) + ' coin' + 's' if self.coinreward > 1 else '')
        if self.whitereward > 0:
            reward.append(str(self.whitereward) + ' clerics' + 's' if self.whitereward > 1 else '')
        if self.blackreward > 0:
            reward.append(str(self.blackreward) + ' rogues' + 's' if self.blackreward > 1 else '')
        if self.orangereward > 0:
            reward.append(str(self.orangereward) + ' warriors' + 's' if self.orangereward > 1 else '')
        if self.purplereward > 0:
            reward.append(str(self.purplereward) + ' wizards' + 's' if self.purplereward > 1 else '')
        if self.vpreward > 0:
            reward.append(str(self.vpreward) + ' victory point' + 's' if self.vpreward > 1 else '')
        
        return "this is a " + self.questtype +  ' quest that costs ' + ', '.join(cost) + ' and rewards ' + ', '.join(reward) +'\n'