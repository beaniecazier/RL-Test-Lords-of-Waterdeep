from resourcevector import RVector

class Intrigue:
    def __init__(self, name, data):
        self.name = name
        self.vector = RVector(data['coin'],data['white'],data['black'],data['orange'],data['purple'],data['vp'],data['intrigue'],data['quest'],data['choice'])
        self.effects = []
        self.text = data['text']
        return

    def addEffects(self, effects):
        self.effects.extend(effects)
    
    def doEffect(self, player, players, deck):
        # check if has plot quest PLACE A SLEEPER AGENT IN SKULLPORT completed
        for e in self.effects:
            e(player, players, deck, self)

    def __repr__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])

    def __str__(self):
        return self.name + ': ' + ','.join([e.__name__ for e in self.effects])