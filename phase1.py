
class Phase1:

    def __init__(self, game):
        self.finished = False
        self.g = game


    def execute(self):
        print("executing phase 1")
        for player in self.g.players:
            while len(player.travel_cards) != 8:
                player.travel_cards.append(self.g.traveldeck.draw())
            self.g.currentPhase = 1
        self.finished = True
        return self.g


