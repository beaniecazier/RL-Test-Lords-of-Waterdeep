# choice and any are represented bythe tokens and the choice params, 
# where the tokens shoe the options and the choice is the number of times the choice and be made
# any is a choice between all 4 types of adeventurers

class RVector():
    def __init__(self, c, w, b, o, p, v, i, q, n):
        self.coin = c
        self.white = w
        self.black = b
        self.orange = o
        self.purple = p
        self.vp = v
        self.intrigue = i
        self.quest = q
        self.choice = n
    
    def __repr__(self):
        pieces = []
        if self.coin != 0:
            pieces.append(('gives' if self.coin > 0 else 'costs') +
                          (' {0!s} coin').format(abs(self.coin)) + ('s' if abs(self.coin) > 1 else ''))
        if self.white != 0:
            pieces.append(('gives' if self.white > 0 else 'costs') +
                          (' {0!s} white').format(abs(self.white)) + ('s' if abs(self.white) > 1 else ''))
        if self.black != 0:
            pieces.append(('gives' if self.black > 0 else 'costs') +
                          (' {0!s} black').format(abs(self.black)) + ('s' if abs(self.black) > 1 else ''))
        if self.orange != 0:
            pieces.append(('gives' if self.orange > 0 else 'costs') +
                          (' {0!s} orange').format(abs(self.orange)) + ('s' if abs(self.orange) > 1 else ''))
        if self.purple != 0:
            pieces.append(('gives' if self.purple > 0 else 'costs') +
                          (' {0!s} purple').format(abs(self.purple)) + ('s' if abs(self.purple) > 1 else ''))
        if self.vp != 0:
            pieces.append(('rewards' if self.vp > 0 else 'costs') +
                          (' {0!s} vp').format(abs(self.vp)) + ('s' if abs(self.vp) > 1 else ''))
        if self.intrigue != 0:
            pieces.append(('gives' if self.intrigue > 0 else 'costs') +
                          (' {0!s} intrigue').format(abs(self.intrigue)) + ('s' if abs(self.intrigue) > 1 else ''))
        if self.quest != 0:
            pieces.append(('gives' if self.quest > 0 else 'costs') +
                          (' {0!s} quest').format(abs(self.quest)) + ('s' if abs(self.quest) > 1 else ''))
        if self.choice != 0:
            pieces.append(('gives' if self.choice > 0 else 'costs') +
                          (' {0!s} choice').format(abs(self.choice)) + ('s' if abs(self.choice) > 1 else ''))
        return ', '.join(pieces)

    def __add__(self, other):
        coin = self.coin + other.coin
        white = self.white + other.white
        black = self.black + other.black
        orange = self.orange + other.orange
        purple = self.purple + other.purple
        vp = self.vp + other.vp
        intrigue = self.intrigue + other.intrigue
        quest = self.quest + other.quest
        choice = self.choice + other.choice
        return RVector(coin, white, black, orange, purple, vp, intrigue, quest, choice)

    def __sub__(self, other):
        coin = self.coin - other.coin
        white = self.white - other.white
        black = self.black - other.black
        orange = self.orange - other.orange
        purple = self.purple - other.purple
        vp = self.vp - other.vp
        intrigue = self.intrigue - other.intrigue
        quest = self.quest - other.quest
        choice = self.choice - other.choice
        return RVector(coin, white, black, orange, purple, vp, intrigue, quest, choice)

    def __lt__(self, other):
        if self.coin < other.coin: return True
        if self.white < other.white: return True
        if self.black < other.black: return True
        if self.orange < other.orange: return True
        if self.purple < other.purple: return True