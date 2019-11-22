# choice and any are represented bythe tokens and the choice params, 
# where the tokens shoe the options and the choice is the number of times the choice and be made
# any is a choice between all 4 types of adeventurers

class RVector():
    coin = 0
    white = 0
    black = 0
    orange = 0
    purple = 0
    vp = 0
    intrigue = 0
    quest = 0
    choice = 0

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

    def __add__(self, other):
        self.coin += other.coin
        self.white += other.white
        self.black += other.black
        self.orange += other.orange
        self.purple += other.purple
        self.vp += other.vp
        self.intrigue += other.intrigue
        self.quest += other.quest
        self.choice += other.choice