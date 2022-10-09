import math

from transportCounterDeck import TransportCounterDeck
# from server import TransportDeck
class Phase3:
    def __init__(self, player):
        self.player = player
        self.finished = False

    def execute(self, index, game):  # Add Turn
        if index == 5 and len(self.player.transport_cards) < 5:
            print("Drew Face down Transport Counter: ", game.transportDeck.facedown_cards[0].name,". At idx=", index)
            card = game.transportDeck.draw_faceDown()
            card.isFaceUp = True
            card.isFaceUp = True
            self.player.transport_cards.append(card)
        elif index >= 0 and len(self.player.transport_cards) < 5:
            print("Drew Transport Counter: ", game.transportDeck.peekFUP(index).name,". At idx=", index)
            card = game.transportDeck.draw_faceUp(index)
            card.isFaceUp = True
            self.player.transport_cards.append(card)
        if len(self.player.transport_cards) == 5:
            self.finished = True
            self.player.phase_num = 4
        game.update(self.player)
        return self.player, game

    def clickedTransportCard(self, x, y):
        index = -1
        adj = -40
        sqx = (x - 1035+adj)**2
        sqy = (y - 121+adj)**2
        area = 40
        if math.sqrt(sqx + sqy) < area:
            index = 0
        sqx = (x - 1130+adj)**2
        sqy = (y - 121+adj)**2
        if math.sqrt(sqx + sqy) < area:
            index = 1

        sqx = (x - 1214+adj)**2
        sqy = (y - 121+adj)**2
        if math.sqrt(sqx + sqy) < area:
            index = 2

        sqx = (x - 1035+adj)**2
        sqy = (y - 187+adj)**2
        if math.sqrt(sqx + sqy) < area:
            index = 3

        sqx = (x - 1130+adj)**2
        sqy = (y - 187+adj)**2
        if math.sqrt(sqx + sqy) < area:
            index = 4

        sqx = (x - 1214+adj)**2
        sqy = (y - 187+adj)**2
        if math.sqrt(sqx + sqy) < area:
            index = 5

        return index