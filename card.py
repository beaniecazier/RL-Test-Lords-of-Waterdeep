class Card():
    def __init__(self, name):
        self.name = name
        self.extraeffects = {}
        
    def addEffect(self, effect, params):
        self.extraeffects[effect] = params