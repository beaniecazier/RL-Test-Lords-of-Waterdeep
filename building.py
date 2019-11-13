# all buildings have cost
# owner
# effect
# owner effect

# Various kinds of buildings effects
# set static adventurers
# set cumulative adventurers
# set choice adventurers
# zoarstar
# set coin set static adventurers
# set coin set choice adventurers
# set adventurer choise adventurer
# dynamic coin
# set adventurer choice quest
# exchange set choice adventure for choice set adventurer
# set static adventurer intrigue card
# cumulative coin
# cumulative victory points choice quest
# spend coin for limit choice adventure
# ambassador
# conditional victory point choice quest

# various kinds of owner effects
# set choice adventurers
# limit choice adventurer
# coin
# victory points
# intrigue cards

class Building:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = None
        self.cost = 0
        self.white = 0
        self.ownerwhit = 0
        self.black = 0
        self.ownerblack = 0
        self.purple = 0
        self.ownerpurple = 0
        self.orange = 0 
        self.ownerorange = 0
        self.coin = 0
        self.ownercoin = 0
        self.cumualtivecoin = False
        self.victorypoints = 0
        self.cumulativepoints = False
        self.zoarstar = False
        return

    def ownerEffect(self):
        return

    def effect(self):
        return

    def drawIntrigue(self):
        return
    
    def chooseQuest(self):
        return
