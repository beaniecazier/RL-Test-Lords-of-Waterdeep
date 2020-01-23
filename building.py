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
import random

class Building:    
    def __init__(self, name, cost, effect, owner, coinpayment, tokenpayment):
        self.cost = cost
        self.name = name
        self.owner = owner
        self.effectvector = []
        self.resourcepool = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.ownervector = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.cumulative = False
        self.occupant = None
        self.showing = False
        # this is a dictionary whose key is a lambda and value is a list of parameters needed
        self.extraeffects = {}
        self.coincost = False
        self.tokencost = False

        if tokenpayment > 0:
            self.effectvector.append(RVector(0,-1,-1,-1,-1,0,0,0,tokenpayment))
            self.tokencost = True

        if coinpayment > 0:
            self.effectvector.append(RVector(-coinpayment,0,0,0,0,0,0,0,0))
            self.coincost = True

        self.effectvector.append(effect)

        if name == 'House of Good Spirits':
            self.effectvector.append(RVector(0, 0, 0, 1, 0, 0, 0, 0, 0))

        if name in ['The Golden Horn', 'Spires of the Morning', 'Jester\'s Court', 'Caravan Court', 'Tower of the Order', 'The Waymoot']:
            self.cumulative = True
            self.resourcepool = effect
        return

    def __repr__(self):
        effect = str(self.effectvector[0]) + (' and ' + str(self.effectvector[1])) if len(self.effectvector) > 1 else ""
        return self.name + ': has the use effect of ' + effect + ' and for the owner ' + str(self.ownervector) + '\n'

    def buy(self, player):
        self.owner = player
        if  self.cumulative:
            player.receiveresources([self.resourcepool])
            self.resourcepool = RVector(0,0,0,0,0,0,0,0,0)

    def use(self, player): 
        self.occupant = player

        if len(self.extraeffects) > 0:
            for effect in self.extraeffects.items():
                print(effect[0](effect[1], player))
                
        player.receiveresources([self.resourcepool] if self.cumulative else self.effectvector)

        # reset cumulative to show player has taken all resources from pile
        if self.cumulative:
            self.resourcepool = RVector(0, 0, 0, 0, 0, 0, 0, 0, 0)

        # do owner effect
        if self.owner != player:
            owner.receiveresources([self.ownervector])
        return

    def updatePile(self):
        if self.cumulative:
            for ev in self.effectvector:
                self.resourcepool += ev
        return
    
    def reveal(self):
        self.showing = True
        return self

    def clear(self):
        self.occupant = None

class Deck():
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
        self.cards = []
        self.buildings = {}
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
            self.cards.append(name)
            self.buildings[name] = Building(name, 
                                        cost_df.loc[name,'cost'], 
                                        effect, 
                                        owner, 
                                        effect_df.loc[name,'paycoin'],
                                        effect_df.loc[name,'payany'])
        return

    def draw(self):
        return self.buildings[self.cards.pop()].reveal()

    def shuffle(self):
        random.shuffle(self.cards)
        return
    
    def remove(self, name):
        if name in self.cards:
                # this throws value error if could not remove or not found
            self.cards.remove(name)
            return self.buildings[name].reveal().name
        return 'ERROR: Building not found in deck'

    def grabInitialBuildings(self, names):
        return [self.buildings[self.remove(name)] for name in names]
