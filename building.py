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

#TODO
# buildings on the board
# list of buildings that can be used
# builder's hall buildings
# player.receiveresources()
# building init
# building basic functions

# MISSING BUILDINGS
# Zoarstar
# Palace of Waterdeep
# The Stone House

import pandas as pd
from resourcevector import RVector

class Building:
    effectvector = [RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)]
    resourcepool = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)
    ownervector = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)
    owner = None
    cumulative = False
    
    def __init__(self, name, cost, effect, owner, coinpayment, tokenpayment):
        self.cost = cost
        self.name = name
        
        if name in ['The Golden Horn', 'Spires of the Morning', 'Jester\'s Court', 'Caravan Court', 'Tower of the Order', 'The Waymoot']:
            self.cumulative = True

        if name == 'House of Good Spirits':
            self.effectvector.append(RVector(0,0,0,1,0,0,0,0,0))

        self.effectvector[0].coin -= coinpayment
        return

    def __repr__(self):
        return self.name

    def use(self, player): 
        # player effect
        player.receiveresources(self.effectvector[0] if not self.cumulative else self.resourcepool)
        
        #special cases
        if self.name == 'House of Good Spirits':
            player.receiveresources(self.effectvector[1])

        # reset cumulative to show player has taken all resources from pile
        if self.cumulative:
            self.resourcepool = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)

        # do owner effect
        if self.owner != player:
            owner.receiveresources(self.ownervector)
        return

    def updatePile(self):
        if self.cumulative:
            for ev in self.effectvector:
                self.resourcepool += ev
        return

class Deck(list):
    def __init__(self):
        effect_df = pd.read_csv('buildingeffect.csv')
        cost_df = pd.read_csv('buildingcost.csv')
        owner_df = pd.read_csv('buildingowner.csv')

        # set index for each
        effect_df.set_index('name', inplace=True)
        cost_df.set_index('name', inplace=True)
        owner_df.set_index('name', inplace=True)
        # check to make sure indexes are same
        # mesh together
        # make list of indexes
        for name in cost_df.index:
            effect = RVector(effect_df.loc[name, 'coin'],
                             effect_df.loc[name, 'white'],
                             effect_df.loc[name, 'black'],
                             effect_df.loc[name, 'orange'],
                             effect_df.loc[name, 'purple'],
                             effect_df.loc[name, 'vp'],
                             effect_df.loc[name, 'intrigue'],
                             effect_df.loc[name, 'quest'],
                             effect_df.loc[name, 'choice'])
            owner = RVector(owner_df.loc[name, 'coin'],
                             owner_df.loc[name, 'white'],
                             owner_df.loc[name, 'black'],
                             owner_df.loc[name, 'orange'],
                             owner_df.loc[name, 'purple'],
                             owner_df.loc[name, 'vp'],
                             owner_df.loc[name, 'intrigue'],
                             owner_df.loc[name, 'quest'],
                             owner_df.loc[name, 'choice'])
            self.append(Building(name, cost_df.loc[name,'cost'], effect, owner, effect_df.loc[name,'paycoin'],effect_df.loc[name,'payany']))

            def draw(self):
                return self.pop()

