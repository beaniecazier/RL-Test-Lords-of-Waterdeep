from resourcevector import RVector
import copy
import random

group = None
quests = None
intrigues = None
buildings = None
inn = None
hall = None
board = None
mandatory = None

def sync(g, q, i, bu, inn_, h, bo, m):
    global group
    global quests
    global intrigues
    global buildings
    global inn
    global hall
    global board
    global mandatory
    
    group = g
    quests = q
    intrigues = i
    buildings = bu
    inn = inn_
    hall = h
    board = bo
    mandatory = m

""" 
QUESTS
"""
#maybes
def exploreAhghaironsTower(player):
    player.receiveResources(RVector(0,0,0,0,0,0,1,0,0))

def fenceGoodsForDukeOfDarkness(player):
    player.receiveResources(RVector(2,0,0,0,0,0,0,0,0))

def bribeTheShipwrights(player):
    player.receiveResources(RVector(0,0,1,0,0,0,0,0,0))

def bolsterGriffonCavalry(player):
    player.receiveResources(RVector(0,0,0,1,0,0,0,0,0))

def produceAMiracleForTheMasses(player):
    print("ERROR unimplemented function")

def placeASleeperAgentInSkullport(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

def recoverTheMagistersOrb(player):
    print("ERROR unimplemented function")

def defendTheTowerOfLuck(player):
    player.receiveResources(RVector(0,1,1,1,1,0,0,0,1))

def studyTheIllushArch(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

def establishNewMerchantGuild(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

def infiltrateBuildersHall(player):
    player.receiveResources(RVector(0,0,0,0,0,4,0,0,0))

def protectTheHouseOfWonder(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

def installASpyInCastleWaterdeep(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

def quellMercenaryUprising(player):
    player.receiveResources(RVector(0,0,0,0,0,2,0,0,0))

#definites
def sendAidToTheHarpers(player):
    print("ERROR unimplemented function")
def establishHarpersSafeHouse(player):
    print("ERROR unimplemented function")
def prisonBreak(player):
    print("ERROR unimplemented function")
def lootTheCryptOfChauntea(player):
    print("ERROR unimplemented function")
def researchChronomancy(player):
    print("ERROR unimplemented function")
def lureArtisansOfMirabar(player):
    print("ERROR unimplemented function")
def placateTheWalkingStatue(player):
    print("ERROR unimplemented function")
def recruitLieutenant(player):
    print("ERROR unimplemented function")

""" 
INTRIGUES
"""
def chooseOneOpponent(player, group, card):
    #choose opponent
    opponent = group.players[1]
    player.receiveResources([card.vector])
    opponent.receiveResources([card.vector*(1/2)])

def conscription(player):
    global intrigues
    global group
    chooseOneOpponent(player, group, intrigues.find('Conscription'))

def crimeWave(player):
    global intrigues
    global group
    chooseOneOpponent(player, group, intrigues.find('Crime Wave'))

def goodFaith(player):
    global intrigues
    global group
    chooseOneOpponent(player, group, intrigues.find('Good Faith'))

def graduationDay(player):
    global intrigues
    global group
    chooseOneOpponent(player, group, intrigues.find('Graduation Day'))

def spreadTheWealth(player):
    global intrigues
    global group
    chooseOneOpponent(player, group, intrigues.find('Spread the Wealth'))

def allOpponentChoose(player, group, card):
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

def recruitSpies(player):
    global group
    global intrigues
    allOpponentChoose(player, group, intrigues.find('Recruit Spies'))

def requestAssistance(player):
    global group
    global intrigues
    allOpponentChoose(player, group, intrigues.find('Request Assistance'))

def researchAgreement(player):
    global group
    global intrigues
    allOpponentChoose(player, group, intrigues.find('Research Agreement'))

def summonTheFaithful(player):
    global group
    global intrigues
    allOpponentChoose(player, group, intrigues.find('Summon the Faithful'))

def taxCollection(player):
    global group
    global intrigues
    allOpponentChoose(player, group, intrigues.find('Tax Collection'))

def allOpponent(player, group, card):
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

def ambush(player):
    global group
    global intrigues
    allOpponent(player, group, intrigues.find('Ambush'))

def arcaneMishap(player):
    global group
    global intrigues
    allOpponent(player, group, intrigues.find('Arcane Mishap'))

def assassination(player):
    global group
    global intrigues
    allOpponent(player, group, intrigues.find('Assassination'))

def lackOfFaith(player):
    global group
    global intrigues
    allOpponent(player, group, intrigues.find('Lack of Faith'))

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

def bribeAgent(player, group, deck, card):
    print("ERROR unimplemented function")

def acceleratePlans(player, group, deck, card):
    print("ERROR unimplemented function")

def changeOfPlans(player, group, deck, card):
    print("ERROR unimplemented function")

def realEstateDeal(player, group, deck, card):
    print("ERROR unimplemented function")

def recallAgent(player, group, deck, card):
    print("ERROR unimplemented function")

def sampleWares(player, group, deck, card):
    print("ERROR unimplemented function")

def assignMandatory(player, group, deck, card):
    #get opponent choice
    opponent = group.players[1]
    quest = deck.pop(deck.index(card))
    opponent.gainQuest([quest])

def fendOffBandits(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Fend Off Bandits'))
    
def foiltheZhentarim(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Foil The Zhentarim'))

def placateAngryMerchants(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Placate Angry Merchants'))

def quellRiots(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Quell Riots'))

def repelDrowInvaders(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Repel Drow Invaders'))

def stampOutCultists(player):
    global group
    global mandatory
    global quests
    assignMandatory(player, group, mandatory, quests.find('Stamp Out Cultists'))

"""  
BUILDINGS
"""
def cliffwatchInn3(player):
    global inn
    innSize = len(inn)
    inn.clear()
    inn.extend([quests.draw().reveal() for i in range(innSize)])

def castleOfWaterdeep(player):
    print("ERROR unimplemented function")

def waterdeepHarber1(player):
    player.playIntrigue.doEffect(player)

def waterdeepHarber2(player):
    player.playIntrigue.doEffect(player)

def waterdeepHarber3(player):
    player.playIntrigue.doEffect(player)

def thePalaceOfWaterdeep(group, player):
    for p in group.players:
        p.setAmbassador(p == player)

def heroesGarden(deck, player):
    print('ERROR, Heroes\' Garden is an uncompleted building. main.py Line 53')

def buildersHall(player):
    # choose and buy a building from the builder's hall
    # check if player has the plot quest INFILTRATE BUILDER"S HALL completed
    return

def theStoneHouse(player):
    global board
    player.receiveResources(RVector(len(board) - 13,0,0,0,0,0,0,0,0))

def theZoarstar(player):
    player.chooseBuilding([b for b in board if b.occupant != player])

def theWaymoot(player):
    player.receiveResources(RVector(0,0,0,0,0,0,0,1,0))