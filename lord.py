# lords have
# two quest types or building
# amount of vp awarded

from quest import Quest
import random
import pandas as pd

typeslist = ['Building', 'Commerce', 'Skullduggery', 'Warfare', 'Piety', 'Arcana']
names = []

class Lord: 
    def __init__(self, name, data):
        self.name = name
        self.types = [data['type1'], data['type2']]
        if 'Building' in self.types:
            self.points = 6
        else:
            self.points = 4

    def __repr__(self):
        questtypes = ''
        if 'Building' in self.types:
            questtypes = 'Buildings'
        else:
            questtypes = str(self.types[0]) + ' and ' + str(self.types[1])
        return self.name + ' has: ' + questtypes + ' for ' + str(self.points) + ' points each'
    
    def award(self, quests):        
        return sum(q.questtype in self.types for q in quests) * self.points