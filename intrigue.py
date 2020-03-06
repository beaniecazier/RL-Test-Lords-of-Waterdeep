from resourcevector import RVector
from card import Card

class Intrigue(Card):
    def __init__(self, name, data):
        super.__init__(name)
        self.vector = RVector(data['coin'],data['white'],data['black'],data['orange'],data['purple'],data['vp'],data['intrigue'],data['quest'],data['choice'])
        self.effects = []
        self.text = data['text']
        return

    def doEffect(self, player, players, deck):
        # check if has plot quest PLACE A SLEEPER AGENT IN SKULLPORT completed
        for e in self.effects:
            e(player, players, deck, self)

    def __repr__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])

    def __str__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])