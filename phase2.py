

class Phase2:
    def __init__(self, game):
        self.finished = False
        self.g = game

    def execute(self):
        print("executing phase 2")
        for player in self.g.players:
            if len(player.transport_cards) < 5:
                card = self.g.transportDeck.draw_faceDown()
                card.isFaceUp = False #make sure
                player.transport_cards.append(card)
                if self.g.currRound == 1:
                    obs = self.g.transportDeck.draw_obstacle()
                    player.obstacle_counter = obs
            self.g.currentPhase = 3
        self.finished = True
        return self.g



