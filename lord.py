# lords have
# two quest types or building
# amount of vp awarded

from quest import Quest

typeslist = ['Building', 'Commerce', 'Skullduggery', 'Warfare', 'Piety', 'Arcana']

class Lord:
    def __init__(self, types):
        self.types = types
        if self.types == ['building']:
            self.points = 6
        else:
            self.points = 4

    def __repr__(self):
        questtypes = ''
        if self.types == ['Building']:
            questtypes = 'Buildings'
        else:
            questtypes = str(self.types[0]) + ' and ' + str(self.types[1])
        return 'this lord has: ' + questtypes + ' for ' + str(self.points) + ' points each\n'
    
    def award(self, quests):        
        return sum(q.questtype in self.types for q in quests) * self.points
