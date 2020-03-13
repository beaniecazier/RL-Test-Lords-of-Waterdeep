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
import random
from card import Card

typeslist = ['Commerce', 'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']

class Quest(Card):
    def __init__(self, name, params, verbose=False):
        super.__init__(name)
        self.questtype = params['questtype']
        self.mandatory = self.questtype == 'Mandatory'
        self.plotquest = params['plot']
        self.cost = RVector(params['cc'],params['wc'],params['bc'],params['onc'],params['pc'],0,0,0,0)
        self.reward = RVector(params['cr'],params['wr'],params['br'],params['onr'],params['pr'],params['vp'],params['intrigue'],params['quest'],params['choice'])
        self.extraeffects = {}

        if verbose:
            print('Name: '+ str(self.name) + ' is a ' + str(type(self.name)))
            print('QuestType: '+ str(self.questtype) + ' is a ' + str(type(self.questtype)))
            print('PlotQuest: '+ str(self.plotquest) + ' is a ' + str(type(self.plotquest)))
        return

    def __repr__(self):
        return self.name + " is a " + self.questtype + ' quest that costs:\n' + str(self.cost) + ' and rewards:\n' + str(self.reward) +'\n'

    def __str__(self):
        return self.name + " is a " + self.questtype + ' quest that costs:\n' + str(self.cost) + ' and rewards:\n' + str(self.reward) +'\n'
