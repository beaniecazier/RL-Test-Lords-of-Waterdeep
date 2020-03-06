#def sendAid(quest, player, group, deck):
#def establishSafeHouse(quest, player, group, deck):
#def prisonBreak(quest, player, group, deck):
#def lootCyrpt(quest, player, group, deck):
#def researchChronomancy(quest, player, group, deck):
#def lureArtisans(quest, player, group, deck):
#def placateWalkingStatue(quest, player, group, deck):
#def recruitLieutenant(quest, player, group, deck):

def assignMandatory(player, group, deck, card):
    #get opponent choice
    opponent = group.players[0]
    quest = deck.mandatory.pop(deck.mandatory.index(deck.find(card.name)))
    opponent.gainQuest([quest])

def allOpponent(player, group, deck, card):
    ovec = copy.deepcopy(card.vector)
    ovec.coin = 0
    ovec.vp = 0
    ovec.intrigue = 0
    ovec.quest = 0
    ovec.choice = 0
    if card.vector.choice != 0:
        card.vector.white = 0
        card.vector.black = 0
        card.vector.orange = 0
        card.vector.purple = 0
        card.vector.choice = 0
    for p in group.players:
        if p != player:
            if p.resources < ovec:
                player.receiveResources([card.vector])
            else:
                p.receiveResources([ovec*-1])

def chooseOneOpponent(player, group, deck, card):
    #choose opponent
    opponent = group.players[1]
    player.receiveResources([card.vector])
    opponent.receiveResources([card.vector*(1/2)])

def allOpponentChoose(player, group, deck, card):
    ovpvec = RVector(0,0,0,0,0,card.vector.vp,0,0,0)
    card.vector.vp = 0
    ovec = copy.deepcopy(card.vector)
    if ovec.black > 0 or ovec.orange > 0:
        ovec = ovec * (1/2)
    player.receiveResources([card.vector])
    #offer choice
    for p in group.players:
        if p != player:
            player.receiveResources([ovec])
            p.receiveResources([ovec*-1,ovpvec])

def biddingWar(player, group, deck, card):
    quests = [deck.draw(), deck.draw()]
    if group.numplayers > 2:
        for i in range(group.numplayers-2):
            quests.append(deck.draw())
    #group.goToCurrent()
    for i in range(group.numplayers):
        group.getCurrent().chooseFromPile(quests)
        group.nextPlayer()

def specialAssignment(player, group, deck, card):
    questtype = player.chooseQuestType()
    drawnquest = deck.draw()
    while questtype != drawnquest.questtype:
        drawnquest = deck.draw()
    player.gainQuest([drawnquest])

def callInAFavor(player, group, deck, card):
    player.receiveResources([card.vector])

def callForAdventurers(player, group, deck, card):
    player.receiveResources([card.vector])
    ovec = RVector(0,1,1,1,1,0,0,0,1)
    for p in group.players:
        if p != player:
            p.receiveResources([ovec])

def freeDrinks(player, group, deck, card):
    choice = RVector(0,0,0,0,0,0,0,0,0)
    for i in range (card.vector.choice):
        choice = player.chooseToken(choice,0,card.vector.white,card.vector.black,card.vector.orange,card.vector.purple)
    player.receiveResources([choice])
    num = random.randint(0,group.numplayers-1)
    while num == group.current:
        num = random.randint(0,group.numplayers-1)
    opponent = group.players[num]
    opponent.receiveResources([choice*-1])

""" def bribeAgent(player, group, deck, card):

def acceleratePlans(player, group, deck, card):

def changeOfPlans(player, group, deck, card):

def realEstateDeal(player, group, deck, card):

def recallAgent(player, group, deck, card):

def sampleWares(player, group, deck, card): """

def palaceOfWaterDeep(group, player):
    for p in group.players:
        p.setAmbassador(p == player)

def heroesGarden(deck, player):
    print('ERROR, Heroes\' Garden is an uncompleted building. main.py Line 53')

def buildersHall():
    # choose and buy a building from the builder's hall
    # check if player has the plot quest INFILTRATE BUILDER"S HALL completed
    return