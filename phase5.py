import math

from travelCard import TravelCardName


class Phase5:
    def __init__(self, player, game):
        self.player = player
        self.finished = False
        self.tempCards = self.player.travel_cards
        self.game = game

    def update_selection(self, t_card):
        self.player.selected_caravan_cards.append(t_card)
        self.player.travel_cards.remove(t_card)
        path = self.player.getPath(self.player.town, self.player.caravan_town, self.game)
        if path.has_obstacle:
            if len(self.player.selected_caravan_cards) == 4:
                print("Executing caravan movement")
                self.player = self.player.command.execute()
                self.player.message_box = "Pass or choose to move boot the Basic way or Caravan."
        else:
            if len(self.player.selected_caravan_cards) == 3:
                print("Executing caravan movement")
                self.player = self.player.command.execute()
                self.player.message_box = "Pass or choose to move boot the Basic way or Caravan."
        self.player.command = None
        return self.player


    def checkIfAvailable(self, name):
        avb = 0
        self.player.message_box = "Click on a town to move to"
        for card in self.travel_cards:
            if name is card.name:
                avb += 1
        return avb

    # def execute(self, index, game):  # Add Turn

    def selectTravelCards(self, x, y):
        print("Phase5, stepping into selectTravelCards")
        print("length of tempCards = ", len(self.tempCards))
        count = 0
        legal = 36
        sqx = (x - 1051) ** 2
        sqy = (y - 596) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.giantPig and count == 0:
                    print("Phase5, returning giantPig, 0")
                    # self.player.refreshClick()
                    count += 1
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    return card, 0
            print("Phase5, returning no giantPig, -1")
            return None, -1
        sqx = (x - 1156) ** 2
        sqy = (y - 596) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.magicCloud and count == 0:
                    print("Phase5, returning magicCloud, 0")
                    # self.player.refreshClick()
                    count += 1
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    return card, 0
            print("Phase5, returning no MC, -1")
            return None, -1
        sqx = (x - 1256) ** 2
        sqy = (y - 596) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.dragon and count == 0:
                    print("Phase5, returning dragon, 0")
                    # self.player.refreshClick()
                    count += 1
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    return card, 0
            print("Phase5, returning no drag, -1")
            return None, -1
        sqx = (x - 1361) ** 2
        sqy = (y - 596) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.trollWagon and count == 0:
                    print("phase5.py, returning trollWagon, 0")
                    # self.player.refreshClick()
                    count += 1
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    return card, 0
            print("Phase5, returning no tw, -1")
            return None, -1
        sqx = (x - 1097) ** 2
        sqy = (y - 741) ** 2
        if math.sqrt(sqx + sqy) < legal and count == 0:
            for card in self.tempCards:
                if card.name == TravelCardName.elfcycle:
                    print("Phase5, returning elfcycle, 0")
                    # self.player.refreshClick()
                    count += 1
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    return card, 0
            print("Phase5, returning no ec, -1")
            return None, -1
        sqx = (x - 1203) ** 2
        sqy = (y - 741) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.raft and count == 0:
                    print("Phase5, returning raft, 0")
                    self.player.refreshClick()
                    print("phase5.py, Player's Last Click: ", self.player.clicked[0], ", ", self.player.clicked[1])
                    count += 1
                    return card, 0
            print("Phase5, returning no raf, -1")
            return None, -1
        sqx = (x - 1308) ** 2
        sqy = (y - 741) ** 2
        if math.sqrt(sqx + sqy) < legal:
            for card in self.tempCards:
                if card.name == TravelCardName.unicorn and count == 0:
                    print("Phase5, returning unicorn, 0")
                    # self.player.refreshClick()
                    print("phase5.py, Player's Last Click: ",self.player.clicked[0], ", ", self.player.clicked[1])
                    count += 1
                    return card, 0
            print("Phase5, returning no uncrn, -1")
            return None, -1
        print("Phase5, returning None, -2")
        return None, -2

    def updateAssets(self, selected):
        self.player.town = self.player.dest
        for point in self.player.points:
            if point.town.name == self.player.dest.name:
                self.player.points.remove(point)
        self.player.dest = None
        i = 0
        for card in self.player.transport_cards:
            if card.name == selected[i].name:
                self.player.transport_cards.remove(card)
                i += 1
                break

        for card in self.player.transport_cards:
            if card.name == selected[i].name:
                self.player.transport_cards.remove(card)
                i += 1
                break

        for card in self.player.transport_cards:
            if card.name == selected[i].name:
                self.player.transport_cards.remove(card)
                i += 1
                break
        self.player.update()
