class Card():
    def __init__(self, name):
        self.name = name
        self.showing = False
        self.extraeffects = {}
        
    def addEffect(self, effect, params):
        self.extraeffects[effect] = params
        
    def reveal(self):
        self.showing = True
        return self