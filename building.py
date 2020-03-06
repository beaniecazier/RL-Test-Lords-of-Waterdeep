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
import player
from card import Card

class Building(Card):    
    def __init__(self, name, data):
        super.__init__(name)
        self.owner = None
        self.occupant = None
        self.showing = False
        self.cumulative = data['cumulative']
        self.rvectors = []
        # this is a dictionary whose key is a lambda and value is a list of parameters needed
        self.extraeffects = {}

        self.costvector = [RVector(data['cost'],0,0,0,0,0,0,0,0)]
        self.ownervector = [RVector(data['owncoin'],data['ownwhite'],data['ownblack'],data['ownorange'],data['ownpurple'],data['ownvp'],data['ownintrigue'],0,data['ownchoice'])]

        self.coincost = data['paycoin'] > 0
        self.tokencost = data['payany'] > 0
        self.payvector = [RVector(0,-1,-1,-1,-1,0,0,0,data['payany']) if self.tokencost else RVector(data['paycoin'],0,0,0,0,0,0,0,0)]

        self.usevectors = [RVector(data['coin'],data['white'],data['black'],data['orange'],data['purple'],data['vp'],data['intrigue'],data['quest'],data['choice'])]
        if name == 'House of Good Spirits':
            self.usevectors.append(RVector(0, 0, 0, 1, 0, 0, 0, 0, 0))
        if name == 'Northgate':
            self.usevectors.append(RVector(2, 0, 0, 0, 0, 0, 0, 0, 0))
        
        self.rvectors.extend(self.usevectors)

    def __repr__(self):
        name = 'Name: ' + self.name + '\n'
        if self.owner != None:
            owner = 'The {} player owns this building\n'.format(self.owner.name)
        else:
            owner = 'This building is currently not owned'
            owner += ', and is sitting in the BUILDER"S HALL\n' if self.showing else ', and is still in the deck\n'
        if self.cumulative:
            effect = 'Effect: Collect this pile,\n' + str(self.rvectors) + '\n'
        else:
            effect = 'Effect:\n' + '\n'.join([str(e) for e in self.usevectors]) + '\n'
        ownereffect = 'Owner Effect:\n' + str(self.ownervector) + '\n'
        return name + owner + effect + ownereffect
    
    def __str__(self):
        name = 'Name: ' + self.name + '\n'
        if self.owner != None:
            owner = 'The {} player owns this building\n'.format(self.owner.name)
        else:
            owner = 'This building is currently not owned'
            owner += ', and is sitting in the BUILDER"S HALL\n' if self.showing else ', and is still in the deck\n'
        if self.cumulative:
            effect = 'Effect: Collect this pile,\n' + str(self.rvectors) + '\n'
        else:
            effect = 'Effect:\n' + '\n'.join([str(e) for e in self.usevectors]) + '\n'
        ownereffect = 'Owner Effect:\n' + str(self.ownervector) + '\n'
        return name + owner + effect + ownereffect

    def buy(self, player):
        #set owner
        #move from builder's hall to board
        #if it is cumulative get the first set of resources
        self.owner = player
        if  self.cumulative:
            player.receiveresources(self.rvectors)
            self.rvectors.clear()

    def use(self, player): 
        # first check to see if player can meet pay vector
        if player.resources < self.payvector:
            print('ERROR {} player cannot pay the requirements to go to this building'.format(player.color))
            return -1

        player.receiveResources(self.payvector)
        self.occupant = player

        if len(self.extraeffects) > 0:
            for effect in self.extraeffects.items():
                effect[0](effect[1], player)

        player.receiveResources(self.rvectors)

        # do owner effect
        if self.owner != player and self.owner != None:
            self.owner.receiveResources(self.ownervector)
        
        # reset cumulative to show player has taken all resources from pile
        if self.cumulative:
            self.rvectors.clear()

        return

    def updatePile(self):
        if self.cumulative:
            self.rvectors.extend(self.usevectors)
        return
    
    def reveal(self):
        self.showing = True
        return self

    def clear(self):
        self.occupant = None
