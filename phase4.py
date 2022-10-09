import math

# from server import TransportDeck
import pygame


class Phase4:
    def __init__(self, player):
        self.player = player
        self.finished = False

    def setTransportCounters(self, idx, x, y, game):
        
        if idx == 5:    # Check if obstacle
            tc = self.player.obstacle_counter
            set, game, error = game.setTransportCounterOnPath(x, y, tc)
            if set:
                self.player.obstacle_counter = None
                self.player.message_box = str("Obstacle set on path")
                game.update(self.player)
                return self.player, game, set
            elif not set:
                print("#### phase4, setTransportCounters: Returning False.")
                if error == -1:  # Illegal Transport Counter was placed.
                    self.player.message_box = "This transport counter can not be placed in this type of road."
                game.update(self.player)
                return self.player, game, set
        else:
            tc = self.player.transport_cards[idx]
            set, game, error = game.setTransportCounterOnPath(x, y, tc)
            if set and idx == 0:
                self.player.transport_cards[idx].isFaceUp = True
                self.player.transport_cards.pop(idx)
                # self.player.message_box = "Transport Counter placement successful."
                print("#### phase4, setTransportCounters: Returning True.")
                self.player.message_box = str("Transport Counter set on path.")
                game.update(self.player)
                return self.player, game, set
            elif set:
                self.player.transport_cards.pop(idx)
                # self.player.message_box = "Transport Counter placement successful."
                print("#### phase4, setTransportCounters: Returning True.")
                self.player.message_box = str("Transport Counter set on path.")
                game.update(self.player)
                return self.player, game, set
            elif not set:
                print("#### phase4, setTransportCounters: Returning False.")
                if error == -1:  # Illegal Transport Counter was placed.
                    self.player.message_box = "This transport counter can not be placed in this type of road."
                game.update(self.player)
                return self.player, game, set

        game.update(self.player)
        return self.player, game, set


    def clickedTransportCard(self, x, y):
        index = -1
        legal = 29 # Length from center of the square
        sqx = (x - 1045)**2
        sqy = (y - 489)**2
        if math.sqrt(sqx + sqy) < legal:
            index = 0
        sqx = (x - 1128)**2
        sqy = (y - 489)**2
        if math.sqrt(sqx + sqy) < legal:
            index = 1
        sqx = (x - 1209)**2
        sqy = (y - 489)**2
        if math.sqrt(sqx + sqy) < legal:
            index = 2
        sqx = (x - 1292)**2
        sqy = (y - 489)**2
        if math.sqrt(sqx + sqy) < legal:
            index = 3
        sqx = (x - 1374)**2
        sqy = (y - 489)**2
        if math.sqrt(sqx + sqy) < legal:
            index = 4
        sqx = (x - 1018) ** 2
        sqy = (y - 741) ** 2
        if math.sqrt(sqx + sqy) < legal:
            if self.player.obstacle_counter is not None:
                index = 5
            else:
                index = -5

        return index

    def execute(self, path, transportCounter):
        self.player.transport_cards.remove(transportCounter)