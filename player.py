class Player:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.white = 0
        self.black = 0
        self.purple = 0
        self.orange = 0
        self.coin = 0
        self.score = 0
        self.fp = False
        self.haslieutenant = False
        self.hasambassador = False
        self.lord = None
        self.numagents = 0
        self.buildings = None
        self.quests = None
        self.intriguecards = None
        self.totalagents = 0
        return

    def incrementWhite(self, amount):
        self.white += amount
        return

    def incrementBlack(self, amount):
        self.black += amount
        return

    def incrementOrange(self, amount):
        self.coin += amount
        return

    def incrementPurple(self, amount):
        self.coin += amount
        return

    def incrementCoin(self, amount):
        self.coin += amount
        return

    def gainLieutenant(self):
        self.haslieutenant = True
        return

    def gainAmbassador(self):
        self.hasambassador = True
        return

    def drawIntrigue(self):
        return

    def drawQuest(self):
        return

    def drawQuest(self, quest):
        return